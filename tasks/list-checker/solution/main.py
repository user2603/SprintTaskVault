"""Reference implementation entrypoint for list-checker."""


def run(context=None):
    """Run the list-checker workflow."""
    return {"feature": "list-checker", "status": "ok"}


if __name__ == "__main__":
    print(run())
