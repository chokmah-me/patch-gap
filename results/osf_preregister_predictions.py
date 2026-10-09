#!/usr/bin/env python3
"""Create and submit OSF Theory-Based Predictions registration for patch-gap P1-P3.

Does not print OSF_TOKEN. Does not create an OSF project child under 5jefh.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SCHEMA_ID = "697b72e611a8e98484c61367"
LICENSE_ID = "563c1cf88c5e4a3877f9e96a"  # CC-By Attribution 4.0 International
API = "https://api.osf.io/v2"
ROOT = Path(__file__).resolve().parents[1]
RESULTS = Path(__file__).resolve().parent

TITLE = "Preregistration of three public falsifiers for The Governance Patch-Gap (P1-P3)"
DESCRIPTION = (
    "Time-stamped scoring rules for three binary predictions from Bilar (2026), "
    "The Governance Patch-Gap. P1: AI-generated substantive comments in a U.S. "
    "federal rulemaking at >=5% by end of 2027. P2: a firm acts on an AI-found "
    "regulatory gap with on-record attribution by end of 2027. P3: at least two "
    "national governments or the EU publicly red-team draft legislation with AI "
    "by mid-2028. All three are open as of 2026-10-09. The same predictions "
    "already appear in paper v1.2 (10.5281/zenodo.23262565); this registration "
    "freezes the scoring rules before the outcome deadlines."
)

RESPONSES = {
    "343-2": """PRIOR PUBLICATION. These three predictions were published on 2026-10-09 in Bilar, D. Y. (2026), The Governance Patch-Gap: Machine-Speed Exploit Discovery Against Human-Speed Legal Repair, v1.2, https://doi.org/10.5281/zenodo.23262565 (concept https://doi.org/10.5281/zenodo.21910874), paper section 7. This OSF registration does not claim that the predictions were unpublished before this timestamp. It freezes the scoring rules before the outcome windows close (P1 and P2: 2027-12-31; P3: 2028-06-30). No prediction is resolved as of 2026-10-09.

THEORY. A statute is a specification; a regulation is an implementation; a judicial opinion is a patch; a legal loophole is a vulnerability. H.L.A. Hart splits a legal rule into a core of settled meaning and a penumbra of open texture. Highly Optimized Tolerance (HOT) says residual breakage concentrates at the edge of the design envelope. The governance patch-gap is the ratio G = Rd / Rp, where Rd is the rate at which exploitable ambiguities reach enforcement relevance and Rp is the rate at which they are closed. The stock S of known-but-unpatched ambiguities obeys dS/dt = Rd - Rp. Three adversary classes (corporate optimizer, state actor, misaligned autonomous agent) produce different trees. Exploit discovery and exploit execution are different problems.

The three predictions are public falsifiers of the claim that machine-speed discovery against human-speed legal repair will show up in legal and regulatory practice at the stated scale. They are not a test of the G formula as an equation, and they are not a measurement of G.

Known near-misses as of 2026-10-09 are frozen as not resolving any prediction: Technology Policy Institute 2026-02-05, two FCC proceedings, 2 of 144 comments (about 1.4%) fully AI-generated; Blair-Stanek et al. LLM tax strategy from researchers, not a firm acting; BCBSA 2026-09-24 hospital coding-intensity shift attributed to AI revenue-cycle tools by a payer association, not an enforcement record; Estonia civic bill-scanning prototype; Italy Chamber of Deputies drafting-standards checks.""",
    "343-4": """Geographic scope. P1: United States federal rulemaking proceedings. P2: any firm whose action can appear in an enforcement record, 8-K, or official report (U.S. surface is the primary expected path; a non-U.S. official report of the same kind also qualifies). P3: national governments or the European Union.

Temporal scope. P1 and P2: events documented on or before 2027-12-31. P3: deployments and public reports on or before 2028-06-30.

Universe of cases. All qualifying public events in those windows. Not a sampled subset. The registration does not cherry-pick jurisdictions or dockets after a candidate appears.

