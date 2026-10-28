"""Reference implementation entrypoint for rule-resolver."""


def run(context=None):
    """Run the rule-resolver workflow."""
    return {"feature": "rule-resolver", "status": "ok"}


if __name__ == "__main__":
    print(run())
