"""Reference implementation entrypoint for canvas-processor."""


def run(context=None):
    """Run the canvas-processor workflow."""
    return {"feature": "canvas-processor", "status": "ok"}


if __name__ == "__main__":
    print(run())
