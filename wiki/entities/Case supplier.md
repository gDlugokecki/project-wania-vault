---
title: Case supplier
type: entity
kind: company
created: 2026-10-11
updated: 2026-10-29
tags: [company]
---

# Case supplier

## What it is

Supplier of the empty plastic palette case. **Not chosen yet.** The [[Producer]] fills the pans and glues them into the case, so the case goes from the supplier to the producer empty. Spec: see [[Packaging]].

## Greg's contact list (2026-10-19)

The suppliers [[Greg]] picked himself. All 10 got the inquiry email on 2026-10-22 ([[Palette case inquiry email]]) (see [[Packaging]] for the spec). Company names are their Alibaba store names until we have the legal names.

How we track it (changed 2026-10-23, Greg asked for a full history per manufacturer):

- **This page is the overview:** one row per supplier with status, last contact and next step, plus the quote comparison below.
- **Each supplier gets its own page from its first reply** (template: `templates/supplier.md`). The page holds the conversation log (one dated summary per message), what they can provide, decisions about them, and open questions. The supplier's name in the table links to that page.
- **Originals go into `raw/suppliers/<supplier>/`**: forwarded emails, Alibaba chat copies or screenshots, quotes, PDFs. They are never edited after they land.
- The key numbers (MOQ, unit price, mould cost, sample cost, lead time) also go into the comparison below, so suppliers can be compared side by side.

Superseded: until 2026-10-22 a supplier got its own page only once we ordered samples from it, and each reply got its own source page.

Statuses: inquiry sent → replied → quote received → samples ordered → samples received → chosen / rejected.

