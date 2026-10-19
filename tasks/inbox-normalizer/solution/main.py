"""Reference implementation entrypoint for inbox-normalizer."""


def run(context=None):
    """Run the inbox-normalizer workflow."""
    return {"feature": "inbox-normalizer", "status": "ok"}


if __name__ == "__main__":
    print(run())
