"""Reference implementation entrypoint for search-parser."""


def run(context=None):
    """Run the search-parser workflow."""
    return {"feature": "search-parser", "status": "ok"}


if __name__ == "__main__":
    print(run())
