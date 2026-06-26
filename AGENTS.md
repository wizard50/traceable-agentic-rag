# AGENTS.md

## Project Overview
- **Name**: traceable-agentic-rag
- **Goal**: Build a production-minded Agentic RAG system with strong observability and evaluation.
- **Core Focus**: Agentic behavior (query rewriting + multi-step reasoning), full tracing (Phoenix), and automated evaluation (retrieval + faithfulness).

## Tech Stack & Key Decisions
- **Orchestration**: LangGraph (primary)
- **Observability**: Arize Phoenix (preferred)
- **Vector Store**: Chroma (for now)
- **LLM**: OpenAI (via LiteLLM if needed later)
- **Frontend**: Streamlit (fast iteration)
- **Data Models**: Pydantic v2 (mandatory for all structured data)
- **Python version**: 3.13+

## Architecture Principles
- Clean separation of concerns (ingestion / retrieval / agent / observability / evaluation)
- Prefer composition over inheritance
- All LLM inputs/outputs should use Pydantic models when possible
- Tracing should be added early and be visible in Phoenix
- Keep the agent logic testable and observable

## Coding Standards
- Use type hints everywhere
- Prefer `pydantic` models over raw dicts for structured data
- Write clear, self-documenting code
- Add docstrings for public functions and classes
- Keep functions relatively small and focused
- Use `ruff` for linting and formatting

## How to Work With Me
- Always read `AGENTS.md` before starting a task
- Ask clarifying questions if requirements are ambiguous
- Propose small, incremental changes when possible
- Show the diff or key changes after implementing something
- Prioritize clean architecture and observability over quick hacks
