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


from .manifest import Manifest
from docopt import docopt
import grequests


def main():
    arguments = docopt(__doc__, version=__version__)
    if arguments['--version']:
        print("yaurtww {0}".format(__version__))
        return

    if arguments['<filename>']:
        manifest = Manifest()
        files = manifest.map_files()