Out of scope (do not count as hits). Agency use of AI to process received comments (P1). Form letters and mass campaigns without individually reasoned arguments identifying specific ambiguities (P1). Researcher-only demonstrations without a firm acting (P2). Civic or parliamentary drafting-standards tools without official red-team deployment and public reports on discovered ambiguities (P3). The BCBSA hospital coding shift is an auxiliary signal for P2 and does not resolve P2.""",
    "343-7": """Independent variable. Continued cheap machine search over legal and regulatory text. This capability is already present as of 2026-10-09 (adjacent formal-system work-factor collapse; civic bill scanners; revenue-cycle coding tools). The predictions are occurrence forecasts given that independent variable remaining in force.

Primary outcome variables (binary).
P1: at least one U.S. federal rulemaking proceeding has >=5% of its substantive comments classified as fully AI-generated by a named detector whose error rate is reported; comments are individually reasoned legal arguments identifying specific ambiguities, generated on behalf of commenting parties.
P2: at least one documented case of a firm using an AI system to identify and act on a regulatory gap, with the firm or an enforcement agency attributing the gap-finding to an AI system in an enforcement record, 8-K, or official report.
P3: at least two national governments, or the EU as one of those two, deploy AI to red-team draft legislation before enactment and produce public reports on discovered ambiguities.

Auxiliary outcome (tracked; does not resolve P2). A synchronized shift in a formally permitted practice across unrelated firms within a short window, attributed to AI tools by an industry body or regulator. First instance: BCBSA, 2026-09-24.

No mediating or moderating variables are scored.""",
    "343-9": """Each primary outcome is a predicted occurrence (binary true) by its deadline. A miss (still false at the deadline) counts against that prediction.

The paper does not claim a joint conjunction of P1, P2, and P3. Score each separately. The primary accuracy metric is the count of predictions correct (0, 1, 2, or 3).

The auxiliary BCBSA-style signal is not a predicted effect on P2's scored value. It is reported alongside P2 and never substituted for P2's attribution requirement.

If the independent variable failed (machine search over legal text became unavailable or cost-prohibitive before a deadline), that prediction would be out of scope rather than a miss. That failure has not occurred as of 2026-10-09 and is not expected.""",
    "343-12": """Public documents only. No private interviews as the resolving record.

P1. Source: the agency docket, researchers analyzing the comment corpus, or investigative journalism. Unit: one U.S. federal rulemaking proceeding. Numerator: comments classified as fully AI-generated by a named detector with a reported error rate. Denominator: substantive comments in that proceeding. Threshold: at least 5%. Content filter: individually reasoned arguments identifying specific ambiguities; not form letters; on behalf of commenting parties, not the agency's own comment-processing tools. Frozen below-threshold observation: TPI 2026-02-05, two FCC proceedings, 2/144 (about 1.4%).

P2. Source: enforcement record, 8-K filing, or official report. Required elements: (a) a firm identified a regulatory gap using an AI system; (b) the firm acted on that gap; (c) the firm or an enforcement agency attributes the gap-finding to AI in that record. Frozen non-resolving items: Blair-Stanek et al. (researchers, not a firm acting); BCBSA 2026-09-24 (payer association attribution, not an enforcement record).

P3. Source: official government or EU publication. Required elements: deployment of AI to red-team draft legislation before enactment, and public reports on discovered ambiguities, from at least two national governments or from the EU counted toward that two. Frozen non-resolving items: Estonia civic prototype; Italy Chamber drafting-standards checks.

