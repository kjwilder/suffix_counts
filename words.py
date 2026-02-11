import argparse
import sys

from collections import defaultdict


def parse_args(argv):
    parser = argparse.ArgumentParser(prog="words")
    parser.add_argument(
        "-d",
        "--dictionary_file",
        default="words.txt",
        help="Text file containing words, one per line",
    )
    return parser.parse_args(argv)


def main(argv):
    args = parse_args(argv)
    suffixes = defaultdict(set)
    for word in open(args.dictionary_file):
        if word.startswith("#"):
            continue
        first_letter, suffix = word[0], word[1:].strip()
        suffixes[suffix].add(first_letter)
    for suffix in sorted(suffixes, key=lambda x: (len(suffixes[x]), x)):
        num_words = len(suffixes[suffix])
        first_letters = " ".join(sorted(suffixes[suffix]))
        print(f"{num_words:>2} {suffix:<22} [{first_letters}]")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
