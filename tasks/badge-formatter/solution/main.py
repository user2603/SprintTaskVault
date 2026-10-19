"""Reference implementation entrypoint for badge-formatter."""


def run(context=None):
    """Run the badge-formatter workflow."""
    return {"feature": "badge-formatter", "status": "ok"}


if __name__ == "__main__":
    print(run())
