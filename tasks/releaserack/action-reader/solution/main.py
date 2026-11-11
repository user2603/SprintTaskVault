"""Reference implementation entrypoint for action-reader."""


def run(context=None):
    """Run the action-reader workflow."""
    return {"feature": "action-reader", "status": "ok"}


if __name__ == "__main__":
    print(run())
