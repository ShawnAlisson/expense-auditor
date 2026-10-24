"""Minimal client for the Banyan Sapling HF endpoint (no auth, stdlib only)."""
import json
import os
import urllib.request

ENDPOINT = os.getenv(
    "SAPLING_URL", "https://6adbee0669a00298cd4774c9.endpoints.huggingface.cloud"
)


def verify(policy: str, evidence: str, claim: str, timeout: int = 90) -> dict:
    body = json.dumps({"inputs": {"policy": policy, "evidence": evidence, "claim": claim}}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


# Triage: Sapling's calibrated `status` is deliberately conservative (the model card reports
# ~45% answer coverage), so we act on the raw label only when its probability is high,
# and send everything else to a person together with the model's lean.
CONFIDENT = 0.75
ACTIONS = {
    "supported": "APPROVE",
    "violation": "REJECT",
    "insufficient_information": "REQUEST DOCS",
    "inconsistent_context": "ESCALATE",
}


def triage(res: dict) -> dict:
    label = res["raw_label"]
    p = res["probabilities"][label]
    if p >= CONFIDENT:
        action, tier = ACTIONS[label], "auto"
    else:
        action, tier = "HUMAN REVIEW", "review"
    return {"action": action, "tier": tier, "lean": label, "confidence": p}