Machine-checked ledger (not the registration itself): gates/predictions.json in companion software v0.2.0, https://doi.org/10.5281/zenodo.21918091.""",
    "343-14": """Absence of a qualifying public record at the deadline is scored resolved-false, not missing. There is no interpolation.

Incomplete candidates (wrong document type, missing attribution, detector without a reported error rate, civic rather than official deployment) stay open until they become complete or the deadline passes.

For P2, firms may never attribute gap-finding to AI on the record. The paper states that an open or false status may therefore reflect non-disclosure rather than non-occurrence. That possibility does not convert an open P2 into a pass, and it does not treat missing attribution as missing data to be imputed.""",
    "343-17": """Primary metric: count of the three binary predictions that are resolved-true at their deadlines (range 0-3). Each prediction is scored independently.

Review dates. P1 and P2: 2028-01-07. P3: 2028-07-07. Status may be resolved-true earlier if a qualifying record appears.

No Brier scores, ranked probability scores, or logarithmic loss. These are occurrence forecasts with public binary criteria.

The auxiliary BCBSA-style signal is reported in the ledger and is never substituted for P2.

Independent-variable caveat (per template): if machine search over legal text were no longer cheap before a deadline, that prediction would not be counted for or against accuracy. That has not occurred as of registration.""",
    "343-19": """Ordinal confidence, not used to weight the 0-3 count.

P1: moderate. A named-detector measurement already exists and is below threshold (about 1.4% in two FCC dockets without mass campaigns). The 5% bar plus the ambiguity-identification content filter is the remaining hurdle.

P2: low to moderate. The event may occur while on-record attribution does not. That is a feature of the criterion, not a reason to loosen it.

P3: moderate. Civic and drafting-standards tools exist; official red-team deployments with public reports on discovered ambiguities do not, as of 2026-10-09.

Confidence is not a scoring weight.""",
    "343-21": """N/A. These are occurrence forecasts with stated public criteria, not a horse-race against an LLM, a prediction market, superforecasters, or a 50-50 mathematical baseline. A miss is a miss.""",
    "343-24": """P1 (deadline 2027-12-31). AI-generated regulatory comments at detectable scale. By end of 2027, at least one U.S. federal rulemaking proceeding will have a detectable, non-trivial fraction of its substantive comments generated by AI systems on behalf of commenting parties (as distinct from agencies' own use of AI to process received comments, which is already underway). These will be individually reasoned legal arguments identifying specific ambiguities in the proposed rule, not form letters. Documentation will come from the agency, from researchers analyzing the comment corpus, or from investigative journalism. "Non-trivial" means at least 5% of the substantive comments in the proceeding, classified as fully AI-generated by a named detector whose error rate is reported. Status at registration, 2026-10-09: open. A February 2026 analysis of two FCC proceedings found 2 of 144 comments (about 1.4%) classified as fully AI-generated and 13 with some AI signal, in proceedings without mass campaigns; that is below the threshold, and the fully AI-generated comments were not described as identifying specific ambiguities.

P2 (deadline 2027-12-31). AI-discovered legal exploit in production. By end of 2027, at least one documented case will show a firm using an AI system to identify and act on a regulatory gap, where the firm or an enforcement agency attributes the gap-finding to an AI system in an enforcement record, 8-K filing, or official report. Status at registration, 2026-10-09: open; no qualifying case found. The nearest item, the LLM-generated tax strategy in Blair-Stanek, Holzenberger, and Van Durme, came from researchers, not a firm acting on it. Firms have reasons never to attribute gap-finding to AI on the record, so an open status may reflect non-disclosure rather than non-occurrence. An auxiliary signal is tracked but does not resolve the prediction: a synchronized shift in a formally permitted practice across unrelated firms within a short window, attributed to AI tools by an industry body or regulator. The hospital coding shift reported by the Blue Cross Blue Shield Association (September 2026; share of medically complex inpatient cases 37% to 40%; about $942 million over two years; attributed to AI revenue-cycle tools) is the first instance of that signal; its attribution comes from a payer association, not from an enforcement record.

P3 (deadline 2028-06-30). Defensive deployment. By mid-2028, at least two national governments or the EU will deploy AI systems to red-team draft legislation before enactment, producing public reports on discovered ambiguities. Status at registration, 2026-10-09: open. Estonia's bill-scanning prototype is a civic tool without an official deployment or public error reports, and Italy's Chamber of Deputies uses generative AI to check bills against drafting standards; neither meets the criterion.

Predicted values: P1 true by 2027-12-31; P2 true by 2027-12-31; P3 true by 2028-06-30. Score independently.

Paper: https://doi.org/10.5281/zenodo.21910874 (always-latest PDF); this version https://doi.org/10.5281/zenodo.23262565. Ledger: gates/predictions.json in https://doi.org/10.5281/zenodo.21918091.""",
    "343-26": """Criteria (thresholds, document types, attribution rules, content filters) change only through an OSF registration update with its own timestamp. Do not silently tighten or loosen a threshold after a candidate appears.

New near-misses may be appended to the companion ledger gates/predictions.json without changing pass/fail rules.

Case-population updates: none expected. The universe is already all qualifying public events in the windows.

Independent-variable updates: only if cheap machine search over legal text ceased. Recalculate nothing else in that event; mark the affected prediction out of scope.

Outcome values are not rewritten except by the deadline scoring rule (resolved-true when a qualifying record appears; resolved-false if still unmet at the deadline).""",
    "343-29": """The author has no operational control over U.S. federal comment dockets, firm 8-K filings, enforcement records, or government red-team programs. Chokmah LLC is the author's affiliation and publishes the paper and the companion software. That is disclosed. No financial interest in any candidate firm, docket, or government program is known at registration.""",
    "343-31": """No separate funding for this registration. AI assistance in drafting the paper is disclosed in the paper's AI Utilization Statement. This registration text was prepared from paper section 7, predictions.md, and gates/predictions.json.""",
    "343-33": """Bilar, D. Y. (2026). The Governance Patch-Gap: Machine-Speed Exploit Discovery Against Human-Speed Legal Repair (v1.2). Zenodo. https://doi.org/10.5281/zenodo.21910874 (concept); https://doi.org/10.5281/zenodo.23262565 (this PDF).

Companion software: patch-gap-hot-search v0.2.0. https://doi.org/10.5281/zenodo.21918091 (concept); https://doi.org/10.5281/zenodo.23262639 (version). Ledger: gates/predictions.json.

Technology Policy Institute (2026-02-05). AI isn't flooding FCC comments. https://techpolicyinstitute.org/publications/artificial-intelligence/ai-isnt-flooding-fcc-comments/

Blair-Stanek, A., Holzenberger, N., and Van Durme, B. LLM-generated tax strategy (researcher demonstration; P2 near miss). https://taxprofblog.aals.org/2026/01/25/chatgpt-generates-a-novel-tax-strategy/

Blue Cross Blue Shield Association reporting as summarized 2026-09-24 (P2 auxiliary signal). https://fiercehealthcare.com/finance/hospitals-use-ai-coding-tools-cost-bcbsa-plans-942m-more-similar-care-analysis

Estonia civic bill-scanning prototype (P3 non-resolving). https://modparl.substack.com/p/from-slip-up-to-solution

Italy Chamber of Deputies drafting-standards checks (P3 non-resolving). https://techpolicy.press/governments-are-using-ai-to-draft-legislation-what-could-possibly-go-wrong

Miller, A. C. (2025). Registering Theory-Based Predictions in Political Science. PS: Political Science and Politics 58(1), 155-161. https://doi.org/10.1017/S1049096524000404

OSF paper mirror (legacy): https://osf.io/w96xz/""",
}


