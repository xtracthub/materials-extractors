import time
import argparse
from materials_io.utils import execute_parser, get_available_parsers


def args_to_parser(parser_name, path):
    if parser_name in get_available_parsers():
        return execute_parser(parser_name, path)
    else:
        print("Invalid parser name")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--parser', help='type of parser to use: ase, '
                                         'crystal (crystal structure), dft, '
                                         'em electron_microscopy, image',
                        type=str, required=True)
    parser.add_argument('--path', help='file path or file group to parse',
                        type=str, required=True)
    args = parser.parse_args()

    t0 = time.time()
    meta = args_to_parser(args.parser, args.path)
    t1 = time.time()
    print({args.parser: meta})
    print(t1 - t0)
