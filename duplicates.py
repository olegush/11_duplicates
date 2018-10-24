import sys
import os
from os.path import getsize
from collections import defaultdict


def get_duplicates(rootdirpath):
    fileslist = defaultdict(dict)
    for path, dirs, files in os.walk(rootdirpath):
        for filename in files:
            filesize = str(getsize(os.path.join(path, filename)))
            paths = [path]
            if fileslist.get((filename, filesize)) is not None:
                paths = fileslist.get((filename, filesize)) + [path]
            fileslist[(filename, filesize)] = paths
    filtered_dict = {
        filenamesize: paths for filenamesize, paths
        in fileslist.items() if len(paths) > 1
    }
    return filtered_dict


if __name__ == '__main__':
    try:
        user_dirpath = sys.argv[1]
        if os.path.isdir(user_dirpath):
            print('Founded duplicates:')
            duplicates_list = get_duplicates(user_dirpath).items()
            for fileinfo, filepath in duplicates_list:
                print('{} ({} bytes) in {}'
                      .format(fileinfo[0], fileinfo[1], filepath)
                      )
        else:
            print('No such directory')
    except IndexError:
        print('No script parameter (path to directory)')
