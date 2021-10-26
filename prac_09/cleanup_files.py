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
        if char.isupper() and i != 0:
            if new_filename[i - 1] != " " and new_filename[i - 1] != "(" and new_filename[i - 1] != "_(":
                new_filename[i] = char.replace(char, f"_{char}")
        if not char.isupper() and new_filename[i-1] == " " or i == 0 or new_filename[i-1] == "(" or new_filename[i-1] == "_":
            new_filename[i] = char.upper()
        if char == " ":
            new_filename[i] = char.replace(" ", "_")
        if char == "(" and new_filename[i-1] != "_":
            new_filename[i] = char.replace(char, f"_{char}")
        if char == '.':
            break
    new_filename = "".join(new_filename)
    new_filename = new_filename.replace(".TXT", ".txt")
    return new_filename


main()
