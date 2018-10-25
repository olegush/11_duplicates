import sys
import os
from os.path import getsize
from collections import defaultdict


def get_duplicates(rootdirpath):
    fileslist = defaultdict(list)
    for path, dirs, filenames in os.walk(rootdirpath):
        for filename in filenames:
            filesize = str(getsize(os.path.join(path, filename)))
            fileslist[(filename, filesize)].append(path)
    filtered_dict = {
        filenamesize: paths for filenamesize, paths
        in fileslist.items() if len(paths) > 1
    }
    return filtered_dict


if __name__ == '__main__':
    try:
        user_dirpath = sys.argv[1]
    except IndexError:
        print('No script parameter (path to directory)')
    else:
        if os.path.isdir(user_dirpath):
            duplicates_list = get_duplicates(user_dirpath).items()
            print('{}'.format('Founded duplicates:'
                              if len(duplicates_list) > 0
                              else 'No duplicates'
                              )
                  )
            for (filename, filesize), filepaths in duplicates_list:
                print('{} ({} bytes) in {}'
                      .format(filename, filesize, filepaths)
                      )
        else:
            print('No such directory')
