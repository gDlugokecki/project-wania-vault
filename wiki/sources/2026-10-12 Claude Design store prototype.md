---
title: 2026-10-12 Claude Design store prototype
type: source
url: https://claude.ai/design/p/f428c94e-5188-49aa-bf07-3ab24fa7883c
created: 2026-10-12
updated: 2026-10-12
tags: [source, website, brand, design]
---

# 2026-10-12 Claude Design store prototype

## What it is

Claude read [[Greg]]'s Claude Design project "Girly Makeup Store Design" on 2026-10-12: the handoff README, design tokens, example product data and the "Lula Mobile Review" page. The project is the [[Store design prototype]]. The design can still change after this date; this page records what it said then.

Main files in the project:

- `Lula Store.dc.html`: the design of record. All screens, loaders and the full flow.
- `Lula Design Tokens.dc.html`: spec sheet with colours, type, spacing, motion.
- `Lula Mobile Review.dc.html`: the live store shown at 390 px (iPhone 15) and 320 px (iPhone SE), screens: Strona główna, Produkt, Kasa, Logowanie, Rejestracja, Konto.
- `design_handoff_lula_store/`: developer handoff (README, `tokens.css`, Tailwind v3 and v4 configs, `products.example.json`).
- `emails/`: templates for welcome, order confirmation, shipped, ready for pickup, abandoned bag, back in stock, password reset.
- Earlier explorations (three landing layouts, a pixel-art store, glitter, motion and density studies). The handoff calls them superseded.

## What it says

### Placeholders, not facts

The handoff says that the brand name "lula.", the product names, shade names, prices and all product copy are **placeholders pending client input**. All imagery is a placeholder too. Nothing below about products or prices is a decision.

Placeholder content in the design:

- Two palettes, four pans each, one SKU each (no variants): "The Everyday Four" 69 zł and "The After Hours Four" 92 zł.
- Refill pans 24 zł, free shipping over 150 zł, otherwise 14 zł, 30-day returns.
- "Ships in 48h from Kraków", "vegan, fragrance-free, dermatologist-tested", "cream-pressed", "refillable tin the size of a card".

### Look and feel

- "Girly-minimal": warm blush background, plum text, one rose accent, led by photography.
- Font: Instrument Sans (Google Fonts), 400/500/600, no second font. No bold for emphasis.
- Main colours: background `#FAEFEC`, ink `#43222E`, accent `#D9788B` (used once or twice per screen), body text `#7A5C66`, lines `#E7D3CE`.
- Rounded pill buttons, 3–4 px panel corners, tap targets at least 50 px.
- Wordmark is live text, no logo file.

### Screens

1. **Landing:** a full-width founder photo (waist up, palette in hand), headline "Four pans. Every face.", a "shelf" listing both palettes. Signature interaction: drag on the photo to smear pigment on skin.
2. **Product page:** scrolling opens the tin; the four pans are listed as contents, not as a shade picker. Quantity and "Add to bag".
3. **Cart and checkout:** line items plus a checkout panel with email, street, postcode, city.
4. **Confirmation:** "Thank you. It's packed."
5. The mobile review also shows **login, register and account** screens, so the current design has more than the five screens in the handoff.

### Photos needed from us

Campaign hero (founder with palette), and per palette: open top-down, swatch on arm, closed tin, on model, plus a 4:5 shelf thumbnail.

### Notes for building it

- Rebuild in the shop's own stack; don't reuse the prototype's HTML runtime. Ready token files exist (CSS variables, Tailwind).
- Still to do: labels on checkout inputs, reduced-motion versions of the animations, a cart that survives a page reload, mobile Safari height handling.

Feeds: [[Website]], [[Brand]], [[Product]], [[Brand name]], [[Pricing and costs]], [[Store design prototype]]
