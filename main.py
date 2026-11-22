#!/usr/bin/env python3
"""Write one 30-day money plan to /output/entry.txt.

The plan: sell $49 AI support chatbots to Shopify stores that have no live
chat yet. Day 1 builds a single reusable template plus a 30-second demo;
days 2-30 are pure outreach (100 stores a day, demo emailed to owners)
closing 2 clients a week at $49 setup + $19/month. The $100 covers a
domain, an email inbox and hosting. Eight clients by day 30 means $392
in setup fees plus $152/month in recurring revenue. The median day-30
outcome the plan is built around is those eight clients: no single
sale, no viral moment and no luck is needed for the math to hold.
"""

import os

PLAN = (
    "Sell $49 AI support chatbots to Shopify stores with no live chat. "
    "Day 1: build a template (FAQs, order tracking, discounts) + 30-sec demo. "
    "Then: find 100 stores/day, email owners the demo, close 2/week at "
    "$49 + $19/mo. $100: domain, email, hosting. "
    "8 clients = $392 + $152/mo."
)


def main():
    text = PLAN.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"plan is {len(text)} chars, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
