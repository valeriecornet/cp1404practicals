"""
Rename files to a desired format.
"""
import os


def main():
    """Cleanup files within subdirectories to a desired format."""
    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        # Loop to rename the files
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_filename = list(filename)
    for i, char in enumerate(new_filename):
        # if new word (with uppercase), add an underscore between words
        if char.isupper() and i != 0 and new_name[i-1] != " " and new_name[i-1] != "(":
            new_filename[i] = f"_{char}"
        # if a new word starts with lowercase, make uppercase
        if not char.isupper() and new_filename[i-1] == " " or new_filename[i-1] == "_" or i == 0 or new_filename[i-1] == "(":
            new_filename[i] = char.upper()
        # if there is a space, make space an underscore
        if char == " ":
            new_filename[i] = "_"
        # before parentheses a add an underscore as a space
        if char == "(" and new_filename[i-1] != "_":
            new_filename[i] = f"_{char}"
        # stop editing name before the format
        if char == '.':
            break
    new_filename = "".join(new_filename)
    new_filename = new_filename.replace(".TXT", ".txt")
    return new_filename


main()