import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command', metavar='command')
    sub_parsers.required = True
    sub_parsers.add_parser('init', help="Initialise a new repo")

    args = parser.parse_args()
    if args.command == 'init':
        print ("New repo initialised")


