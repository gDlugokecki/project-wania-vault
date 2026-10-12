---
title: Website
type: domain
created: 2026-10-11
updated: 2026-10-12
tags: [domain]
---


# Website

The webshop, built in [[bvt-ecommerce]]. What works, and what is left before launch.

## Current state

From the [[2026-10-11 bvt-ecommerce repo review|repo review]] (last commit 2026-09-30):

- **Stack:** Medusa backend + Astro storefront with React components.
- **[[Staging shop]]** is live and auto-deploys from GitHub. No [[Production environment]] yet.
- **Works and is tested:** catalogue, cart drawer, checkout with promo codes, [[InPost]] lockers and courier, [[Tpay]] (BLIK, bank transfer), accounts with Google login, order emails via [[AWS SES]], cookie consent, [[PostHog]] analytics.
- **Language:** Polish only.

## Decisions

_None yet._

## Open questions

- [ ] [[Production environment]]: hosting, domain, deploy
- [ ] [[Legal pages]]: privacy policy placeholders; no regulamin or returns page
- [ ] Final name, domain and design from [[Brand]] (beautyvtricks.com is a test domain only)
- [ ] Real product data from [[Product]]
- [ ] Production [[Tpay]] and [[InPost]] accounts need [[Company registration]]
- [ ] Card payments exist in code but aren't offered at checkout. Intended?
- [ ] Staging admin password is committed in plain text in the repo

## Next steps

| What | Who | By when |
|---|---|---|
| Change the staging admin password and remove it from the repo | [[Greg]] | soon |
| Write regulamin and returns policy, complete privacy policy | [[Greg]], [[Greg's wife]] | before launch |
| Plan the production setup | [[Greg]] | before launch |

## Connections

- [[Product]]: product data and photos
- [[Brand]]: visual identity and copy
- [[Business]]: company details, payment accounts, invoices
- [[Launch]]

Sources: [[2026-10-11 bvt-ecommerce repo review]], [[2026-10-11 Kickoff Q&A with Greg]]
