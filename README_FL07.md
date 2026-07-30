# FL-07 — Build the Agent (Checkpoint 1 MVP)

**Type:** Assignment · **Track:** General AI Fluency · **Phase:** Build (core)

## What's here

- [`agent.py`](./agent.py) — the working prototype. A Research Scout that
  searches the web live, drafts a sourced brief, and saves it to a local
  folder after confirmation.
- [`build_log.md`](./build_log.md) — real build log: platform deviation from
  the FL-06 spec, every bug hit along the way, and what was cut for time.
- [`fl07_submission_note.txt`](./fl07_submission_note.txt) — the submission
  note as posted to the internship platform.
- Raw run capture (screen recording of a full successful end-to-end run):
  **[link to video — add your Google Drive link here]**

## How it works

1. User enters a topic
2. Agent runs a live DuckDuckGo web search
3. Groq's `llama-3.1-8b-instant` drafts a structured brief (takeaway, sourced
   findings, open questions)
4. Agent asks for confirmation before saving
5. On confirmation, saves a uniquely named file to a local `Research_Briefs`
   folder and reports the saved path

## Running it locally

```bash
pip install openai ddgs
```

Set your Groq API key as an environment variable (never hardcode it in the file):

```powershell
$env:GROQ_API_KEY = "your_key_here"      # PowerShell
```
```bash
export GROQ_API_KEY="your_key_here"      # macOS/Linux
```

Then run:

```bash
python agent.py
```

## Deviation from the FL-06 spec

FL-06 specified Claude Project + Google Drive. Google Drive's OAuth setup
blocked progress during the build, so this MVP uses a scripted agent instead
(DuckDuckGo search + local file save + Groq's free API) — one of the
platform options the FL-06 brief explicitly allows. Full reasoning and every
bug fixed along the way is in [`build_log.md`](./build_log.md).

See [`/FL-06`](../FL-06) for the original design spec.
