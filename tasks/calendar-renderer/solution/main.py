"""Reference implementation entrypoint for calendar-renderer."""


def run(context=None):
    """Run the calendar-renderer workflow."""
    return {"feature": "calendar-renderer", "status": "ok"}


if __name__ == "__main__":
    print(run())
