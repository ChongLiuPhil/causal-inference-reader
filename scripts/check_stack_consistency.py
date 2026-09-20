#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

ROOT=Path(__file__).resolve().parents[1]
def load(p): return yaml.safe_load((ROOT/p).read_text(encoding="utf-8"))
def fail(m):
    print("ERROR:",m,file=sys.stderr)
    raise SystemExit(1)

project=load("project.yaml")
website=load("website.yaml")
stack=load("project-stack.yaml")
lock=load("project-stack.lock.yaml")

pid=stack["project"]["id"]
if project.get("id") != pid or website.get("project_id") != pid:
    fail("project-stack, project.yaml, and website.yaml project ids must agree")

gov=stack["components"]["governance"]
if project.get("governance",{}).get("adopted_protocol_commit") != gov["project_native"]["adopted_commit"]:
    fail("legacy HARC functional mapping no longer matches project.yaml")

if stack["components"]["publishing"].get("adoption_state") != "deferred":
    fail("second pilot must not silently adopt or change the publication framework")
if lock["resolved"].get("ppf") is not None:
    fail("PPF lock must remain null while PPF adoption is deferred")

if lock["resolved"].get("ahicp") != gov["adopted_commit"]:
    fail("AHICP lock drift")
if lock["resolved"].get("vault_interface") != stack["components"]["portfolio_interface"]["adopted_commit"]:
    fail("Vault Interface lock drift")
if lock["resolved"].get("starter") != stack["starter"]["adopted_commit"]:
    fail("Starter lock drift")

if not website.get("publish"):
    fail("website metadata conflicts with the project's already-authorized public Web Edition")

print("Project stack consistency passed: legacy governance mapped, public metadata standardized, PPF deferred, existing Pages route preserved.")
