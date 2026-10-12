---
title: 2026-10-11 bvt-ecommerce repo review
type: source
url: https://github.com/gDlugokecki/bvt-ecommerce
created: 2026-10-11
updated: 2026-10-12
tags: [source, website]
---


# 2026-10-11 bvt-ecommerce repo review

Claude read the [[bvt-ecommerce]] repo at its last commit (2026-09-30, "Adjust layouts").

## Findings

- Medusa v2 backend, Astro storefront with React, pnpm + Turborepo, shared payment and shipping package.
- [[Staging shop]] deployed to AWS EC2 via GitHub Actions. No production config.
- Built with unit and Playwright tests: catalogue, cart, checkout, promo codes, [[InPost]], [[Tpay]], accounts, Google login, emails via [[AWS SES]], cookie consent, [[PostHog]].
- Privacy policy has "DO UZUPEŁNIENIA" placeholders; no regulamin or returns page. → [[Legal pages]]
- Tpay card group defined but not offered at checkout.
- Staging admin credentials committed in plain text in `docs/onboarding.md`.

Feeds: [[Website]], [[Production environment]]
