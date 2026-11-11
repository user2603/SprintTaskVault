"""Reference implementation entrypoint for guide-reminder."""


def run(context=None):
    """Run the guide-reminder workflow."""
    return {"feature": "guide-reminder", "status": "ok"}


if __name__ == "__main__":
    print(run())
