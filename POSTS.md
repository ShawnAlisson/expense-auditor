## Side-quest submission (paste in Discord, side-quests)
Team: <YOUR TEAM NAME>
Task: Expense Auditor checks every line of an expense report against the written policy and receipts with Banyan Sapling, routes reject/request docs/escalate, and re-judges live when you attach the missing evidence.
X: <X POST LINK>
LinkedIn: <LINKEDIN POST LINK>
Repo: https://github.com/ShawnAlisson/expense-auditor

## X post (tag @MubitLabs, attach docs/screenshot-fixed.png, and docs/screenshot.png as second image)
We built and used Expense Auditor on a sample expense report. For example, we included a mileage claim for driving to Manchester, and on the same day, a train ticket was also claimed for that trip. Sapling flagged this right away for inconsistent context (0.76), demonstrating its ability to spot duplicates and contradictions. 

Sapling flagged the inconsistency (inconsistent_context, 0.76), just as designed. It also correctly rejected a £195 hotel above the £130 cap (0.93), and kicked back a cropped invoice missing the nightly rate (0.91).

When we attach the manager's approval and it judges that line again. The hotel goes from reject at 0.93 to leaning supported at 0.52. That close, a person signs off. We don't let it approve those on its own.

Expense Auditor checks each line against the policy and the receipts.
https://github.com/ShawnAlisson/expense-auditor

## LinkedIn post (tag Mubit)

We built Expense Auditor for the Mubit x Night Shift side quest, working alongside Banyan Sapling. Expense reports are full of little details—like making sure a hotel stay is under the cap, checking there’s no wine on the dinner bill, and confirming that mileage claims are for real drives.

Sapling reads each line against the policy and the evidence you actually have, then approves it, rejects it, asks for a missing document, or escalates when two things disagree.

We tried it on a made-up 11-line report. It rejected a £195 hotel against a £130 cap (0.93), wine on a client dinner (0.92), and a claim filed 54 days late (0.78). A cropped invoice with the rate cut off got sent back (0.91). Mileage to Manchester, on a day they also expensed the train, got escalated (0.76).

Attach the manager's approval and Sapling looks at that line again straight away. The hotel drops from a reject at 0.93 to leaning supported at 0.52, which is close enough that someone should actually look at it.

What I learned: on this research preview, Sapling's calibrated status was "unsure" on every line, and it sat near 50/50 on compliant lines. So the tool only acts automatically above 0.75 and sends the rest to a person with the model's lean attached. The README lists where it was and wasn't right.

https://github.com/ShawnAlisson/expense-auditor
@Mubit
