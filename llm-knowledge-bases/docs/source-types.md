# Source Types

## Social / X sources

Treat social posts as first-class sources, but usually not the final authority on a topic.

### Why keep them separately

A post can contribute:
- discovery
- framing
- author interpretation
- claims worth verifying
- attached images or screenshots

But the linked article, paper, repo, or dataset is often the primary artifact.

### Recommended pattern

For a post with a link:
- store the post in `raw/x/`
- store the linked artifact in the appropriate raw folder
- connect both during compilation

### Suggested classification

Every social source should be classified as one or more of:
- lead / pointer
- commentary
- primary evidence
- speculation

### Practical rule

If a social post links elsewhere, do not collapse both into one source. Keep them separate and relate them in the wiki.
