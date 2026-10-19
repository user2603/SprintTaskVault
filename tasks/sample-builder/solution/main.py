"""Reference implementation entrypoint for sample-builder."""


def run(context=None):
    """Run the sample-builder workflow."""
    return {"feature": "sample-builder", "status": "ok"}


if __name__ == "__main__":
    print(run())
