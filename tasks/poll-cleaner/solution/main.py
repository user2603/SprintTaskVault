"""Reference implementation entrypoint for poll-cleaner."""


def run(context=None):
    """Run the poll-cleaner workflow."""
    return {"feature": "poll-cleaner", "status": "ok"}


if __name__ == "__main__":
    print(run())
