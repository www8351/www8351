# Skills and plugins reference

Paste this block into a project's `CLAUDE.md`, or import it with `@claude-skills-reference.md`.
Use a skill only when its trigger matches the task. Never install or update plugins without being asked.

## Writing
* `blader/humanizer`: skill. Removes signs of AI-generated writing. Use when editing or reviewing prose, docs, README text.

## Design and UI quality
* `heydamir/unslop`: skill. Turns vibecoded, AI-looking UI into a designed interface. Use when a finished UI looks generic.
* `pbakaus/impeccable`: design vocabulary for the coding agent. Use for polish, critique and audit passes before shipping UI.
* `Leonxlnx/taste-skill`: skills for art direction, reference images and a browser check. Use when starting a page or judging its look.
* `Nutlope/hallmark`: anti AI slop design skill for Claude Code, Cursor and Codex. Use as a final check on visual output.
* `nextlevelbuilder/ui-ux-pro-max-skill`: UI/UX design intelligence across platforms. Use when planning layout, hierarchy and components.

## Websites
* `nateherkai/scroll-craft`: skill and Claude Code plugin. Premium scroll-driven, immersive sites. Use only for scroll animation heavy pages.

## Unverified
* `Jakubantalik/transitions.dev`: not read yet. Purpose unknown, confirm before relying on it.

## Order of use for UI work
1. Build with `taste-skill` or `ui-ux-pro-max-skill`.
2. Review with `impeccable`.
3. Clean up with `unslop` and `hallmark`.
4. Edit all visible copy with `humanizer`.
