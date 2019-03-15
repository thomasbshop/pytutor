import os  # This module provides a portable way of using operating system dependent functionality.

# os.walk: Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each
# directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames,
# filenames).
# Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in
# the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
# listing = os.walk('.')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory <<{}>>".format(f))
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + "<<{}>>".format(f))

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of <<{}>>".format(s))

        dir_list(s)
    else:
        print("<<{}>> does not exist".format(s))


list_directories('.')
