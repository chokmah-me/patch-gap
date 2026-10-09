#!/usr/bin/env python3
"""Publish Patch-Gap paper v1.2 under concept 21910874 (draft 23262565)."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

TOKEN = os.environ.get("ZENODO_TOKEN")
if not TOKEN:
    sys.exit("ZENODO_TOKEN not set")

API = "https://zenodo.org/api"
ROOT = Path(r"C:\Users\Elke Shayna\Documents\00Dev\patch-gap")
PDF = ROOT / "PAPER_PATCHGAP-REL.pdf"
META = ROOT / "results" / "zenodo_v12_metadata.json"
DRAFT_ID = 23262565


def req(method: str, url: str, data: bytes | None = None, content_type: str | None = None) -> dict:
    headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
    if content_type:
        headers["Content-Type"] = content_type
    r = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=180) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        err = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"{method} {url} -> {exc.code}\n{err}") from exc


def main() -> None:
    if not PDF.is_file() or PDF.stat().st_size < 100_000:
        sys.exit(f"bad pdf: {PDF} size={PDF.stat().st_size if PDF.is_file() else 'missing'}")
    meta = json.loads(META.read_text(encoding="utf-8"))
    draft = req("GET", f"{API}/deposit/depositions/{DRAFT_ID}")
    if draft.get("state") != "unsubmitted":
        sys.exit(f"unexpected state {draft.get('state')}")
    for f in draft.get("files") or []:
        fid = f.get("id")
        name = f.get("filename") or f.get("key")
        if fid:
            print(f"delete inherited {name} {fid}")
            req("DELETE", f"{API}/deposit/depositions/{DRAFT_ID}/files/{fid}")
    draft = req("GET", f"{API}/deposit/depositions/{DRAFT_ID}")
    bucket = draft["links"]["bucket"]
    print(f"upload {PDF.name} {PDF.stat().st_size}")
    req("PUT", f"{bucket}/{PDF.name}", PDF.read_bytes(), "application/octet-stream")
    payload = json.dumps({"metadata": meta}).encode("utf-8")
    print(f"PUT metadata {len(payload)} bytes")
    check = req("PUT", f"{API}/deposit/depositions/{DRAFT_ID}", payload, "application/json")
    files = [f.get("filename") or f.get("key") for f in (check.get("files") or [])]
    print("verify title", check.get("metadata", {}).get("title"))
    print("verify version", check.get("metadata", {}).get("version"))
    print("verify date", check.get("metadata", {}).get("publication_date"))
    print("verify files", files)
    print("verify related", [
        f"{x.get('relation')}:{x.get('identifier')}"
        for x in (check.get("metadata", {}).get("related_identifiers") or [])
    ])
    if files != [PDF.name]:
        sys.exit(f"file list mismatch: {files}")
    if check.get("metadata", {}).get("version") != "1.2":
        sys.exit("version not 1.2")
    print("PUBLISH")
    published = req("POST", f"{API}/deposit/depositions/{DRAFT_ID}/actions/publish")
    out = {
        "id": published.get("id") or published.get("record_id"),
        "doi": published.get("doi") or (published.get("metadata") or {}).get("doi"),
        "conceptdoi": published.get("conceptdoi"),
        "conceptrecid": published.get("conceptrecid"),
        "version": (published.get("metadata") or {}).get("version"),
        "pdf_bytes": PDF.stat().st_size,
        "url": f"https://zenodo.org/records/{published.get('id') or DRAFT_ID}",
        "state": published.get("state"),
    }
    print(json.dumps(out, indent=2))
    (ROOT / "results" / "zenodo-publish.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
