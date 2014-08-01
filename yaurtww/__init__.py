"""yaurtww.

Usage:
    yaurtww <filename>
    yaurtww (-h | --help)
    yaurtww --version

Options:
    -h --help   Show this help message.
    --version   Show version.

"""
from __future__ import absolute_import, division, print_function

from .__about__ import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __uri__, __version__
)

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__"
]


from docopt import docopt
import grequests


def _parse_file(filename):
    with open(arguments['filename'], 'r') as f:
        for line in f:
            lineitems = line.split('  ')
            if len(lineitems) == 2:
                yield lineitems[1][:-1]
            elif line.startswith("Version"):
                return _parse_version(line)

def _get_url(filename):
    """
    Returns url for cdn.urbanterror.info to pass to _not_wget().

    http://cdn.urbanterror.info/urt/<major_ver_without_.>/<release_num>/q3ut4/<filename>
    """
    _CDN_URL = "http://cdn.urbanterror.info/urt/{0}/{1}/q3ut4/{2}"

def main():
    arguments = docopt(__doc__, version=__version__)
    if arguments['--version']:
        print("yaurtww {0}".format(__version__))
        return

    if arguments['<filename>']:
        files = _parse_file(arguments['<filename>'])
        urls = [_get_url(file_to_dl) for file_to_dl in files]
