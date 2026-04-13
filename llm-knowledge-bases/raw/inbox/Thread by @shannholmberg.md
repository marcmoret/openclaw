**Shann³** @shannholmberg 2026-04-02

how karpathy builds a personal AI knowledge base with obsidian

most of his token spend is shifting from code to knowledge management

he dumps everything he's researching into one folder. articles, papers, repos, datasets, images

then he points claude at the folder. it reads through every source, writes summaries, groups related ideas, links concepts across documents, and builds a structured wiki in markdown

all viewable in Obsidian. karpathy rarely edits the wiki himself, the LLM maintains it

when he adds something new, it figures out how it connects to whats already there and updates the wiki on its own

his wiki is at ~100 articles and ~400K words. at that scale he queries it like a research engine:

\> "what are the common patterns across these papers"

\> "what connects this new idea to something I saved weeks ago"

\> "summarize everything on topic X and tell me whats missing"

every answer gets filed back into the wiki. so it grows from both what you save and what you ask

he runs "health checks" too. the LLM finds inconsistencies, fills gaps with web searches, and suggests new directions

he skipped RAG and vector databases entirely. the LLM auto-maintains index files and reads related docs on its own at this scale

right now you need Obsidian, CLI tools, custom scripts, and browser extensions to wire it together

"I think there is room here for an incredible new product instead of a hacky collection of scripts"

> 2026-04-02
> 
> LLM Knowledge Bases
> 
> Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating
> 
> ![Image](https://pbs.twimg.com/media/HFAFCBtaQAAOilu?format=png&name=large)