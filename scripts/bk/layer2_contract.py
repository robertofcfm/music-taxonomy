from __future__ import annotations

import re


RESPONSE_LAYER = "MVET-LAYER2"
VALID_SEVERITIES = {"FATAL", "WARNING", "SUGGESTION"}
VALID_DECISIONS = {"PASS", "PASS_WITH_WARNINGS", "FAIL"}
VALID_RESULTS = {"PASS", "FAIL"}
LAYER2_RULE_REQUIRED_FIELDS = {
    "rule_id",
    "fb",
    "severity",
    "description",
    "check",
}

PROMPT_PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def find_unresolved_placeholders(text: str) -> list[str]:
    return sorted(set(PROMPT_PLACEHOLDER_RE.findall(text)))


def compute_decision(fatal_count: int, warning_count: int, suggestion_count: int) -> str:
    if fatal_count:
        return "FAIL"
    if warning_count or suggestion_count:
        return "PASS_WITH_WARNINGS"
    return "PASS"