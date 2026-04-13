# Pretext

- URL: https://github.com/chenglou/pretext
- Date captured: 2026-04-10
- Type: repo

## Content

**Pretext** is a pure JavaScript/TypeScript library for multiline text measurement and layout. It provides fast, accurate text sizing that works across all languages without requiring DOM measurements.

### Key Description

As stated in the repository: "Pure JavaScript/TypeScript library for multiline text measurement & layout. Fast, accurate & supports all the languages you didn't even know about."

### Core Value Proposition

The library eliminates the need for expensive DOM operations like `getBoundingClientRect()` and `offsetHeight`, which trigger layout reflow. Instead, it implements proprietary text measurement logic using the browser's font engine as the source of truth.

### Primary Use Cases

**1. Text Height Measurement Without DOM Touch**

The `prepare()` function performs one-time text analysis and caching, while `layout()` executes pure arithmetic calculations on cached widths to determine paragraph height and line count at a given width and line-height.

**2. Manual Line-by-Line Layout**

Using `prepareWithSegments()`, developers can access lower-level APIs for custom rendering scenarios—particularly useful for canvas, SVG, or variable-width layouts where different lines need different widths.

### Installation

```
npm install @chenglou/pretext
```

### Key Features

- Supports rich international text including Arabic, Chinese, emoji
- Optional `whiteSpace: 'pre-wrap'` for textarea-like behavior
- `wordBreak: 'keep-all'` for CJK text handling
- Shrink-wrap capabilities for finding tightest container widths
- Zero layout reflow triggering
- Extensive API for various layout scenarios

### API Highlights

Core functions include `prepare()`, `layout()`, `prepareWithSegments()`, `layoutWithLines()`, `walkLineRanges()`, and `layoutNextLineRange()` for progressive, cursor-based layouts.

### Repository Stats

- 42.8k stars
- 2.3k forks
- 355 commits
- Active development with demos available
