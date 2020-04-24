import time
import argparse
from materials_io.utils.interface import get_available_parsers, get_parser, run_all_parsers_on_group

import os

def extract_matio(paths, parser):
    """Runs a file through all available MaterialsIO parsers.
    Parameter:
    path (str): File path of file to parse.
    Return:
    meta_dictionary (dict): Dictionary of all metadata extracted using
    MaterialsIO parsers.
    """

    #single_file_ls = ['crystal', 'ase', 'image', 'csv', 'electron_microscopy', 'electron']

    # if parser in single_file_ls:
    #     single_file = True
    # else:
    #     single_file= False

    t0 = time.time()
    meta_dictionary = {"matio": {}, "parser": parser}

    # file_list = os.listdir(path)
    # This only exists here to get rid of that dang 'hidden' Macbook file in every dir by default... 
    # without_ds = []
    # for f in file_list:
    #     if not f.startswith('.DS'):
    #         full_path = os.path.join(path, f)
    #         without_ds.append(full_path)
    
    # If single, file then get metadata from each file in the directory (/group)
    # if single_file:
    #if parser in single_file_ls: 
        #path = paths[0]  # Not clean, but easy way of getting one file as string :) 
    #    meta_dictionary["matio"]["files"] = []
    #    # for path in paths:  # TODO: why are we iterating through something 1 item long?

    #    #fact_list = []
    #    #for filen in paths:
    #    #    if os.path.isfile(filen):
    #    #        fact_list.append(True)
    #    #    else:
    #    #        fact_list.append(False)

    #    # return fact_list
    #    try: 
    #        # parser_gen = execute_parser(parser, path)  # TODO
    #        gen_dump = []
    #        # return paths
    #        parser_gen = run_all_parsers_on_group(group=paths, adapter_map='match', include_parsers=['ase'])

    #        for item in parser_gen:
    #            gen_dump.append(item)

    #        meta_dictionary["matio"]["files"].append({parser : gen_dump})

    #    except Exception as e: 
    #        pass

    # This is the much easier case. Can just read in the entire directory.
    if 'a'=='a':
        # return "We made it here!"
        meta_dictionary['debug'] = paths

        try:
            gen_dump = []
            # parser_gen = execute_parser(parser, paths) # List index error from this line.
            parser_gen = run_all_parsers_on_group(group=paths, adapter_map='match', include_parsers=[parser])
            
            for item in parser_gen:
                gen_dump.append(item)
            
            meta_dictionary["matio"] = gen_dump

        except Exception as e: 
            return e
            meta_dictionary['error1'] = f"THE LIST ERROR WAS HERE: {e}"


    meta_dictionary["container_version"] = os.environ['container_version']

    total_time = time.time() - t0
    meta_dictionary.update({"extract time": total_time})

    return meta_dictionary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--paths', help='list of files to parse',
                        type=str, required=True)
    parser.add_argument('--parser', type=str, required=True)
    args = parser.parse_args()
    meta = extract_matio(args.paths, args.parser)
    print(meta)
    # for item in meta:
    #    print(item)

