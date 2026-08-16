# Foundry VTT Copilot UI

Simple chat interface for the Foundry VTT Copilot agent, built with Next.js and CopilotKit.

## Prerequisites

- Node.js 20+
- pnpm
- The CopilotKit backend running on `http://localhost:8000` (see project root)

## Setup

```bash
pnpm install
cp .env.example .env
```

Edit `.env` if your backend runs on a different URL.

## Development

```bash
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) to chat with your agent.

## Architecture

```
Browser → CopilotChat → /api/copilotkit → CopilotRuntime → HttpAgent → http://localhost:8000/agui
```

The Next.js API route acts as a bridge between the CopilotKit frontend protocol and the AG-UI protocol used by the Agno agent backend.
