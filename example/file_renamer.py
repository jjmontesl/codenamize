#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from codenamize import codenamize
# PLEASE BE AWARE THIS IMPORT IS NOT IN THE PIPENV.
# THIS IS NOT A DEPENDENCY AS IT IS NOT REQUIRED STRICTLY TO RUN THE LIBRARY.
# PLEASE INSTALL BY YOURSELF IF YOU NEED TO RUN THIS SCRIPT !
# Please see : https://pypi.org/project/codenamize/ and https://github.com/jjmontesl/codenamize
import argparse
import pathlib

'''
COLLISIONS CALCULATIONS
3 adj (max 4 chars) = 962286000 combinations
3 adj (max 5 chars) = 25471468750 combinations
3 adj (max 6 chars) = 122636229513 combinations
3 adj (max 7 chars) = 355283372136 combinations
3 adj (max 0 chars) = 2119641566400 combinations <= We choose this configuration :)
TESTS
  (*, 1 adj, max 3) => 1742 distinct results (space size is 2760)
  (*, 2 adj, max 3) => 41855 distinct results (space size is 66240)
  (*, 3 adj, max 3) => 1005353 distinct results (space size is 1589760)

'''

class Humanizer():

    def __init__(self):
        self.already_generated = set({})


    def rename_all_files(self, path : pathlib.Path):
        p = path.resolve().glob('**/*')
        files = [x for x in p if x.is_file()]

        files.sort() # To prevent System's way of sorting paths.
        # Therefore, we are sure about the order of treatment on any machine (deteminism)

        print(f"Going to change names of : {files} \n Are you sure you want to continue ?")
        input()

        first = True
        for f in files :

            new_name = self.humanize_name(f.name + f.suffix)

            if first :
                print(f"The file {f.name} is going to be changed to {new_name}. \n Do you want to continue ? (Automatically approved after this first warning)")
                input()
                first = False

            f.rename(f.parent / str(new_name + f.suffix))

        print(f"Done. {len(files)} modified.")

    def humanize_name(self, name:str, collision_removal : bool =True) -> str:
        new_name = codenamize(name, 3, 0)

        i = 0
        while collision_removal and self.is_already_drawn(new_name) :
            print(f"Collision found on filename {name} generating {new_name}. Adding 1 to filename.")
            # Modify/Create a new name
            tmp_name = name + str(i)

            # Redraw the new name
            new_name = codenamize(tmp_name, 3, 0)
            print(f"Collision handled by renaming {name} to {tmp_name} generating {new_name}.")

        self.already_generated.add(new_name)
        return new_name

    def is_already_drawn(self, new_name:str) -> bool:
        return {new_name}.issubset(self.already_generated)

def main():
    # Usage example : python3 ./humanizer.py -p ./MINI_DATASET/
    parser = argparse.ArgumentParser(description='Rename all files in the given directory and subdirectory')
    parser.add_argument('-p', '--path', dest='path', action='store', type=lambda p: pathlib.Path(p).absolute(), default=1, help='all path')
    parser.add_argument('--version', action='version', version='humanizer %s' % ("1.0.0"))

    args = parser.parse_args()
    humanizer = Humanizer()
    humanizer.rename_all_files(args.path)


if __name__ == "__main__":
    main()


