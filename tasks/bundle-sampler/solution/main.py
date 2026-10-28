"""Reference implementation entrypoint for bundle-sampler."""


def run(context=None):
    """Run the bundle-sampler workflow."""
    return {"feature": "bundle-sampler", "status": "ok"}


if __name__ == "__main__":
    print(run())
