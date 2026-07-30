# FL-07 Build Log — Research Scout MVP

## Platform deviation from FL-06 spec

FL-06 specified Claude Project with a Google Drive connector. During the build,
Google Drive's OAuth setup repeatedly blocked progress, so I pivoted to a
scripted agent instead — one of the platform options explicitly allowed in the
FL-06 brief. This kept the build moving instead of stalling on a connector
setup issue.

- **Search tool:** DuckDuckGo web search (via the `ddgs` Python package)
  instead of Claude's native web search.
- **Storage:** local file save to a `Research_Briefs` folder on the Desktop,
  instead of Google Drive.
- **Model:** Groq's free `llama-3.1-8b-instant` API instead of Claude, to keep
  the build free of cost/credit constraints during iteration.
- Everything else — brief structure, confirm-before-save guardrail, sourced
  findings — matches the FL-06 spec as written.

## What broke, and what I changed

1. **Invalid API key (401 error).** First real run failed with
   `openai.AuthenticationError: Invalid API Key`. The Groq key had been
   copied incorrectly. Regenerated the key on console.groq.com and replaced
   it in the script — fixed.

2. **`duckduckgo_search` package deprecation warning.** The original package
   name was renamed upstream to `ddgs`. Ran `pip install ddgs` and updated
   the import — fixed, warning gone.

3. **Search results weren't reaching the model.** Early version fetched
   search results correctly (visible in the `[TOOL USED] Searching web...`
   log line) but never actually inserted them into the prompt sent to the
   LLM. The agent replied "I don't have any information to work with" even
   though real results existed. Fixed by explicitly building the search
   results into the user message before calling the model.

4. **Filename bug.** Every brief was being saved to the same hardcoded
   `brief_test.txt`, so each run silently overwrote the last one and made it
   look like nothing was saving correctly. Fixed by generating a unique
   filename per topic + timestamp.

5. **Exposed API key.** While debugging in PowerShell, the Groq key was
   accidentally pasted directly into the terminal instead of the script file
   (and briefly appeared on screen). Rotated the key immediately as a
   precaution — not a code bug, but worth logging as a process lesson: API
   keys go in the file, never typed into the terminal.

## What I cut from the spec

- The "weekly recurring scan" behavior (comparing this week's findings to
  last week's) from the FL-06 spec was not built into this MVP. The current
  version only handles one-off topic requests. Cut for time — noted as a
  stretch item for the next checkpoint.

## Final state

End-to-end loop confirmed working: user enters a topic → agent performs a
live DuckDuckGo search → Groq drafts a sourced brief (takeaway, findings,
open questions) → agent asks for confirmation → on "y", saves a uniquely
named file to `Desktop/Research_Briefs/` → prints the saved path.

Verified with the topic "AI brower agents 2026" (typo and all) — search still
returned relevant, current results and the brief was saved successfully.
