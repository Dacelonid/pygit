import argparse
import os


def init(root_dir):
    git_dir = os.path.join(root_dir, ".git")
    refs_dirs = [os.path.join(git_dir, "refs"), os.path.join(git_dir, "refs", "heads"), os.path.join(git_dir, "refs", "tags")]
    objects_dirs = [os.path.join(git_dir, "objects"), os.path.join(git_dir, "objects", "info"), os.path.join(git_dir, "objects", "pack")]
    branches_dirs = [os.path.join(git_dir, "branches")]
    desc_dirs = [os.path.join(git_dir, "description")]
    config_dirs = [os.path.join(git_dir, "config")]
    hooks_dirs = [os.path.join(git_dir, "hooks")]
    info_dirs = [os.path.join(git_dir, "info"), os.path.join(git_dir, "info", "exclude")]

    starting_dirs = [git_dir] + refs_dirs + objects_dirs + branches_dirs + config_dirs + hooks_dirs + info_dirs + desc_dirs

    for name in starting_dirs:
        os.mkdir(name)

    head_file = open(os.path.join(git_dir, "HEAD"), "wb")
    head_file.write(b'ref: refs/heads/master')
    head_file.close()
    print ("Initialised empty git repository in {}". format (git_dir))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command', metavar='command')
    sub_parsers.required = True
    sub_parsers.add_parser('init', help="Initialise empty git repository in current directory")

    args = parser.parse_args()
    if args.command == 'init':
        init(os.getcwd())


