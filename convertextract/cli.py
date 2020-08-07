"""
Use argparse to handle command-line arguments.
"""

import argparse
import encodings
import os
import pkgutil
import sys
import six
import re
import glob

from g2p.mappings.langs import LANGS_NETWORK
import argcomplete


from convertextract import VERSION
from convertextract.parsers import DEFAULT_ENCODING, _get_available_extensions
from convertextract import process
from convertextract.exceptions import CommandLineError
from convertextract.colors import red


class AddToNamespaceAction(argparse.Action):
    """This adds KEY,VALUE arbitrary pairs to the argparse.Namespace object
    """

    def __call__(self, parser, namespace, values, option_string=None):
        key, val = values.strip().split('=')
        if hasattr(namespace, key):
            parser.error((
                'Duplicate specification of the key "%(key)s" with --option.'
            ) % locals())
        setattr(namespace, key, val)


# Fix FileType to honor 'b' flag, see: https://bugs.python.org/issue14156
class FileType(argparse.FileType):
    def __call__(self, string):
        if string == '-' and six.PY3:
            if 'r' in self._mode:
                string = sys.stdin.fileno()
            elif 'w' in self._mode:
                string = sys.stdout.fileno()
        return super(FileType, self).__call__(string)


# This function is necessary to enable autodocumentation of the script
# output
def get_parser():
    """Initialize the parser for the command line interface and bind the
    autocompletion functionality"""
    # initialize the parser
    parser = argparse.ArgumentParser(
        description=(
            'Command line tool for extracting text from any document. '
        ) % locals(),
    )

    # define the command line options here
    parser.add_argument(
        'filename', help='Filename to extract text from'
    ).completer = argcomplete.completers.FilesCompleter
    parser.add_argument(
        '-e', '--encoding', type=str, default=DEFAULT_ENCODING,
        choices=_get_available_encodings(),
        help='Specify the encoding of the output',
    )
    parser.add_argument(
        '--extension', type=str, default=None,
        choices=_get_available_extensions(),
        help='Specify the extension of the file',
    )
    parser.add_argument(
        '-o', '--output', type=FileType('wb'),
        help='Output raw text in this file',
    )
    parser.add_argument('--no-write', dest='no_write', action='store_true',
                        help="Disable default console writing of converted file.")
    parser.add_argument(
        '-m', '--mapping', type=os.path.abspath,
        help='Path to a lookup table for conversion. Only use this if the g2p library does not have the mapping you want.',
    )
    parser.add_argument('-il', '--input-language',
                        choices=LANGS_NETWORK.nodes,
                        help='The input language to be converted from, for a full list please visit https://g2p-studio.herokuapp.com/api/v1/langs')
    parser.add_argument('-ol', '--output-language',
                        choices=LANGS_NETWORK.nodes,
                        help='The output language to be converted to, for a full list please visit https://g2p-studio.herokuapp.com/api/v1/langs')
    parser.add_argument(
        '-O', '--option', type=str, action=AddToNamespaceAction,
        help=(
            'Add arbitrary options to various parsers of the form '
            'KEYWORD=VALUE. A full list of available KEYWORD options is '
            'available at http://bit.ly/textract-options'
        ),
    )
    parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s '+VERSION,
    )

    # enable autocompletion with argcomplete
    # argcomplete.autocomplete(parser)

    return parser


def _get_available_encodings():
    """Get a list of the available encodings to make it easy to
    tab-complete the command line interface.

    Inspiration from http://stackoverflow.com/a/3824405/564709
    """
    available_encodings = set(encodings.aliases.aliases.values())
    paths = [os.path.dirname(encodings.__file__)]
    for importer, modname, ispkg in pkgutil.walk_packages(path=paths):
        available_encodings.add(modname)
    available_encodings = list(available_encodings)
    available_encodings.sort()
    return available_encodings





