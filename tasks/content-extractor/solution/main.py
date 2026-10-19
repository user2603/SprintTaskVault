"""Reference implementation entrypoint for content-extractor."""


def run(context=None):
    """Run the content-extractor workflow."""
    return {"feature": "content-extractor", "status": "ok"}


if __name__ == "__main__":
    print(run())
