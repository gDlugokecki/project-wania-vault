# Projekt Wania vault

This vault is the second brain of Projekt Wania: Greg and his wife launching their own eyeshadow palette, sold through their own webshop in Poland. Claude maintains it. The owners drop material into `raw/` and ask questions; everything outside `raw/` is Claude's to write and keep correct.

Structure follows [second-brain-os](https://github.com/undefined-ui/second-brain-os), adapted for a company: the **domains** are the "what we are doing" layer, the **wiki** is the "what we know" layer.

## Where the vault lives

The GitHub repo `gDlugokecki/project-wania-vault` is the single source of truth. The owners open it in Obsidian and pull with the Obsidian Git plugin. Claude threads clone it, edit, commit and push to `main`. Pull before editing, keep commits small, one commit per change with a clear message.

## Folders

```
Home.md          start page: domains, decisions, open questions
domains/         one living doc per domain: current state, decisions, open questions, next steps
wiki/
  entities/      people, companies, services, systems (Producer, Tpay, bvt-ecommerce ...)
  concepts/      topics that cut across domains (Compliance and CPNP, Pricing, Legal pages ...)
  decisions/     one page per important decision, dated
  sources/       one page per thing we learned from (a conversation, a repo review, an email, a quote)
raw/             original material: emails, PDFs, quotes, chat exports. Never edited after it lands.
                 Exception: `raw/suppliers/<supplier>/drafts/` holds Claude's draft replies, editable until sent.
templates/       page templates
output/          things generated for use outside the vault (the graph page)
log.md           one line per change, newest at the bottom
```

## Page contract

Every page starts with frontmatter: `title`, `type` (domain | entity | concept | decision | source), `created`, `updated`, `tags`. Entities also have `kind` (person | company | service | system).

## Rules

1. **Nothing lands unlinked.** Link the first mention of every entity, concept, decision or domain with a `[[wikilink]]`. If the page does not exist, create it in the same change or list it under Gaps in `Home.md`.
2. **Never invent facts.** Unknown is written as an open question. Every fact traces to a source page.
3. **Record, don't overwrite.** When something changes (a price, a decision), keep the old value with its date and mark it superseded.
4. **Domains hold state, the wiki holds knowledge.** A domain says where things stand and what is next. An entity or concept page says what it is and links to every domain and source that touches it.
5. **Ingest from raw/.** For a new file in `raw/`: write a source page, update the affected entities, concepts and domains, add links, append to `log.md`.
6. **Log every change** in `log.md`: `YYYY-MM-DD action what -> pages touched`.
7. **Rebuild the graph page** after changes: see `.tools/README.md`.

## Voice

Plain sentences, written for the owners in six months. Use the same name for the same thing everywhere.
