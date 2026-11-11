"""Reference implementation entrypoint for guide-builder."""


def run(context=None):
    """Run the guide-builder workflow."""
    return {"feature": "guide-builder", "status": "ok"}


if __name__ == "__main__":
    print(run())
