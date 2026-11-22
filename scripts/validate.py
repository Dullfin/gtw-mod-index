"""Checks mods.json: valid JSON, required fields, unique ids, known dependencies."""
import json
import re
import sys

errors = []

with open("mods.json", encoding="utf-8") as f:
    try:
        index = json.load(f)
    except json.JSONDecodeError as e:
        sys.exit(f"mods.json is not valid JSON: {e}")

if index.get("schemaVersion") != 1:
    errors.append("schemaVersion must be 1")

mods = index.get("mods")
if not isinstance(mods, list):
    sys.exit("mods.json needs a \"mods\" array")

ids = [m.get("id") for m in mods]
for i, mod in enumerate(mods):
    where = f"mods[{i}] ({mod.get('id', '?')})"
    for field in ("id", "name"):
        if not isinstance(mod.get(field), str) or not mod[field].strip():
            errors.append(f"{where}: \"{field}\" is required")
    repo, url = mod.get("repo"), mod.get("downloadUrl")
    if not repo and not url:
        errors.append(f"{where}: needs \"repo\" or \"downloadUrl\"")
    if repo and not re.fullmatch(r"[\w.-]+/[\w.-]+", repo):
        errors.append(f"{where}: \"repo\" must look like owner/name")
    if url and not url.startswith("https://"):
        errors.append(f"{where}: \"downloadUrl\" must be https")
    if mod.get("sha256") and not re.fullmatch(r"[0-9a-fA-F]{64}", mod["sha256"]):
        errors.append(f"{where}: \"sha256\" must be 64 hex characters")
    for dep in mod.get("dependencies", []):
        if dep not in ids:
            errors.append(f"{where}: dependency \"{dep}\" is not in the list")
    if ids.count(mod.get("id")) > 1:
        errors.append(f"{where}: duplicate id")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(mods)} mod(s)")
