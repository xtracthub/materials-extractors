import time
import argparse
from materials_io.utils.interface import run_all_parsers


def extract_matio(path):
    """Runs a file through all available MaterialsIO parsers.
    Parameter:
    path (str): File path of file to parse.
    Return:
    meta_dictionary (dict): Dictionary of all metadata extracted using
    MaterialsIO parsers.
    """
    t0 = time.time()
    meta_dictionary = {"matio": {}}

    parser_gen = run_all_parsers(path, exclude_parsers=['noop', 'generic', 'csv'])
    for parser_data in parser_gen:
        meta_dictionary["matio"].update({parser_data[1]: parser_data[2]})

    total_time = time.time() - t0
    meta_dictionary.update({"extract time": total_time})

    return meta_dictionary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='file path or file group to parse',
                        type=str, required=True)
    args = parser.parse_args()

    meta = args_to_parser(args.path)
    print(meta)