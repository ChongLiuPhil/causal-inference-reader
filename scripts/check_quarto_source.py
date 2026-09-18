from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
manuscript = root / "manuscript"
expected = [
    "frontmatter-preface.qmd",
    "frontmatter-guide.qmd",
    "01-questions.qmd",
    "02-history.qmd",
    "03-philosophies.qmd",
    "04-potential-outcomes-identification.qmd",
    "05-scm-graphs.qmd",
    "06-identification-calculus.qmd",
    "07-design-estimation.qmd",
    "08-discovery.qmd",
    "09-transportability.qmd",
    "10-causal-ml-applications.qmd",
    "11-synthesis-open-problems.qmd",
    "appendix-A-comparative-topics.qmd",
    "appendix-B-glossary-learning.qmd",
    "appendix-C-exercises.qmd",
    "appendix-D-primary-reading.qmd",
]
errors = []
missing = [name for name in expected if not (manuscript / name).is_file()]
if missing:
    errors.append("missing manuscript files: " + ", ".join(missing))

files = [manuscript / name for name in expected if (manuscript / name).is_file()]
text = "\n".join(p.read_text(encoding="utf-8") for p in files)
placeholder = re.compile(
    r"(?mi)^\s*(?:TODO|TBD|FIXME|待补|待写|占位)(?:\s*[:：-].*)?\s*$"
)
for match in placeholder.finditer(text):
    errors.append(f"placeholder line remains: {match.group(0).strip()}")

for pattern in (
    r"\\chapter\{", r"\\section\{", r"\\subsection\{",
    r"\\textcite\{", r"\\parencite\{", r"\\begin\{document\}",
    r"WEBTABLE\d+", r"WEBTIKZ\d+", r"web-assets/",
):
    if re.search(pattern, text):
        errors.append(f"legacy migration markup remains: {pattern}")

bib = (root / "references.bib").read_text(encoding="utf-8")
bibkeys = set(re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)", bib))
# Validate unambiguous Pandoc bracket citations only. Bare @tokens can be ordinary
# handles/usernames in prose or code; Quarto/Pandoc remains responsible for
# interpreting narrative citations during the full render.
citation_groups = re.findall(r"\[[^\]\n]*@[^\]\n]+\]", text)
cited = {
    key
    for group in citation_groups
    for key in re.findall(r"(?<![\w@])@([A-Za-z0-9_:.+-]+)", group)
}
missing_keys = sorted(key for key in cited if key not in bibkeys)
if missing_keys:
    errors.append("missing bibliography keys: " + ", ".join(missing_keys[:30]))

asset_refs = set(re.findall(r"\.\./assets/([^\s\"')>]+)", text))
for rel in sorted(asset_refs):
    if not (root / "assets" / rel).exists():
        errors.append(f"missing asset: assets/{rel}")

if errors:
    print("Quarto source validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(f"Validated {len(files)} manuscript files and {len(cited)} bracket citation keys.")
