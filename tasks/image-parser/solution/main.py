"""Reference implementation entrypoint for image-parser."""


def run(context=None):
    """Run the image-parser workflow."""
    return {"feature": "image-parser", "status": "ok"}


if __name__ == "__main__":
    print(run())
