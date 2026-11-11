"""Reference implementation entrypoint for screen-previewer."""


def run(context=None):
    """Run the screen-previewer workflow."""
    return {"feature": "screen-previewer", "status": "ok"}


if __name__ == "__main__":
    print(run())
