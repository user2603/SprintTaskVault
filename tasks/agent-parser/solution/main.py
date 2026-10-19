"""Reference implementation entrypoint for agent-parser."""


def run(context=None):
    """Run the agent-parser workflow."""
    return {"feature": "agent-parser", "status": "ok"}


if __name__ == "__main__":
    print(run())
