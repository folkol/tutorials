import spam

"""
1) Search for built-in module named 'spam'
2) If not found, search sys.path for a file named spam.py
    - sys.path is initialized from these locations:
        * The directory containing the input script (or pwd, if none is specified)
        * PYTHONPATH (env variable, similar to $PATH. Augments, rather than replaces.
            (PYTHONPATH, separated by os.pathsep. directories or zip files, non existent
            directories are ignored.)
        * The installation-dependent default
"""