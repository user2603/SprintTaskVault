"""Reference implementation entrypoint for map-picker."""


def run(context=None):
    """Run the map-picker workflow."""
    return {"feature": "map-picker", "status": "ok"}


if __name__ == "__main__":
    print(run())
