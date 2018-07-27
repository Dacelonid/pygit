import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command', metavar='command')
    sub_parsers.required = True
    sub_parsers.add_parser('init', help="Initialise empty git repository in current directory")

    args = parser.parse_args()
    if args.command == 'init':
        git_dir = os.path.join(os.getcwd(), ".git")
        os.mkdir(git_dir)
        os.mkdir(os.path.join(git_dir, "refs"))
        os.mkdir(os.path.join(git_dir, "objects"))
        open(os.path.join(git_dir, "HEAD"), "w")
        print ("Initialised empty git repository in {}". format (git_dir))


