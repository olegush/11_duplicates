import sys
import os
from os.path import getsize


def get_duplicates(rootdirpath):
    fileslist = []
    paths = []
    for path, dirs, files in os.walk(rootdirpath):
        for file in files:
            fileslist.append([file, str(getsize(path + '/' + file))])
            paths.append(path)
    for file, path in zip(fileslist, paths):
        if fileslist.count(file) > 1:
            print('{} ({} bytes) in {}'.format(file[0], file[1], path))


if __name__ == '__main__':
    try:
        user_dirpath = sys.argv[1]
    except IndexError:
        print('No script parameter (path to directory)')
    except OSError:
        print('No such directory')
    else:
        print('Founded duplicates:')
        get_duplicates(user_dirpath)
