#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
errors = []
required_files = [
    "README.md","SERVICE.md","PARTNERSHIPS.md","SECURITY.md","COMPLIANCE.md",
    "docs/SAMPLE_AUDIT.md"
]
for name in required_files:
    if not (root / name).is_file():
        errors.append("missing " + name)

text = "\n".join((root / name).read_text(encoding="utf-8") for name in required_files if (root/name).is_file())
patterns = {
    r"guaranteed revenue|guaranteed savings|ضمان الربح|ربح مضمون": "guaranteed outcome",
    r"sk-[A-Za-z0-9_-]{16,}": "possible API key",
    r"gh[pousr]_[A-Za-z0-9]{20,}": "possible GitHub token",
    r"AKIA[0-9A-Z]{16}": "possible AWS key",
}
for pattern,label in patterns.items():
    if re.search(pattern,text,re.I):
        errors.append(label)

if "Validation only" not in (root/"README.md").read_text(encoding="utf-8"):
    errors.append("README must state Validation only")

if errors:
    print("VERIFY FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)
print("VERIFY PASS")
