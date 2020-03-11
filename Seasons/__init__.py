"""
This helps import every module in this directory
https://stackoverflow.com/questions/46980637/importing-dynamically-all-modules-from-a-folder
"""
import os
direc = os.path.dirname(os.path.abspath(__file__))
modules = [os.path.splitext(_file)[0] for _file in os.listdir(direc) if not _file.startswith('__')]
Seasons = []
for mod in modules:
    exec('from Seasons import {}; Seasons.append({})'.format(mod, mod))
