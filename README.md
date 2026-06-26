# Traceable Agentic RAG

Rust Book Documentation Assistant with Agentic RAG, tracing, and evaluation.

Source material: [The Rust Programming Language](https://github.com/rust-lang/book) (`src/` folder, cloned to `data/download/`).

## Setup

```bash
uv sync --dev
pre-commit install
```

## Development

```bash
uv run pytest
uv run ruff check .
uv run ty check
```

See [AGENTS.md](AGENTS.md) for architecture and implementation guidance.

## License

MIT — see [LICENSE](LICENSE).
