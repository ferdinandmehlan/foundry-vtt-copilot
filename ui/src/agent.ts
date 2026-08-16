import { HttpAgent } from "@ag-ui/client";

export function createDefaultAgent(): HttpAgent {
  return new HttpAgent({
    url:
      (process.env.AGENT_URL || "http://localhost:8000").replace(/\/$/, "") +
      "/agui",
  });
}
