# Codex Memory & Project Docs

You can give Codex extra instructions and guidance using `AGENTS.md` files. Codex looks for these files in the following order and merges them top-down:

1. `~/.codex/AGENTS.md` — Personal global guidance  
2. `AGENTS.md` at the repo root — Shared project notes  
3. `AGENTS.md` in the current working directory — Sub-folder/feature specifics  

---

## Debugging

Set the environment variable to print full API request and response details:

```sh
DEBUG=true codex
```

---

## Configuration Guide

Codex configuration files can be placed in the `~/.codex/` directory. Both YAML and JSON formats are supported.

### Basic Configuration Parameters

| Parameter            | Type    | Default     | Description                              | Available Options                                  |
|----------------------|---------|-------------|------------------------------------------|----------------------------------------------------|
| `model`              | string  | o4-mini     | AI model to use                          | Any model name supporting OpenAI API               |
| `approvalMode`       | string  | suggest     | AI assistant's permission mode           | `suggest` (suggestions only), `auto-edit`, `full-auto` |
| `fullAutoErrorMode`  | string  | ask-user    | Error handling in full-auto mode         | `ask-user` (prompt for user input), `ignore-and-continue` |
| `notify`             | boolean | true        | Enable desktop notifications             | `true`/`false`                                    |

### Example Usage
```sh
codex --approval-mode full-auto "create the fanciest todo-list app"
```
