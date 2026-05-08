import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="A friendly greeting program")
    parser.add_argument("name", help="Your name")
    parser.add_argument("-n", "--number", type=int, default=1,
                        help="Number of times to greet (default: 1)")
    args = parser.parse_args()

    for _ in range(args.number):
        print(f"Hello, {args.name}!")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