def token() -> str:
    t = os.environ.get("OSF_TOKEN", "").strip()
    if not t:
        sys.exit("OSF_TOKEN unset")
    return t


def req(method: str, url: str, payload: dict | None = None, raw: bytes | None = None, content_type: str | None = None):
    headers = {
        "Authorization": f"Bearer {token()}",
        "Accept": "application/vnd.api+json",
    }
    data = None
    if raw is not None:
        data = raw
        headers["Content-Type"] = content_type or "application/octet-stream"
    elif payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/vnd.api+json"
    r = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(r, timeout=90) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code} {method} {url}\n{err[:4000]}")
        raise


def write_protocol() -> tuple[Path, Path]:
    md = RESULTS / "osf-prereg-p1-p3.md"
    lines = [
        "# Protocol: preregistration of patch-gap P1-P3",
        "",
        "Cover. These predictions were published on 2026-10-09 in paper v1.2",
        "(https://doi.org/10.5281/zenodo.23262565). This file is the protocol",
        "attached to the OSF Theory-Based Predictions registration. It freezes",
        "scoring rules before 2027-12-31 (P1, P2) and 2028-06-30 (P3).",
        "",
    ]
    labels = {
        "343-2": "Background",
        "343-4": "Scope condition cases",
        "343-7": "Variable specification",
        "343-9": "Variable relationships",
        "343-12": "Measurement and data",
        "343-14": "Missing data",
        "343-17": "Prediction accuracy",
        "343-19": "Confidence levels",
        "343-21": "Alternative baselines",
        "343-24": "Predictions",
        "343-26": "Update criteria",
        "343-29": "Conflicts of interest",
        "343-31": "Acknowledgments",
        "343-33": "References",
    }
    for k, title in labels.items():
        lines.append(f"## {title}")
        lines.append("")
        lines.append(RESPONSES[k])
        lines.append("")
    md.write_text("\n".join(lines), encoding="utf-8")

    html_path = RESULTS / "osf-prereg-p1-p3.html"
    body = "".join(
        f"<h2>{labels[k]}</h2>\n<p>" + RESPONSES[k].replace("\n\n", "</p><p>").replace("\n", "<br>\n") + "</p>\n"
        for k in labels
    )
    html_path.write_text(
        "<!doctype html><meta charset='utf-8'><title>"
        + TITLE
        + "</title><style>body{font:16px/1.4 Georgia,serif;max-width:42rem;margin:2rem auto;padding:0 1rem}</style>"
        + f"<h1>{TITLE}</h1>"
        + "<p>Cover. Predictions published 2026-10-09 in paper v1.2 "
        "(https://doi.org/10.5281/zenodo.23262565). This protocol freezes scoring "
        "rules before the outcome deadlines.</p>"
        + body,
        encoding="utf-8",
    )
    pdf = RESULTS / "osf-prereg-p1-p3.pdf"
    edge_candidates = [
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    ]
    edge = next((p for p in edge_candidates if p.exists()), None)
    if edge:
        subprocess.run(
            [
                str(edge),
                "--headless",
                "--disable-gpu",
                f"--print-to-pdf={pdf}",
                html_path.as_uri(),
            ],
            check=False,
        )
    return md, pdf if pdf.exists() else html_path


