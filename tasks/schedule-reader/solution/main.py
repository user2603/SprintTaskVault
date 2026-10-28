"""Reference implementation entrypoint for schedule-reader."""


def run(context=None):
    """Run the schedule-reader workflow."""
    return {"feature": "schedule-reader", "status": "ok"}


if __name__ == "__main__":
    print(run())
