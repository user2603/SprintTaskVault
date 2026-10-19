"""Reference implementation entrypoint for field-handler."""


def run(context=None):
    """Run the field-handler workflow."""
    return {"feature": "field-handler", "status": "ok"}


if __name__ == "__main__":
    print(run())
