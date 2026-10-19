"""Reference implementation entrypoint for shortcut-loader."""


def run(context=None):
    """Run the shortcut-loader workflow."""
    return {"feature": "shortcut-loader", "status": "ok"}


if __name__ == "__main__":
    print(run())
