"""Reference implementation entrypoint for coupon-editor."""


def run(context=None):
    """Run the coupon-editor workflow."""
    return {"feature": "coupon-editor", "status": "ok"}


if __name__ == "__main__":
    print(run())
