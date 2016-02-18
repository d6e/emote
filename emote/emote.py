""" A simple CLI tool for quickly copying common emoticon/emoji to your
clipboard. """
import pyperclip
import json
import sys
import argparse

def read_emote_mapping(filename="mapping.json"):
    # TODO: Read from an env var and a harcoded .dotfile
    with open(filename) as f:
        return json.load(f)

def parse_arguments():
    parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__)
    parser.add_argument('-l','--list', action="store_true",
                        help="List all available emotes.")
    parser.add_argument('-s','--silent', action="store_true",
                        help="Don't print to stdout.")
    parser.add_argument("name", type=str, nargs='?',
                        help="The name of the emote.")

    # Print help if no cli args are specified.
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)
    return parser.parse_args()

def list_emotes(emotes):
    print [e for e in emotes.keys()]
    print [e for e in emotes.values()]

def print_emote(name, emotes, silent=False):
    try:
        emote = emotes[name]
        pyperclip.copy(emote)
        if not silent:
            print emote
    except KeyError:
        print("That emote does not exist. You can see all existing emotes "
        "with the command: `emote -l`.")

def main():
    args = parse_arguments()
    emotes = read_emote_mapping()
    if args.list:
        list_emotes(emotes)
    if args.name:
        print_emote(args.name, emotes, silent=args.silent)


if __name__ == "__main__":
    main()
