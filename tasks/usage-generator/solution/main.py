"""Reference implementation entrypoint for usage-generator."""


def run(context=None):
    """Run the usage-generator workflow."""
    return {"feature": "usage-generator", "status": "ok"}


if __name__ == "__main__":
    print(run())
