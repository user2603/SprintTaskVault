"""Reference implementation entrypoint for comment-logger."""


def run(context=None):
    """Run the comment-logger workflow."""
    return {"feature": "comment-logger", "status": "ok"}


if __name__ == "__main__":
    print(run())
