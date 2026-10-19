"""Reference implementation entrypoint for hook-previewer."""


def run(context=None):
    """Run the hook-previewer workflow."""
    return {"feature": "hook-previewer", "status": "ok"}


if __name__ == "__main__":
    print(run())
