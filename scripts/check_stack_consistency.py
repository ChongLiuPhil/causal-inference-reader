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
publishing=scalars(read("publishing.yaml"))
ahicp=scalars(read("AHICP_MANIFEST.yaml"))

if stack.get("schema") != "inquiry-publishing-stack/v2":
    fail("project stack must use v2")
if lock.get("schema") != "inquiry-publishing-stack-lock/v2":
    fail("project stack lock must use v2")

pid=stack.get("project.id")
if project.get("id") != pid or website.get("project_id") != pid:
    fail("project-stack, project.yaml, and website.yaml project ids must agree")

if stack.get("components.governance.adoption_state") != "active":
    fail("governance mapping must remain active")
if stack.get("components.portfolio_interface.adoption_state") != "active":
    fail("Vault Interface must remain active")
if project.get("governance.adopted_protocol_commit") != stack.get("components.governance.project_native.adopted_commit"):
    fail("legacy HARC functional mapping no longer matches project.yaml")

if stack.get("components.publishing.adoption_state") != "active":
    fail("PPF lifecycle mapping must remain active after D009")
if stack.get("components.publishing.profile") != "quarto-book-github-pages-project-native":
    fail("PPF must map the existing GitHub Pages route rather than invent a new provider")
if publishing.get("deployment.web.current_provider") != "github-pages":
    fail("publishing.yaml provider drift: current provider must remain GitHub Pages")
if publishing.get("deployment.web.target_provider") != "github-pages":
    fail("publishing.yaml target provider drift")
if publishing.get("deployment.web.integration_state") != "REPOSITORY_VALIDATED":
    fail("repository publication chain must remain validated")
if publishing.get("deployment.web.cutover_state") != "BLOCKED":
    fail("provider-side Pages binding must remain an explicit unresolved gate")
if publishing.get("publication.web.authorization_state") != "authorized":
    fail("public Web authorization drift")
if publishing.get("publication.web.visibility") != "public":
    fail("public Web visibility drift")
if lock.get("resolved.ppf") != stack.get("components.publishing.template_source_commit"):
    fail("PPF lock drift")

if stack.get("components.governance.template_source_commit") != "02d0b3c02ca23073c760b6e0f761a468e0235a1c":
    fail("unexpected AHICP template pin")
if stack.get("components.governance.project_adopted_commit") != "ed5a60b1016497472072db108072ace59bcdb65d":
    fail("unexpected AHICP adopted pin")
if ahicp.get("ahicp.adopted_protocol_commit") != "ed5a60b1016497472072db108072ace59bcdb65d":
    fail("AHICP manifest pin drift")
if stack.get("components.publishing.template_source_commit") != "9a6005de85f032095e36eea03fda317e73126538":
    fail("unexpected PPF template pin")
if stack.get("components.publishing.project_adopted_commit") != "e660b48fb216c28c8faa1f0fe2d0816401e1de2c":
    fail("unexpected PPF adopted pin")
if stack.get("components.portfolio_interface.template_source_commit") != "592c6e2e938f995b7b3e7df07a72f7f1e2c50c5a":
    fail("unexpected Vault Interface template pin")
if stack.get("components.portfolio_interface.project_adopted_commit") != "79d64b12275a5cc7c09236b144bf4213fa7afc5e":
    fail("unexpected Vault Interface adopted pin")
if stack.get("starter.adopted_commit") != "05857086e240cbd269eae91af8419ea0921c01fa":
    fail("unexpected Starter source revision")

if lock.get("resolved.ahicp") != stack.get("components.governance.template_source_commit"):
    fail("AHICP lock drift")
if lock.get("resolved.vault_interface") != stack.get("components.portfolio_interface.template_source_commit"):
    fail("Vault Interface lock drift")
if lock.get("resolved.starter") != stack.get("starter.adopted_commit"):
    fail("Starter lock drift")
if website.get("publish") is not True:
    fail("website metadata conflicts with the already-authorized public Web Edition")

print("Project stack v2 consistency passed: Stack v2 template/adopted revisions align, HARC-lite history is retained, and the existing GitHub Pages route/provider-binding gate is preserved.")
