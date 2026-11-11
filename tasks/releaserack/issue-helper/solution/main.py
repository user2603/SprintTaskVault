"""Reference implementation entrypoint for issue-helper."""


def run(context=None):
    """Run the issue-helper workflow."""
    return {"feature": "issue-helper", "status": "ok"}


if __name__ == "__main__":
    print(run())