def create_draft() -> str:
    payload = {
        "data": {
            "type": "draft_registrations",
            "attributes": {
                "title": TITLE,
                "description": DESCRIPTION,
                "category": "hypothesis",
                "tags": ["patch-gap", "preregistration", "legal-AI", "HOT", "open-texture"],
            },
            "relationships": {
                "registration_schema": {
                    "data": {"type": "registration-schemas", "id": SCHEMA_ID}
                }
            },
        }
    }
    status, body = req("POST", f"{API}/draft_registrations/", payload)
    did = body["data"]["id"]
    print("draft", did, "http", status)
    return did


def patch_draft(did: str) -> None:
    payload = {
        "data": {
            "id": did,
            "type": "draft_registrations",
            "attributes": {
                "title": TITLE,
                "description": DESCRIPTION,
                "category": "hypothesis",
                "tags": ["patch-gap", "preregistration", "legal-AI", "HOT", "open-texture"],
                "registration_responses": RESPONSES,
                "node_license": {
                    "copyright_holders": ["Daniyel Yaacov Bilar"],
                    "year": "2026",
                },
            },
            "relationships": {
                "license": {"data": {"type": "licenses", "id": LICENSE_ID}}
            },
        }
    }
    status, _ = req("PATCH", f"{API}/draft_registrations/{did}/", payload)
    print("patched", did, "http", status)


