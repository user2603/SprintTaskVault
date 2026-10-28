"""Reference implementation entrypoint for link-sampler."""


def run(context=None):
    """Run the link-sampler workflow."""
    return {"feature": "link-sampler", "status": "ok"}


if __name__ == "__main__":
    print(run())
