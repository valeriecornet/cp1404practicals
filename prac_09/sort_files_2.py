"""Sort files - version 2"""

import os


def main():
    """Sort files according to extensions and user directions"""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]

        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            # Create folder categories
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
