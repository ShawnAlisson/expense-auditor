## Side-quest submission (paste in Discord, side-quests)
Team: <YOUR TEAM NAME>
Task: Expense Auditor checks every line of an expense report against the written policy and receipts with Banyan Sapling, routes reject/request docs/escalate, and re-judges live when you attach the missing evidence.
X: <X POST LINK>
LinkedIn: <LINKEDIN POST LINK>
Repo: <REPO LINK>

## X post (tag @MubitLabs, attach docs/screenshot-fixed.png, and docs/screenshot.png as second image)
An employee claimed mileage for driving to Manchester. Same day, they also claimed the train ticket for that trip.

@MubitLabs Banyan Sapling flagged it: inconsistent_context, 0.76. It also rejected a GBP 195 hotel against a GBP 130 cap (0.93) and asked for the missing rate on a cropped invoice (0.91).

Then attach the manager's approval and Sapling re-judges live: REJECT 0.93 -> leans supported 0.52. Where it's near 50/50, a human signs off, never auto-approve.
Expense Auditor: every expense line is a claim, checked against policy + receipts.
<REPO LINK>

## LinkedIn post (tag Mubit)
Expense reports are a pile of small claims: "this hotel is within the cap," "this dinner had no alcohol," "this mileage was real." I built Expense Auditor for the Mubit x Night Shift Banyan Sapling side quest.

Each line becomes a claim. Sapling checks it against the policy clause and the evidence (receipts, logs, dates) and returns one of four verdicts: approve, reject, request documents, or escalate a conflict.

On a synthetic 11-line report: rejected an over-cap hotel (0.93), wine on a dinner bill (0.92), a claim submitted 54 days late (0.78), asked for a cropped invoice's missing rate (0.91), and escalated mileage claimed for a trip already paid for by train (0.76).

Click "attach manager's approval" and Sapling re-judges the line live: reject at 0.93 becomes lean-supported at 0.52, so it goes to a person.

What I learned: on this research preview, Sapling's calibrated status was "unsure" on every line, and it sat near 50/50 on compliant lines. So the tool only acts automatically above 0.75 and sends the rest to a person with the model's lean attached. The README lists where it was and wasn't right.

Repo: <REPO LINK>
Mubit
