"""Reference implementation entrypoint for alert-normalizer."""


def run(context=None):
    """Run the alert-normalizer workflow."""
    return {"feature": "alert-normalizer", "status": "ok"}


if __name__ == "__main__":
    print(run())
