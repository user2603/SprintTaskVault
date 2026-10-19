"""Reference implementation entrypoint for survey-comparator."""


def run(context=None):
    """Run the survey-comparator workflow."""
    return {"feature": "survey-comparator", "status": "ok"}


if __name__ == "__main__":
    print(run())
