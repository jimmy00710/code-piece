import os 
from pathlib import Path


def _scan_files(base_dir,file_extension):
    '''
    The os scan dir creates an iterator.
    Then we use a for loop to go over that iterator.
    Then we check whehter the things we are iterating are
    directory or files. In case they are files we return the base directory 
    of thoes files. 
    In case if they are directory we do a recursive call 
    and search in thar directory. 
    '''

    for entry in os.scandir(base_dir):
        if entry.is_file() and (entry.name.endswith(file_extension)):
            yield entry.path
        elif entry.is_dir():
            yield from _scan_files(entry.path,file_extension)
        else:
            #For debugging purpose comment this out.
            #print(f'Neither a file nor a dir : {entry.path})
            pass


    
def get_files(base_dir,file_extension):
    list_of_files = []

    for i in _scan_files(base_dir,file_extension):
        list_of_files.append(i)

    return list_of_files

    