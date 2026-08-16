# Foundry VTT Copilot

AI powered Assistant for Foundry VTT

## Quick Start

### Prerequisites

- Python 3.12
- `uv` (Python package manager)

### Setup

```bash
# Fill in secrets
cp .env.example .env

# Setup python packages
uv venv && source .venv/bin/activate
uv sync

# Setup pnpm packages
cd ui && pnpm install
```
### Run

```bash
# Start the python agent with AG-UI endpoint
uv run -m app

# Start the UI with AG-UI Adpater
cd ui && pnpm run dev
```

- API: `http://localhost:7777/`
- API Docs: `http://localhost:7777/docs`
- Chat UI: `http://localhost:3000/`

## Development

### Test

```bash
uv run pytest
```

### Format

```bash
uv run ruff format . && uv run ruff check --fix
```

### Observability

```bash
phoenix serve
```

### Update Dependencies

```bash
uv-upx upgrade run
```
