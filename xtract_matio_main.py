
import time
import argparse
from materials_io.utils.interface import run_all_parsers_on_group

import os


def extract_matio(paths, parser):
    """Runs a file through MaterialsIO parsers.

    Parameter:
    paths (list(str): List of paths of files to parse.

    Return:
    meta_dictionary (dict): Dictionary of all metadata extracted using
    MaterialsIO parsers.
    """

    t0 = time.time()
    meta_dictionary = {"matio": {}, "parser": parser}

    meta_dictionary['debug'] = paths

    try:
        gen_dump = []
        # parser_gen = execute_parser(parser, paths) # List index error from this line.
        parser_gen = run_all_parsers_on_group(group=paths, adapter_map="match", include_parsers=[parser])

        for item in parser_gen:
            gen_dump.append(item)

        meta_dictionary["matio"] = gen_dump

    except Exception as e:
        # meta_dictionary["matio"]
        meta_dictionary['error1'] = f"THE LIST ERROR WAS HERE: {e}"

    meta_dictionary["CONTAINER_VERSION"] = os.environ['CONTAINER_VERSION']

    total_time = time.time() - t0
    meta_dictionary.update({"extract time": total_time})

    return meta_dictionary


def execute_extractor(paths, parser):

    mdata = extract_matio(paths, parser)
    return mdata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--paths', nargs='+', help='list of files to parse',
                        type=str, required=True)
    parser.add_argument('--parser', type=str, required=True)
    args = parser.parse_args()
    meta = extract_matio(args.paths, args.parser)
    print(meta)


