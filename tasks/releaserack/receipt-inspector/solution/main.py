"""Reference implementation entrypoint for receipt-inspector."""


def run(context=None):
    """Run the receipt-inspector workflow."""
    return {"feature": "receipt-inspector", "status": "ok"}


if __name__ == "__main__":
    print(run())
