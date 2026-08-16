from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI

from agent import build_team
from database import build_db

# enable_local_tracing()

team = build_team()
agent_os = AgentOS(
    teams=[team],
    interfaces=[AGUI(team=team)],
    db=build_db(),
    tracing=True,
    telemetry=True,
)
app = agent_os.get_app()


if __name__ == "__main__":
    agent_os.serve(app="app:app", reload=True)
