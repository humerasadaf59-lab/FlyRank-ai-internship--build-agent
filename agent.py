from openai import OpenAI
from ddgs import DDGS
from datetime import datetime
import os

# GROQ FREE API
# For security, the real key is not stored in this file.
# Set it as an environment variable before running:
#   Windows (PowerShell):  $env:GROQ_API_KEY = "your_real_key_here"
#   Then run:               python agent.py
import os

api_key = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

SAVE_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop", "Research_Briefs")

SYSTEM_PROMPT = """You are a Research Scout. You will be given a topic and a set
of raw web search results. Turn them into a concise, sourced brief.

Structure your reply as:
1. A 1-2 sentence takeaway, up front.
2. 3-6 key findings, each naming which numbered source it came from.
3. 1-2 open questions or gaps.

Rules:
- Only use information present in the search results given to you below.
- If the results disagree with each other, say so explicitly.
- If the results are thin or irrelevant, say so plainly instead of padding.
- Keep it under 400 words.
"""

print("=" * 55)
print("FL-07 RESEARCH SCOUT MVP - WITH REAL SEARCH")
print("=" * 55)


def web_search(topic, max_results=5):
    print(f"[TOOL USED] Searching web for '{topic}'...")
    with DDGS() as ddgs:
        results = list(ddgs.text(topic, max_results=max_results))
    if not results:
        return None
    formatted = ""
    for i, r in enumerate(results, 1):
        formatted += f"[{i}] {r.get('title','')}\n{r.get('body','')}\nSource: {r.get('href','')}\n\n"
    return formatted


def make_brief(topic, search_results):
    user_message = (
        f"Topic: {topic}\n\n"
        f"Search results:\n{search_results}\n\n"
        f"Write the brief now, using only the search results above."
    )
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content


def save_brief(topic, brief_text):
    os.makedirs(SAVE_FOLDER, exist_ok=True)
    safe_topic = "".join(c if c.isalnum() or c in " -_" else "_" for c in topic)[:40]
    filename = f"Brief - {safe_topic} - {datetime.now().strftime('%Y-%m-%d %H%M%S')}.txt"
    path = os.path.join(SAVE_FOLDER, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(brief_text)
    return path


while True:
    topic = input("\nYou [Enter topic or 'exit']: ")
    if topic.lower() == "exit":
        break
    if not topic.strip():
        print("Please enter a real topic.")
        continue

    print(f"\n[PERCEPTION] Topic received: {topic}")

    results = web_search(topic)
    if not results:
        print("[TOOL RESULT] No search results found. Try a different topic.")
        continue

    print("[ACTION] Drafting brief from real search results...")
    brief = make_brief(topic, results)

    print("\n[RESEARCH BRIEF]")
    print(brief)

    confirm = input("\nSave this brief? [y/N] ")
    if confirm.strip().lower() == "y":
        saved_path = save_brief(topic, brief)
        print(f"[TOOL USED] Saved to: {saved_path}")
    else:
        print("Not saved.")