# Copyright 2025 Thomas Gingele <b1tc0r3@proton.me>
# Copyright 2025 mitch-n <quarrel-most-heap@duck.com>
import argparse

from bitmunch import BitMunch


def get_args():
    parser = argparse.ArgumentParser(
        prog="BitMunch Encoder",
        epilog="Copyright 2025 Thomas Gingele b1tc0r3@proton.me, mitch-n quarrel-most-heap@duck.com"
    )

    parser.add_argument(
        "-i",
        "--input",
        help="The raw payload. Read from STDIN.",
        required=True,
    )

    parser.add_argument(
        "-p",
        "--padding",
        help="Execute mode only. Addes padding*2 to padding*10 encoded characters (randomized) to the front and back of the payload.",
        default=0,
        type=int,
    )

    parser.add_argument(
        "-e",
        "--exec",
        action="store_true",
        help="Make the payload self-execute when pasted into a browser terminal. No extra eval() required.",
    )

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    bm = BitMunch()

    if args.exec:
        print(bm.encode_self_executing(args.input, args.padding))

    else:
        print(bm.encode(args.input))


if __name__ == "__main__":
    main()
