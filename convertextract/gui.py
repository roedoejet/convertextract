import os
import sys
import logging

from gooey import Gooey, GooeyParser
from g2p.mappings.langs import LANGS_NETWORK

import convertextract
from convertextract.cli import _get_available_encodings
from convertextract import process
from convertextract.parsers import DEFAULT_ENCODING
from convertextract.exceptions import CommandLineError
from convertextract.colors import red
from convertextract import VERSION

def get_gui():
    parser = GooeyParser(
        description=(
            'GUI for extracting and converting text. '
        ) % locals(),
    )
    parser.add_argument(
        'filename', help='Filename to extract text from', widget='FileChooser'
    )
    parser.add_argument(
        '-e', '--encoding', type=str, default=DEFAULT_ENCODING,
        choices=_get_available_encodings(),
        help='Specify the encoding of the output',
    )
    parser.add_argument('-il', '--input-language',
                        choices=LANGS_NETWORK.nodes,
                        help='The input language to be converted from, for a full list please visit https://g2p-studio.herokuapp.com/api/v1/langs')
    parser.add_argument('-ol', '--output-language',
                        choices=LANGS_NETWORK.nodes,
                        help='The output language to be converted to, for a full list please visit https://g2p-studio.herokuapp.com/api/v1/langs')
    parser.add_argument(
        '-m', '--mapping', type=os.path.abspath, required=False, widget='FileChooser',
        help='Path to a custom lookup table for conversion. Only use this if the g2p library does not have the mapping you want.',
    )
    return parser


ABOUT = {
    'type': 'AboutDialog',
    'menuTitle': 'About',
    'name': 'Convertextract GUI',
    'description': 'GUI for extracting and converting text.',
    'version': VERSION,
    'copyright': 'Aidan Pine 2020',
    'website': 'https://github.com/roedoejet/convertextract',
    'developer': 'https://aidanpine.ca',
    'license': 'MIT'
}


@Gooey(program_name='Convertextract',
       program_description="Extract and Convert text",
       menu=[{'name': "Help", 'items': [ABOUT]}]
       )
def gooey_main():
    """Interpret the command-line arguments, process the document and
    raise errors accordingly (with traceback surpressed).
    """
    parser = get_gui()
    args = parser.parse_args()
    try:
        logging.info(f'Extracting text from "{args.filename}"')
        if args.mapping:
            logging.info(
                f'Preparing to convert from mapping file provided at "{args.mapping}"')
        else:
            logging.info(
                f'Preparing to convert from "{args.input_language}" to "{args.output_language}"')
        output = process(**vars(args))
    except CommandLineError as ex:
        logging.error(
            "Whoops. Something went wrong. Please check your input file and your mapping file (if using a custom one)")
        sys.stderr.write(red(ex) + '\n')
        sys.exit(1)
    else:
        fn, ext = os.path.splitext(args.filename)
        output_path = fn + '_converted' + ext
        logging.info(f'Converted file available at "{output_path}"')


if __name__ == '__main__':
    gooey_main()
