"""Sort files"""

import os
import shutil


def main():
    """Sort files according to extensions"""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(filename, '{extension/}')


main()
