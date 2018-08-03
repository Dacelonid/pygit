import argparse
import os


def init(root_dir):
    git_dir = os.path.join(root_dir, ".git")
    refs_dirs = [os.path.join(git_dir, "refs"), os.path.join(git_dir, "refs", "heads"), os.path.join(git_dir, "refs", "tags")]
    objects_dirs = [os.path.join(git_dir, "objects"), os.path.join(git_dir, "objects", "info"), os.path.join(git_dir, "objects", "pack")]
    branches_dirs = [os.path.join(git_dir, "branches")]
    hooks_dirs = [os.path.join(git_dir, "hooks")]
    info_dirs = [os.path.join(git_dir, "info")]

    starting_dirs = [git_dir] + refs_dirs + objects_dirs + branches_dirs + hooks_dirs + info_dirs

    for name in starting_dirs:
        os.mkdir(name)

    write_file(os.path.join(git_dir, "HEAD"), b'ref: refs/heads/master')
    write_file(os.path.join(git_dir, "config"), b'')
    write_file(os.path.join(git_dir, "info", "exclude"), b'')
    write_file(os.path.join(git_dir, "description"), b'')

    print ("Initialised empty git repository in {}". format (git_dir))


def write_file(path, data):
    file_name = open(path, "wb")
    file_name.write(data)
    file_name.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command', metavar='command')
    sub_parsers.required = True
    sub_parsers.add_parser('init', help="Initialise empty git repository in current directory")

    args = parser.parse_args()
    if args.command == 'init':
        init(os.getcwd())


