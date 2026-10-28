"""Reference implementation entrypoint for digest-profiler."""


def run(context=None):
    """Run the digest-profiler workflow."""
    return {"feature": "digest-profiler", "status": "ok"}


if __name__ == "__main__":
    print(run())
