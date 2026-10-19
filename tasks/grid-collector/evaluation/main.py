import argparse


def main(args):
    """Evaluate grid-collector outputs."""
    assert args.agent_workspace
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent_workspace", required=True)
    args = parser.parse_args()
    exit(0 if main(args) else 1)
