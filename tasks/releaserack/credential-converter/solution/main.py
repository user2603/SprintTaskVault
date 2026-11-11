"""Reference implementation entrypoint for credential-converter."""


def run(context=None):
    """Run the credential-converter workflow."""
    return {"feature": "credential-converter", "status": "ok"}


if __name__ == "__main__":
    print(run())
