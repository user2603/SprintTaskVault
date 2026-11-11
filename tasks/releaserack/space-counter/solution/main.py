"""Reference implementation entrypoint for space-counter."""


def run(context=None):
    """Run the space-counter workflow."""
    return {"feature": "space-counter", "status": "ok"}


if __name__ == "__main__":
    print(run())
