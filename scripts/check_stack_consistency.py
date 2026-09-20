#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
def read(name): return (ROOT/name).read_text(encoding="utf-8")
def scalars(text):
    out = {}
    parents = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#") or ":" not in raw:
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        key, value = raw.strip().split(":", 1)
        while parents and parents[-1][0] >= indent:
            parents.pop()
        if value.strip() == "":
            parents.append((indent, key))
            continue
        path = ".".join([p[1] for p in parents] + [key])
        value = value.strip().strip('"').strip("'")
        if value == "null":
            value = None
        elif value == "true":
            value = True
        elif value == "false":
            value = False
        out[path] = value
    return out

def fail(msg):
    print("ERROR:",msg,file=sys.stderr)
    raise SystemExit(1)

project=scalars(read("project.yaml"))
website=scalars(read("website.yaml"))
stack=scalars(read("project-stack.yaml"))
lock=scalars(read("project-stack.lock.yaml"))

pid=stack.get("project.id")
if project.get("id") != pid or website.get("project_id") != pid:
    fail("project-stack, project.yaml, and website.yaml project ids must agree")

if project.get("governance.adopted_protocol_commit") != stack.get("components.governance.project_native.adopted_commit"):
    fail("legacy HARC functional mapping no longer matches project.yaml")

if stack.get("components.publishing.adoption_state") != "deferred":
    fail("second pilot must not silently adopt or change the publication framework")
if lock.get("resolved.ppf") is not None:
    fail("PPF lock must remain null while PPF adoption is deferred")

if lock.get("resolved.ahicp") != stack.get("components.governance.adopted_commit"):
    fail("AHICP lock drift")
if lock.get("resolved.vault_interface") != stack.get("components.portfolio_interface.adopted_commit"):
    fail("Vault Interface lock drift")
if lock.get("resolved.starter") != stack.get("starter.adopted_commit"):
    fail("Starter lock drift")
if website.get("publish") is not True:
    fail("website metadata conflicts with the already-authorized public Web Edition")

print("Project stack consistency passed: legacy governance mapped, public metadata standardized, PPF deferred, existing Pages route preserved.")
