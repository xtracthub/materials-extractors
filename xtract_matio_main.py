import time
import argparse
from materials_io.utils.interface import execute_parser, get_available_parsers

import os

def extract_matio(path, parser):
    """Runs a file through all available MaterialsIO parsers.
    Parameter:
    path (str): File path of file to parse.
    Return:
    meta_dictionary (dict): Dictionary of all metadata extracted using
    MaterialsIO parsers.
    """

    single_file_ls = ['crystal']

    if parser in single_file_ls:
        single_file = True

    t0 = time.time()
    meta_dictionary = {"matio": {}}
    file_list = os.listdir(path)
    
    # If single, file then get metadata from each file in the directory (/group)
    if single_file:
        meta_dictionary["matio"]["files"] = []
        for file_n in file_list:
            try: 
                parser_gen = execute_parser(parser, f"{path}/{file_n}")
                meta_dictionary["matio"]["files"].append({parser : parser_gen})

            except Exception as e: 
                # print(e)  # TODO: Should probably record that it's unextractable. 
                pass

    # This is the much easier case. Can just read in the entire directory.
    else: 
        parser_gen = execute_parser(parser, path)
        meta_dictionary["matio"][parser] = parser_gen

    meta_dictionary["container_version"] = os.environ['container_version']

    total_time = time.time() - t0
    meta_dictionary.update({"extract time": total_time})

    return meta_dictionary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='file path or file group to parse',
                        type=str, required=True)
    args = parser.parse_args()
    meta = extract_matio(args.path)

