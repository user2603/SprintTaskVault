"""Reference implementation entrypoint for history-reader."""


def run(context=None):
    """Run the history-reader workflow."""
    return {"feature": "history-reader", "status": "ok"}


if __name__ == "__main__":
    print(run())
