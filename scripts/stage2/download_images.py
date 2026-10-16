#!/usr/bin/env python3
"""Phase 1 — download all :::image images to assets/images/ with normalized names.

Naming: {subject_abbr}_{subtopic_slug}_{NN}.{ext}
Manifest: scripts/stage2/images_manifest.json
Also copies inputs/upsc_readymade_resource_guide.png -> assets/images/cover_candidate_resource_guide.png

Re-run: python3 scripts/stage2/download_images.py [--force]
"""
import json
import re
import shutil
import sys
import time
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INV = REPO / "scripts" / "stage2" / "v17_inventory.json"
IMG_DIR = REPO / "assets" / "images"
MANIFEST = REPO / "scripts" / "stage2" / "images_manifest.json"

SUBJ_ABBR = {
    "HISTORY": "hist",
    "GEOGRAPHY": "geog",
    "SOCIETY": "soci",
    "POLITY": "poli",
    "GOVERNANCE": "gove",
    "INTERNATIONAL RELATIONS": "ir",
    "SOCIAL JUSTICE": "soju",
    "ENVIRONMENT": "envi",
    "SCIENCE & TECHNOLOGY": "scitech",
    "INTERNAL SECURITY": "inte",
    "INDIAN ECONOMY": "econ",
    "AGRICULTURE": "agri",
    "DISASTER MANAGEMENT": "disa",
    "ETHICS, INTEGRITY & APTITUDE": "ethi",
}

UA = "Mozilla/5.0 (X11; Linux x86_64) ebook-build/1.0 (image ingest)"


def magic_ext(b: bytes):
    if b.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if b.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if b.startswith(b"GIF87a") or b.startswith(b"GIF89a"):
        return "gif"
    if b.startswith(b"RIFF") and b[8:12] == b"WEBP":
        return "webp"
    if b[4:8] == b"ftyp" and b[8:12] in (b"avif", b"avis", b"mif1"):
        return "avif"
    if b.lstrip()[:4].lower() == b"<svg" or b.lstrip()[:5].lower() == b"<?xml":
        return "svg"
    return None


def avif_to_png(avif_bytes: bytes) -> bytes:
    """Convert AVIF to PNG via ffmpeg (safer format for editable/printable HTML)."""
    import subprocess
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        src, dst = Path(td) / "in.avif", Path(td) / "out.png"
        src.write_bytes(avif_bytes)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), str(dst)], check=True)
        return dst.read_bytes()


def slug(s, n=40):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s[:n].strip("-") or "x"


def fetch(url, timeout=30, retries=2):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "image/*,*/*;q=0.8"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2)
    raise last


def main():
    data = json.loads(INV.read_text(encoding="utf-8"))
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    # resume support: reuse successful downloads from a previous manifest
    prev_by_url = {}
    if MANIFEST.exists():
        try:
            prev = json.loads(MANIFEST.read_text(encoding="utf-8"))
            for e in prev.get("entries", []):
                if e.get("status") == "ok" and e.get("local_filename") and (IMG_DIR / e["local_filename"]).exists():
                    prev_by_url[e["url"]] = e
        except Exception:  # noqa: BLE001
            pass

    items = []
    for c in data["cards"]:
        for u in c["image_urls"]:
            u = u.strip()
            if u.startswith("http"):
                items.append({"url": u, "card_id": c["id"], "subject": c["subject"], "subtopic": c["subtopic"]})
    by_url = {}
    for it in items:
        by_url.setdefault(it["url"], []).append(it)
    print(f"image blocks: {len(items)}  unique urls: {len(by_url)}")

    seq = defaultdict(int)
    manifest, ok, broken = [], 0, 0
    for url, its in sorted(by_url.items()):
        first = its[0]
        abbr = SUBJ_ABBR.get(first["subject"], slug(first["subject"], 8))
        key = (abbr, slug(first["subtopic"]))
        seq[key] += 1
        stem = f"{abbr}_{key[1]}_{seq[key]:02d}"
        entry = {
            "url": url,
            "card_ids": sorted({x["card_id"] for x in its}),
            "subject": first["subject"],
            "subtopic": first["subtopic"],
            "local_filename": None, "status": None, "bytes": 0, "error": None,
        }
        if url in prev_by_url:
            manifest.append(prev_by_url[url])
            print(f"  [skip] {prev_by_url[url]['local_filename']} (already downloaded)")
            continue
        try:
            raw = fetch(url)
            ext = magic_ext(raw[:64])
            if ext == "avif":
                try:
                    raw = avif_to_png(raw)
                    ext = "png"
                except Exception as ce:  # noqa: BLE001
                    entry["error"] = f"avif->png conversion failed: {ce}"[:200]
            if ext is None:
                entry["status"], entry["error"] = "broken", "not an image (unrecognized magic bytes)"
                broken += 1
            elif len(raw) <= 3072:
                entry["status"], entry["error"] = "broken", f"suspiciously small ({len(raw)} bytes)"
                broken += 1
            else:
                fname = f"{stem}.{ext}"
                (IMG_DIR / fname).write_bytes(raw)
                entry.update(status="ok", local_filename=fname, bytes=len(raw))
                ok += 1
        except Exception as e:  # noqa: BLE001
            entry["status"], entry["error"] = "broken", f"{type(e).__name__}: {e}"[:200]
            broken += 1
        manifest.append(entry)
        info = entry.get("bytes") or entry.get("error")
        print(f"  [{entry['status']}] {stem} <- {url.rsplit('/', 1)[-1]} ({info})")
        time.sleep(1)

    src_png = REPO / "inputs" / "upsc_readymade_resource_guide.png"
    dst_png = IMG_DIR / "cover_candidate_resource_guide.png"
    if src_png.exists():
        shutil.copyfile(src_png, dst_png)

    out = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "total_blocks": len(items),
        "unique_urls": len(by_url),
        "ok": ok,
        "broken": broken,
        "entries": manifest,
    }
    MANIFEST.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nDONE: ok={ok} broken={broken}  manifest={MANIFEST}")
    print(f"cover candidate copied: {dst_png.name}")


if __name__ == "__main__":
    main()
