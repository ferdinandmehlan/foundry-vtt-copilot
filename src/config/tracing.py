from phoenix.otel import register


def enable_local_tracing():
    register(
        project_name="foundry-vtt-copilot",
        auto_instrument=True,
    )
