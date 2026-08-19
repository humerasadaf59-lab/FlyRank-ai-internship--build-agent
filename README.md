## Research Scout Agent — Live Demo & Documentation

### What it does:
Research Scout is an AI-powered web research agent that takes any topic, 
searches the web, and generates a sourced research brief in ~15 seconds.

### Demo Video:
[Watch the live demo](https://youtu.be/_BExQm-F7t8?si=SOct0XNbilHaZxkQ)

In the video I show:
- Running the agent with topic: "AI trends in 2026"
- Live web search results being analyzed
- Claude generating a structured research brief with citations
- One design decision: Why Claude + web search tool vs. custom scraper
- One limitation: Limited to first 10 search results

### Key Deliverables:
- **README**: Full setup, usage examples, architecture, eval results
- **Demo**: 3-min live run with narration explaining design & limitations
- **Repository**: [FlyRank-ai-internship--build-agent](https://github.com/humerasadaf59-lab/FlyRank-ai-internship--build-agent)

### How it was built:
Used Claude API's tool-use capability to:
1. Design research prompts (Claude designed the system prompt)
2. Execute web searches with real-time results
3. Generate structured briefs with citations
4. Iterate and debug the agent workflow

**Transparency**: "Built with Claude API's web search tool. Claude was used to design research prompts and debug the agent workflow."

### GitHub Repository:
- Complete README with setup instructions
- agent.py source code
- Example research brief output
