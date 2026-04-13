![Image](https://pbs.twimg.com/media/HEzwYeqXsAEm1bb?format=jpg&name=large)

In this article, I’ve curated 20 powerful agentic skills you can add to any AI model to boost your productivity.

Each skill is written in .md format, which is the standard for Claude. You can still copy the documents and paste them into ChatGPT or Gemini whenever you need to use the skill.

I’ve group the skills into 5 categories and also attached a video guide showing how to easily add these skills to your Claude agent.

<video preload="none" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/amplify_video_thumb/2039261607931580416/img/npmNaZu__VpPJHEU.jpg" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"><source type="video/mp4" src="blob:https://x.com/d85f56de-fb59-439d-abbe-acbed01df9d9"></video>

0:03 / 1:35

1:32

## Writing & Content Skills

- **SCQA Writing Framework:**

SCQA is a **framework for structuring communication**, especially for writing or presentations. It stands for:

- **S = Situation** → Set the context. Explain the current state or background so the audience understands the starting point.
- **C = Complication** → Introduce a problem, tension, or challenge that disrupts the situation. This is what makes the story or argument interesting.
- **Q = Question** → Pose the key question that naturally arises from the complication. What does the audience want answered?
- **A = Answer** → Provide the solution, insight, or recommendation. This resolves the question logically.

Think of it as **storytelling with logic**. It’s widely used in consulting, business writing, and content creation because it makes complex ideas easy to follow.

```text
name: scqa-writing-framework
description: Structures content using the Situation, Complication, Question, Answer framework for clear, logical, and engaging narratives suitable for threads, articles, and reports.
license: Complete terms in LICENSE.txt
---

# SCQA Writing Framework

## Overview

Transforms unstructured ideas into structured, high-engagement content. It’s perfect for educational material, storytelling, and technical explanations.

**Keywords**: writing, storytelling, SCQA, structured content, clarity, narrative, article, thread

## Core Framework

### Situation
- Establish context, current state
- Concise, clear, relevant

### Complication
- Introduce problem or tension
- Create curiosity

### Question
- Frame audience’s key question
- Essential and natural

### Answer
- Deliver insight or solution
- Clear, actionable

## Features

- Logical progression
- Readability optimized
- Curiosity-driven engagement

## Output Format

- SCQA blocks, short paragraphs, bullet highlights

## Instructions

- Break input into SCQA sections
- Keep sentences concise
- Avoid unnecessary jargon
- Maintain smooth flow

## Constraints

- No skipped sections
- No repetition
- Conciseness prioritized
```

- **Content Repurposing Engine**

```text
name: content-repurposing-engine
description: Converts long-form content into multiple formats like social media threads, short video scripts, or summaries while preserving the core message.
license: Complete terms in LICENSE.txt
---

# Content Repurposing Engine

## Overview

Transforms blogs, notes, and articles into varied formats for different channels.

**Keywords**: content, repurposing, social media, threads, scripts, short-form, long-form

## Features

- Extracts key ideas
- Adapts for platforms
- Maintains tone and clarity

## Output Format

- Platform-specific content
- Structured sections
- Engaging headlines/hooks

## Instructions

- Analyze original content
- Identify key points
- Rewrite in target format
- Keep consistent tone and readability

## Constraints

- Preserve meaning
- Avoid verbosity
- Format must match channel style
```

- **Tone & Style Enforcer**

```text
name: tone-style-enforcer
description: Ensures all outputs match a consistent brand or personal tone, maintaining clarity, style, and audience alignment across multiple outputs.
license: Complete terms in LICENSE.txt
---

# Tone & Style Enforcer

## Overview

Keeps all generated content in line with defined style guidelines or brand voice.

**Keywords**: style, tone, brand voice, consistency, clarity, writing

## Features

- Tone preservation
- Consistency across outputs
- Formatting enforcement

## Output Format

- Text aligned with style guide
- Optional bullet structure
- Clean, professional

## Instructions

- Apply defined tone to all input
- Check for style inconsistencies
- Adjust language, structure, and formatting

## Constraints

- No deviation from selected tone
- Maintain clarity
```

- **Long-Form to Summary Compressor**

```text
name: long-form-summary-compressor
description: Condenses long text into concise summaries, keeping essential ideas intact for quick consumption and understanding.
license: Complete terms in LICENSE.txt
---

# Long-Form to Summary Compressor

## Overview

Reduces complex content into digestible summaries for easy reading.

**Keywords**: summarization, long-form, clarity, conciseness, insights

## Features

- Key point extraction
- Bullet or paragraph output
- Simplifies dense material

## Output Format

- Concise paragraph
- Optional bullet points

## Instructions

- Identify main points
- Remove redundancy
- Produce readable, actionable summary

## Constraints

- No missing critical info
- No filler
```

- **Structured Copywriting Skill**

```text
name: structured-copywriting-skill
description: Generates high-impact copy with clear hooks, structured flow, and concise messaging for marketing, articles, and social media content.
license: Complete terms in LICENSE.txt
---

# Structured Copywriting Skill

## Overview

Produces persuasive, well-structured copy with strong hooks and calls to action.

**Keywords**: copywriting, marketing, social media, structured content, hooks, engagement

## Features

- Strong hooks
- Sectioned flow
- CTA inclusion
- Concise and readable

## Output Format

- Sections, bullet points, hooks, conclusion

## Instructions

- Craft attention-grabbing opening
- Organize main points clearly
- Include actionable CTA
- Avoid unnecessary filler

## Constraints

- Maintain readability
- Do not overcomplicate
```

## Visual & Infographic Skills

- **Excalidraw Diagram Generator**

```text
name: excalidraw-diagram-generator
description: Converts textual concepts or workflows into clear diagram instructions suitable for Excalidraw or other visual tools.
license: Complete terms in LICENSE.txt
---

# Excalidraw Diagram Generator

## Overview

Transforms ideas into diagram structures for visualization, learning, and planning.

**Keywords**: diagrams, visualization, excalidraw, workflows, mapping

## Features

- Node and connector generation
- Logical hierarchy
- Clear labels

## Output Format

- Diagram title
- Nodes and connections
- Layout suggestion

## Instructions

- Identify main elements
- Create nodes
- Connect logically
- Suggest layout

## Constraints

- Avoid clutter
- Maintain clarity
```

- **Infographic Builder**

```text
name: infographic-builder
description: Turns textual content into structured infographic formats suitable for reports, presentations, and educational materials.
license: Complete terms in LICENSE.txt
---

# Infographic Builder

## Overview

Generates visual-friendly summaries from text, highlighting steps, processes, or data points.

**Keywords**: infographic, visual, summary, chart, design

## Features

- Sectioned breakdown
- Bullet or step representation
- Readable visual format

## Output Format

- Steps, headings, visual cues
- Optional icons or markers

## Instructions

- Extract key points
- Organize visually
- Apply concise formatting

## Constraints

- Avoid excessive text
- Maintain clarity
```

- **Flowchart Decision Builder**

```text
name: flowchart-decision-builder
description: Generates decision trees and flowcharts from textual input to simplify complex decision-making processes.
license: Complete terms in LICENSE.txt
---

# Flowchart Decision Builder

## Overview

Converts processes into stepwise flowcharts for clear decision-making.

**Keywords**: flowchart, decision tree, process, visualization, clarity

## Features

- Node-based structure
- Conditional branching
- Clear labeling

## Output Format

- Nodes
- Connections
- Layout guidance

## Instructions

- Identify steps and decisions
- Map conditional paths
- Maintain logical flow

## Constraints

- Keep diagrams simple
- Avoid unnecessary nodes
```

- **UI/UX Layout Advisor**

```text
name: ui-ux-layout-advisor
description: Advises on interface layouts to optimize clarity, spacing, hierarchy, and usability.
license: Complete terms in LICENSE.txt
---

# UI/UX Layout Advisor

## Overview

Provides structured suggestions for designing clean and usable interfaces.

**Keywords**: ui, ux, layout, design, hierarchy, clarity

## Features

- Spacing and alignment suggestions
- Hierarchy optimization
- Accessibility considerations

## Output Format

- Layout instructions
- Element positioning
- Optional visual hints

## Instructions

- Analyze input design
- Suggest optimal layout
- Maintain readability and hierarchy

## Constraints

- Do not overcrowd layout
- Prioritize clarity
```

## Research & Analysis Skills

- **Deep Research Synthesizer**

```text
name: deep-research-synthesizer
description: Synthesizes insights from large datasets, filters irrelevant data, identifies patterns, and produces actionable summaries.
license: Complete terms in LICENSE.txt
---

# Deep Research Synthesizer

## Overview

Converts large amounts of text into structured insights and actionable takeaways.

**Keywords**: research, synthesis, insights, analysis, knowledge

## Features

- Filters low-value info
- Highlights patterns
- Creates structured output

## Output Format

- Key insights
- Supporting details
- Summary paragraph

## Instructions

- Identify key points
- Remove irrelevant content
- Organize logically

## Constraints

- Avoid generic summaries
- Focus on utility
```

- **Onchain Transaction Analyzer**

```text
name: onchain-transaction-analyzer
description: Analyzes blockchain transactions by tracing wallets, contracts, and token movements and providing simple, understandable explanations.
license: Complete terms in LICENSE.txt
---

# Onchain Transaction Analyzer

## Overview

Decodes onchain data into human-readable explanations.

**Keywords**: blockchain, crypto, analysis, transactions, wallets

## Features

- Wallet tracking
- Contract mapping
- Token flow visualization
- Simple language

## Output Format

- Step-by-step explanation
- Key actors and actions
- Summary insights

## Instructions

- Trace wallet and token flows
- Identify key interactions
- Summarize in plain language

## Constraints

- Avoid jargon
- Focus on clarity
```

- **Source Validation Skill**

```text
name: source-validation-skill
description: Validates the credibility of information sources, highlighting reliability, relevance, and potential biases.
license: Complete terms in LICENSE.txt
---

# Source Validation Skill

## Overview

Filters information for trustworthiness and relevance.

**Keywords**: credibility, validation, sources, research, bias

## Features

- Reliability scoring
- Bias detection
- Relevance filtering

## Output Format

- Verified sources
- Key insights
- Notes on reliability

## Instructions

- Check references
- Evaluate author and date
- Highlight trustworthy content

## Constraints

- Avoid unverified info
- Prioritize high-quality sources
```

- **Competitive Intelligence Skill**

```text
name: competitive-intelligence-skill
description: Compares products, protocols, or tools to provide structured analysis of strengths, weaknesses, and opportunities.
license: Complete terms in LICENSE.txt
---

# Competitive Intelligence Skill

## Overview

Delivers comparative insights for business, tech, or market research.

**Keywords**: analysis, competitive, research, comparison, strategy

## Features

- Feature comparison
- SWOT-style analysis
- Recommendations

## Output Format

- Bullet comparison
- Strengths/weaknesses
- Key takeaways

## Instructions

- Identify competitors/tools
- Compare features
- Highlight differences and risks

## Constraints

- Avoid bias
- Focus on actionable insights
```

- **Knowledge Structuring Skill**

```text
name: knowledge-structuring-skill
description: Organizes unstructured information into clear frameworks, bullet points, or structured notes for easier understanding and application.
license: Complete terms in LICENSE.txt
---

# Knowledge Structuring Skill

## Overview

Transforms messy input into structured, usable knowledge.

**Keywords**: knowledge, structuring, frameworks, organization, notes

## Features

- Categorizes ideas
- Creates logical hierarchy
- Bullet formatting

## Output Format

- Structured framework
- Key points
- Optional notes

## Instructions

- Identify major topics
- Group related ideas
- Present clearly and concisely

## Constraints

- Avoid ambiguity
- Maintain readability
```

- **Video Script Generator**

```text
name: video-script-generator
description: Generates video scripts with hooks, structured sections, pacing, and call-to-actions optimized for engagement and retention.
license: Complete terms in LICENSE.txt
---

# Video Script Generator

## Overview

Produces structured scripts for short and long-form video content.

**Keywords**: video, scripts, hooks, engagement, pacing, content

## Features

- Strong opening hooks
- Sectioned content
- Clear calls-to-action

## Output Format

- Hook
- Content sections
- Closing summary

## Instructions

- Start with hook
- Organize main points
- Maintain pacing
- Include CTA

## Constraints

- Avoid filler
- Maintain audience attention
```

- **Video Editing Planner**

```text
name: video-editing-planner
description: Suggests editing structure, scene cuts, transitions, and pacing for improved video content quality and engagement.
license: Complete terms in LICENSE.txt
---

# Video Editing Planner

## Overview

Assists in planning efficient, engaging edits.

**Keywords**: video, editing, pacing, transitions, scenes

## Features

- Scene breakdown
- Transition suggestions
- Pacing optimization

## Output Format

- Editing steps
- Scene notes
- Transition plan

## Instructions

- Identify key scenes
- Suggest cuts/transitions
- Optimize for engagement

## Constraints

- Avoid excessive edits
- Preserve story clarity
```

- **Hook Generator**

```text
name: hook-generator
description: Produces attention-grabbing hooks for videos, social posts, and content intros to maximize engagement.
license: Complete terms in LICENSE.txt
---

# Hook Generator

## Overview

Creates compelling openings to capture attention immediately.

**Keywords**: hook, attention, engagement, intro, viral

## Features

- Short, impactful
- Curiosity-driven
- Adaptable to content type

## Output Format

- Hook sentence
- Optional follow-up intro

## Instructions

- Focus on curiosity or bold statements
- Keep concise
- Match audience interest

## Constraints

- Avoid generic hooks
- Maintain relevance
```

- **Caption & Subtitle Formatter**

```text
name: caption-subtitle-formatter
description: Formats captions and subtitles for readability, timing, and accessibility across videos.
license: Complete terms in LICENSE.txt
---

# Caption & Subtitle Formatter

## Overview

Ensures captions are readable, timed correctly, and maintain visual clarity.

**Keywords**: caption, subtitle, accessibility, readability, video

## Features

- Line breaks for clarity
- Timing alignment
- Readability optimization

## Output Format

- Caption text blocks
- Timing cues

## Instructions

- Format each line for clarity
- Match timing to speech
- Maintain readability standards

## Constraints

- Avoid long lines
- Keep clear and concise
```

## Coding & Automation Skills

- **Code Review Skill**

```text
name: code-review-skill
description: Reviews code for bugs, inefficiencies, and adherence to best practices, providing actionable improvement suggestions.
license: Complete terms in LICENSE.txt
---

# Code Review Skill

## Overview

Analyzes code to ensure quality, efficiency, and maintainability.

**Keywords**: code, review, bugs, optimization, best practices

## Features

- Error detection
- Optimization recommendations
- Style enforcement

## Output Format

- Issues found
- Suggested fixes
- Optional summary

## Instructions

- Analyze code line by line
- Highlight errors or inefficiencies
- Suggest improvements

## Constraints

- Maintain accuracy
- Avoid false positives
```

- **Workflow Automation Agent**

```text
name: workflow-automation-agent
description: Breaks complex tasks into step-by-step workflows, mapping actions to tools, optimizing execution, and improving efficiency.
license: Complete terms in LICENSE.txt
---

# Workflow Automation Agent

## Overview

Converts goals into actionable workflows for AI-assisted or human execution.

**Keywords**: automation, workflow, productivity, steps, execution

## Features

- Task decomposition
- Tool mapping
- Optimization

## Output Format

- Goal
- Stepwise actions
- Tools & instructions

## Instructions

- Identify goal
- Break into steps
- Assign tools
- Optimize for efficiency

## Constraints

- Avoid vague instructions
- Maintain logical flow
```

- **Skill Creator (Meta Skill)**

```text
name: skill-creator-meta-skill
description: Generates new AI skills in \`.md\` format, providing structured name, description, and instruction for future use.
license: Complete terms in LICENSE.txt
---

# Skill Creator (Meta Skill)

## Overview

Automates creation of AI skills by generating fully structured \`.md\` files.

**Keywords**: skill creation, automation, AI, md, modular

## Features

- Generates skill metadata
- Includes detailed instructions
- Ready-to-use format

## Output Format

- Skill name
- Description
- Instruction steps

## Instructions

- Accept input goal
- Define role, task, process
- Output structured \`.md\` skill

## Constraints

- Maintain clarity
- Ensure usability
```

- **DevOps Assistant**

```text
name: devops-assistant
description: Assists in version control, deployment, and automation tasks, ensuring smooth DevOps operations and workflow efficiency.
license: Complete terms in LICENSE.txt
---

# DevOps Assistant

## Overview

Supports development workflows by managing versioning, deployment, and automation tasks.

**Keywords**: devops, automation, deployment, git, workflow

## Features

- Commit and version guidance
- Deployment suggestions
- Workflow optimization

## Output Format

- Task instructions
- Stepwise guide
- Automation recommendations

## Instructions

- Analyze project requirements
- Suggest DevOps actions
- Optimize workflow efficiency

## Constraints

- Ensure accuracy
- Avoid redundant steps
```

**Thanks for your attention on this matter!!!**