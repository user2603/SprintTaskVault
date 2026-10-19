"""Reference implementation entrypoint for link-comparator."""


def run(context=None):
    """Run the link-comparator workflow."""
    return {"feature": "link-comparator", "status": "ok"}


if __name__ == "__main__":
    print(run())
