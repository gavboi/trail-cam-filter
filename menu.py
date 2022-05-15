"""This module acts as the controller for the project.
"""

import msg
import os.path

SAVE_FILE = 'past.txt'
"""File name for file storing past paths for future access."""
FUNCTIONS = ['exit', 'prop', 'merge', 'speed', 'diff']
"""Inputs accepted that tie to some other action."""
FUNCTIONS_HELP = (' exit  : close menu\n'
                  + ' prop  : sort by video properties like duration\n'
                  + ' merge : combine clips into one video\n'
                  + ' speed : change framerate of a video\n'
                  + ' diff  : sort by visual differences in video frames')
"""Message displaying what all accepted functions do."""


def get_past_paths():
    """Gets the last video source and destination used, or if one is not
    found, suggests a location.

    :raises IndexError: if working directory changes in the middle of
        this function running, it will not correctly identify a path and
        will throw this error
    :return: str for path to source, bool for if path is a folder, str
        for path to destination
    :rtype: tuple
    """

    try_source = (os.path.join('E:', 'DCIM', '100STLTH'),
                  os.getcwd())
    try_dest = (os.path.join(os.path.expanduser('~'), 'Downloads'),
                os.getcwd())
    source = ''
    source_is_folder = None
    dest = ''
    file_content = []
    if os.path.isfile(SAVE_FILE): # check for saved
        with open(SAVE_FILE, 'r') as file:
            file_content = file.readlines()
        if len(file_content) >= 2: # add to front of line if exist
            try_source = (file_content[0].strip(),) + try_source
            try_dest = (file_content[1].strip(),) + try_dest
    i = 0
    while source == '': # find best valid source
        if os.path.isdir(try_source[i]):
            source = try_source[i]
            source_is_folder = True
        elif os.path.isfile(try_source[i]):
            source = try_source[i]
            source_is_folder = False
        i += 1
    i = 0
    while dest == '': # find best valid destination
        if os.path.isdir(try_dest[i]):
            dest = try_dest[i]
        i += 1
    return source, source_is_folder, dest


def make_full_path(path, file_type='dir'):
    """Checks that the path is the full path.

    :param path: path to file, full or not
    :type path: str
    :param file_type: directory or file
    :type file_type: str
    :return: full path from given path
    :rtype: str
    """

    if file_type == 'dir':
        if os.path.isdir(os.path.join(os.getcwd(), path)):
            return os.path.join(os.getcwd(), path)
        return path
    if os.path.isfile(os.path.join(os.getcwd(), path)):
        return os.path.join(os.getcwd(), path)
    return path


def run():
    """Main functionality of menu.

    :return: if project should exit
    :rtype: bool
    """
    
    msg.form_print(f'{msg.TEXT_INIT}\n') # startup text
    function = ''
    while function == '':
        msg.form_print(msg.TEXT_FUNCTION)
        print(FUNCTIONS_HELP)
        inp = input(msg.TEXT_PROMPT).strip()
        if inp in FUNCTIONS:
            function = inp
        else:
            msg.form_print('Not a valid function, try again,\n')
    if function == 'exit':
        return True
    else:
        msg.form_print(f'Using function {function}\n')
    suggest_source, suggest_is_folder, suggest_dest = get_past_paths()
    source = ''
    source_is_folder = None
    dest = ''
    while source == '': # get source from input
        msg.form_print(msg.TEXT_SOURCE)
        msg.form_print(f'({suggest_source})')
        inp = input(msg.TEXT_PROMPT).strip()
        if os.path.isdir(inp):
            source_is_folder = True
            source = make_full_path(inp, 'dir')
        elif os.path.isfile(inp):
            source_is_folder = False
            source = make_full_path(inp, 'file')
        elif inp == '':
            source_is_folder = suggest_is_folder
            source = suggest_source
        else:
            msg.form_print('Not a valid path, try again,\n')
    msg.form_print(f'Using source {source}\n')
    while dest == '': # get dest from input
        msg.form_print(msg.TEXT_DEST)
        msg.form_print(f'({suggest_dest})')
        inp = input(msg.TEXT_PROMPT).strip()
        if os.path.isdir(inp):
            dest = make_full_path(inp, 'dir')
        elif inp == '':
            dest = suggest_dest
        else:
            msg.form_print('Not a valid path, try again,\n')
    msg.form_print(f'Using destination {dest}\n')


if __name__ == '__main__':
    run()
        
    
