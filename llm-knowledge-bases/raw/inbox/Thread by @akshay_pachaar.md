**Akshay** @akshay\_pachaar [2026-04-14](https://x.com/akshay_pachaar/status/2044000393110474756/history)

MiniMax M2.7 is open-source!

The most interesting part of this release isn't a benchmark number. It's what MiniMax calls "self-evolution," and it's essentially Karpathy's Autoresearch applied at full scale.

Every AI agent today runs inside a harness: the scaffolding of skills, tools, memory, and workflow rules that surrounds it. Normally a human engineer builds this, and the agent operates within it. The harness stays fixed.

M2.7 treats its harness as something it can rewrite.

The agent runs a task, analyzes where things went wrong, plans changes to its own scaffold, applies them, evaluates against a benchmark, and decides whether to keep or revert. It writes self-criticism into memory so the next round starts smarter, then loops again.

MiniMax ran this for 100+ rounds internally. The model discovered optimizations on its own: it systematically searched for optimal sampling parameters, wrote workflow-specific guidelines (like checking for the same bug pattern in other files after a fix), and added loop detection to avoid getting stuck.

They also tested it on 22 ML competitions from OpenAI's MLE Bench Lite, each running 24 hours fully autonomous. With every round, the trained models achieved higher medal rates. The best run earned 9 gold medals.

The weights never changed. What improved was the system around the model: better skills, better memory, better workflow rules. That distinction matters because the improvement loop can run continuously without any retraining.

I'm pretty sure every major AI lab is doing some version of this internally. The fact that MiniMax is publishing it openly is what makes this release worth paying attention to.

huggingface : http://huggingface.co/MiniMaxAI/MiniMax-M2.7…

Blog: https://minimax.io/news/minimax-m27-en…

Note: The model licence is NON-COMMERCIAL LICENSE, that said, there's a lot to learn from this work being available in the open.