def upload_files(did: str, files: list[Path]) -> None:
    status, body = req("GET", f"{API}/draft_registrations/{did}/")
    rel = body["data"]["relationships"]
    files_url = None
    for key in ("files", "branched_from"):
        if key in rel:
            print("rel", key, rel[key].get("links", {}).get("related", {}).get("href"))
    bf = rel.get("branched_from", {}).get("links", {}).get("related", {}).get("href")
    if bf:
        st, node = req("GET", bf)
        nid = node["data"]["id"]
        print("branched_from", nid, node["data"]["type"])
        files_url = node["data"]["relationships"].get("files", {}).get("links", {}).get("related", {}).get("href")
    if not files_url:
        files_url = rel.get("files", {}).get("links", {}).get("related", {}).get("href")
    if not files_url:
        print("no files endpoint; skip upload")
        return
    st, listing = req("GET", files_url)
    # find osfstorage provider
    upload_link = None
    providers = listing.get("data") or []
    if providers and isinstance(providers, list):
        for p in providers:
            links = p.get("links") or {}
            if "upload" in links:
                upload_link = links["upload"]
                break
            href = (p.get("relationships") or {}).get("files", {}).get("links", {}).get("related", {}).get("href")
            if href:
                st, inner = req("GET", href)
                # waterbutler upload is often in links.upload of the provider itself
    if not upload_link:
        # try node files/osfstorage
        if bf:
            nid = bf.rstrip("/").split("/")[-1]
            # GET providers
            st, prov = req("GET", f"{API}/nodes/{nid}/files/")
            for p in prov.get("data") or []:
                if p.get("attributes", {}).get("name") == "osfstorage" or p.get("id", "").endswith(":osfstorage"):
                    upload_link = p.get("links", {}).get("upload")
                    print("provider", p.get("id"), "upload", bool(upload_link))
    if not upload_link:
        print("WARNING: could not find upload link")
        print(json.dumps(listing, indent=2)[:2000])
        return
    for path in files:
        if not path.exists():
            continue
        url = upload_link + ("&" if "?" in upload_link else "?") + f"kind=file&name={path.name}"
        raw = path.read_bytes()
        # Waterbutler uses the same bearer token
        headers = {
            "Authorization": f"Bearer {token()}",
            "Content-Type": "application/octet-stream",
        }
        r = urllib.request.Request(url, data=raw, method="PUT", headers=headers)
        try:
            with urllib.request.urlopen(r, timeout=120) as resp:
                print("uploaded", path.name, resp.status)
        except urllib.error.HTTPError as e:
            print("upload fail", path.name, e.code, e.read().decode("utf-8", errors="replace")[:1500])


def submit(did: str) -> dict:
    # Try register endpoint variants
    attempts = [
        (
            "POST",
            f"{API}/draft_registrations/{did}/register/",
            {
                "data": {
                    "type": "registrations",
                    "attributes": {"registration_choice": "immediate"},
                }
            },
        ),
        (
            "POST",
            f"{API}/registrations/",
            {
                "data": {
                    "type": "registrations",
                    "attributes": {
                        "draft_registration": did,
                        "registration_choice": "immediate",
                    },
                }
            },
        ),
    ]
    last_err = None
    for method, url, payload in attempts:
        try:
            status, body = req(method, url, payload)
            print("submit", url, status)
            return body
        except urllib.error.HTTPError as e:
            last_err = e
            continue
    raise SystemExit(f"submit failed: {last_err}")


def main() -> None:
    md, proto = write_protocol()
    print("protocol", md, proto)
    (RESULTS / "osf_prereg_responses.json").write_text(
        json.dumps(RESPONSES, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    did = create_draft()
    (RESULTS / "osf_prereg_draft_id.txt").write_text(did, encoding="utf-8")
    patch_draft(did)
    upload_files(did, [proto, md, ROOT.parent / "patch-gap-hot-search" / "gates" / "predictions.json"])
    body = submit(did)
    (RESULTS / "osf_prereg_submit.json").write_text(
        json.dumps(body, indent=2, ensure_ascii=False)[:200000], encoding="utf-8"
    )
    data = body.get("data") or {}
    rid = data.get("id")
    print("registration_id", rid)
    attrs = data.get("attributes") or {}
    print("public", attrs.get("public"))
    print("pending", attrs.get("pending_registration_approval"))
    print("doi_attr", attrs.get("doi"))
    if rid:
        time.sleep(2)
        try:
            st, live = req("GET", f"{API}/registrations/{rid}/")
            ident = live["data"].get("attributes", {}).get("doi")
            print("live_doi", ident)
            print("live_public", live["data"]["attributes"].get("public"))
            print("url", f"https://osf.io/{rid}/")
        except Exception as e:
            print("live fetch", e)


if __name__ == "__main__":
    main()
