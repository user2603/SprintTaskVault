"""Reference implementation entrypoint for list-renderer."""


def run(context=None):
    """Run the list-renderer workflow."""
    return {"feature": "list-renderer", "status": "ok"}


if __name__ == "__main__":
    print(run())
