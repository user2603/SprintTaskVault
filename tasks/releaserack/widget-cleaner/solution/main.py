"""Reference implementation entrypoint for widget-cleaner."""


def run(context=None):
    """Run the widget-cleaner workflow."""
    return {"feature": "widget-cleaner", "status": "ok"}


if __name__ == "__main__":
    print(run())
