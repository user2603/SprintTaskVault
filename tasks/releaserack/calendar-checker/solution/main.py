"""Reference implementation entrypoint for calendar-checker."""


def run(context=None):
    """Run the calendar-checker workflow."""
    return {"feature": "calendar-checker", "status": "ok"}


if __name__ == "__main__":
    print(run())
