"""Run the full expense report through Sapling and write data/results.json."""
import concurrent.futures as cf
import json
import sys

from sapling import triage, verify

report = json.load(open("data/report.json"))


def run(line):
    res = verify(line["policy"], line["evidence"], line["claim"])
    return line["id"], {"sapling": res, "triage": triage(res)}


with cf.ThreadPoolExecutor(len(report["lines"])) as ex:
    results = dict(ex.map(run, report["lines"]))
json.dump(results, open("data/results.json", "w"), indent=2)

tot = {}
for l in report["lines"]:
    t = results[l["id"]]["triage"]
    tot[t["action"]] = tot.get(t["action"], 0) + l["amount"]
    print(f'{l["id"]} {l["amount"]:>7.2f}  {t["action"]:<13} lean={t["lean"]:<25} p={t["confidence"]:.2f}  status={results[l["id"]]["sapling"]["status"]}')
print()
for a, v in tot.items():
    print(f"{a:<13} GBP {v:,.2f}")
