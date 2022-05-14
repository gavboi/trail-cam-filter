"""Module helps with menu messages and text formatting.

Contains:

    * :func:`form_print`
"""

TEXT_INIT = '--- TRAIL CAM FILTER ---'
"""Text for indication of project starting."""
TEXT_SOURCE = ('Enter a folder containing videos to use or a single video '
               + 'file. Leave blank to use suggested directory.')
"""Text for source selection prompt."""
TEXT_DEST = ('Enter a folder to generate output. If folder does not exist, '
             + 'it will be created. Leave blank to use suggested '
             + 'directory.')
"""Text for destination selection prompt."""
TEXT_PROMPT = ' > '
"""Text for actual user input prompt."""


def form_print(text):
    """Prints text with forced max line lengths. If single word is too
    long for a line however, it will not split it. Also adds a space to
    the start of lines for aesthetics, that is included in the
    character count.

    Max line length arbitrarily set to 80 characters.

    :param text: text to be printed
    :type text: str
    """

    new_text = ' '
    max_length = 80
    length = 1
    for word in text.split(' '):
        if (length + len(word)) > 80 and length != 1:
            new_text += f'\n {word} '
            length = len(word) + 2
        else:
            new_text += f'{word} '
            length += len(word) + 1
    print(new_text)
            
            
