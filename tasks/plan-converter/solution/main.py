"""Reference implementation entrypoint for plan-converter."""


def run(context=None):
    """Run the plan-converter workflow."""
    return {"feature": "plan-converter", "status": "ok"}


if __name__ == "__main__":
    print(run())
