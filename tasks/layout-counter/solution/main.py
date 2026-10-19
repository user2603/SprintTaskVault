"""Reference implementation entrypoint for layout-counter."""


def run(context=None):
    """Run the layout-counter workflow."""
    return {"feature": "layout-counter", "status": "ok"}


if __name__ == "__main__":
    print(run())
