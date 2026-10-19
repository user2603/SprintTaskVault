"""Reference implementation entrypoint for palette-extractor."""


def run(context=None):
    """Run the palette-extractor workflow."""
    return {"feature": "palette-extractor", "status": "ok"}


if __name__ == "__main__":
    print(run())
