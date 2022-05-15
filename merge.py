"""Module deals with functionality concerning merging video clips into
one.

Requires external library `moviepy`.

Contains:

    *:func:`run`
    *:func:`is_video`
"""

import msg
import moviepy.editor, os


def run(source, source_is_folder, dest):
    """Completes the merging of many videos into one containing all
    clips shown consecutively.

    :param source: path to separated files
    :type source: str
    :param source_is_folder: if source is a path to a folder, as
        opposed to a single file
    :type source_is_folder: bool
    :param dest: path to folder for merged video to be placed
    :type dest: str
    """

    msg.form_print('Starting merge...')
    files = []
    if source_is_folder:
        files = [os.path.join(source, file) for file in os.listdir(source)
                 if is_video(file)]
    else:
        files = [source]
    msg.form_print(f'Found {len(files)} files from {source}')
    clips = [moviepy.editor.VideoFileClip(file) for file in files]
    final = moviepy.editor.concatenate_videoclips(clips)
    final_name = (os.path.splitext(os.path.basename(files[0]))[0]
                  + '_merged.mp4')
    final.write_videofile(os.path.join(dest, final_name))
    msg.form_print(f'Wrote {final_name} to {dest}')


def is_video(path):
    """Checks that a path has a video format file extension.

    :param path: path to a file
    :type path: str
    """

    ext = os.path.splitext(path)[1]
    return ext.lower() in ['.mp4', '.avi', '.mov']