| # | Supplier | Where | Link | Status | Last contact | Next step |
|---|---|---|---|---|---|---|
| 1 | [[Yihong Plastic]] (hkyihong) | China (Alibaba) | [eyeshadow cases](https://hkyihong.m.en.alibaba.com/productgrouplist-819526332-8/Eyeshadow_Case.html) · [store](https://hkyihong.m.en.alibaba.com/) | replied (MOQ 12,000 per style) | 2026-10-25 Greg asked about MOQ for stock | wait for reply |
| 2 | [[Lihui Plastic]] (lihuiplastic) | China (Alibaba) | [company profile](https://lihuiplastic.en.alibaba.com/company_profile.html) | replied (no stock fit, catalog sent) | 2026-10-25 Greg asked for 9183/9358-like models | wait for reply |
| 3 | [[Omi Plastic]] (ominatural) | China (Alibaba) | [eyeshadow cases](https://ominatural.m.en.alibaba.com/productgrouplist-801504579-4/Eyeshadow_Case.html) | replied (checking stock and 2,000 units) | 2026-10-25 chat | wait; they want style, finish, logo file |
| 4 | [[Nanlong Plastic]] (gdnanlong) | China (Alibaba) | [company profile](https://gdnanlong.en.alibaba.com/company_profile.html) | replied (acknowledged only) | 2026-10-22 will check | wait, nudge ~2026-10-27 |
| 5 | [[Choebe Package]] (cnchoebe) | China (Alibaba) | [store](https://cnchoebe.m.en.alibaba.com/) | replied (asked for an image) | 2026-10-25 Greg sent pictures | wait for reply |
| 6 | [[Stardust Trading]] (stardustcosmetics) | China (Alibaba) | [company profile](https://stardustcosmetics.en.alibaba.com/company_profile.html) | replied (stock palettes, prices) | 2026-10-25 Greg sent pictures | wait for reply |
| 7 | Toly | Malta (EU) | [contact form](https://www.toly.com/en/contact/) | inquiry sent | 2026-10-22 inquiry sent | wait for reply |
| 8 | Picca International | Taichung, Taiwan | [picca.com.tw](https://www.picca.com.tw/) · picca@ms16.hinet.net · +886 4 2389 7607 | inquiry sent (recommended by Irmina) | 2026-10-22 inquiry sent | wait for reply |
| 9 | TimeSource Enterprise | Taiwan | [timesourcetw.com](https://www.timesourcetw.com/) (calls itself an empty case packaging supplier) · contact form · +886 2 2546 8289 | inquiry sent (recommended by Irmina) | 2026-10-22 inquiry sent | wait for reply |
| 10 | Colorich | Zhongshan, China | [colorichpkg.com](https://www.colorichpkg.com/) · admin@colorichpkg.com · MOQ 500; mostly paper palettes, so ask for plastic | inquiry sent (recommended by Irmina) | 2026-10-22 inquiry sent | wait for reply |
| 11 | Sambound New Material Technology Packaging Limited | not recorded | not recorded | inquiry sent (Greg, 2026-10-29); not in Greg's Alibaba inbox as of 2026-10-29, so contact channel unknown | 2026-10-29 inquiry sent | wait for reply |
| 12 | Shantou Chengfeng Trading Co., Ltd. | Shantou, China (Alibaba) | Alibaba chat, contact Ivy Lin | inquiry sent (Greg, 2026-10-29); a reply arrived the same day, not read yet | 2026-10-29 reply waiting | read and log the reply |

Rows 1-6 updated 2026-10-23 and 2026-10-25 from the Alibaba chats (read through Claude in Chrome); each supplier now has its own page. Rows 11-12 added 2026-10-29: Greg contacted them that day. Rows 8-10 added on 2026-10-22, recommended by Irmina (who she is: not recorded yet). Greg's list had hkyihong twice (a product group and the store page); merged into one row.

### Quote comparison

| Supplier | MOQ | Unit price (1k / 2k / 5k) | Mould cost | Sample cost | Lead time | Notes |
|---|---|---|---|---|---|---|
| [[Omi Plastic]] | 10,000 | not yet | stock moulds | not yet | not yet | stock 3025 (9 x Ø28, mirror) closest; 3011/3012 wells too small |
| [[Stardust Trading]] | 1 (stock) | 15.05-23.76 PLN (ABS mirror 12-well, listing range) | stock | not yet | not yet | acrylic 9/12-well from 9.90 PLN, no mirror possible |
| [[Lihui Plastic]] | not yet | not yet | custom mould "high" | not yet | not yet | no stock fit; catalog sent |
| [[Kaiya Cosmetics]] | 12,000 | USD 1.13 | n/a | not yet | not yet | paper palette, not plastic |
| [[Yihong Plastic]] | 12,000 per style | not yet | not yet | not yet | not yet | asked if lower for a stock model |
| [[Walkin Printing]] | not yet | not yet | custom | plain sample 3-5 days | bulk 15-20 working days + 35-45 days DDP | probably paperboard |

### Also answered (not on Greg's list)

Greg also posted an RFQ (request for quotation) on Alibaba; when and with what text is not recorded yet. Two paper-packaging companies quoted on it:

- [[Kaiya Cosmetics]]: paper palettes only, MOQ 12,000, USD 1.13. Checking plastic options.
- [[Packshion Packaging]]: paper boxes; a candidate for the outer box, not for the case.
- [[Walkin Printing]] (2026-10-24): custom magnetic palettes with mirror, 9 or 12 pans, probably paperboard. Sent 14 portfolio photos and a timeline.

## Claude's shortlist (2026-10-19, revised the same day)

[[Greg]] checked the first list and found that none of the European companies offers eyeshadow palette cases as a product. Rechecked: of the European names only Toly shows palettes it actually made, and those are for prestige brands. Most European packaging firms source palettes in Asia (Texen says so itself). So the realistic route at 1,000-5,000 pcs is a factory in China, with Toly as the one European attempt. See [[2026-10-19 Palette case supplier search]].

| # | Company | Where | Evidence | Contact | Status |
|---|---|---|---|---|---|
| 1 | Toly | Malta (EU), HQ and factory in Zejtun | Made eyeshadow palettes for Lancôme (12 shades), Armani, Clarins; stock 12-pan "Upstage" palette with mirror. Prestige clients, MOQ unknown | form: toly.com/en/contact | on Greg's list |
| 2 | Zhejiang Weili Plastic | Jinhua, China | Manufacturer; plastic palettes with mirror and magnetic closure | sales5@zjwlsj.com | not contacted |
| 3 | SN Packs (Sun Nature) | Wuhan, China | Custom magnetic plastic palettes 1-16 pans, palettes with mirror | info@snpacks.com | not contacted |
| 4 | Shantou Tongzhuang Cosmetic | Shantou, China | Magnetic empty palette, 0.53 USD FOB at MOQ 12,000 (listed price) | inquiry form on made-in-china.com | not contacted |

Also worth asking: the [[Producer]] itself, whether it already buys cases that fit its pans.

Dropped on 2026-10-19 (palettes not confirmed on their own sites): Euromakeup / Eurovetrocap, Quadpack, HCP Packaging, Lumson / Marino Belotti, Texen (sources in Asia and North Africa), Faca Packaging (jars only), A Packaging Group (US, MOQ 10,000). Paper palettes (Major Custom Packaging) only if plastic proves too expensive. Colorich is back on Greg's list (row 10).

## Appears in

[[Product]] · [[Packaging]] · [[Pricing and costs]]

Sources: [[2026-10-11 Kickoff Q&A with Greg]], [[2026-10-19 Palette case supplier search]], Alibaba chats in `raw/suppliers/` (2026-10-23)
