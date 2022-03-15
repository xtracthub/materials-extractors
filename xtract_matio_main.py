
import os
import sys
import time
import argparse
from materials_io.utils.interface import run_all_parsers_on_group, get_available_parsers



def extract_matio(paths):

    # CSV omitted because cannot pass in anything. 
    parsers=['crystal', 'csv', 'ase', 'dft', 'image', 'tdb']
    """Runs a file through MaterialsIO parsers.

    Parameter:
    paths (list(str): List of paths of files to parse.

    Return:
    meta_dictionary (dict): Dictionary of all metadata extracted using
    MaterialsIO parsers.
    """

    # This helps us handle the Xtract-case. 
    if type(paths) == str:
        paths = [paths]

    all_mdata = []

    path_sizes = dict()
    # for path in paths: 

    #for parser in parsers:
    t0 = time.time()
    # meta_dictionary = {"matio": {}, "parser": pars}
    
    for path in paths:
        if not os.path.isfile(path):
            return {'error': f'file {path} does not exist'}
        

    meta_dictionary = dict()

    meta_dictionary['debug'] = paths

    # print(get_available_parsers().keys())

    # print(f"Parsers: {parsers}") 

    for par in parsers:
        # print(f"Now executing parser...{par}")
        ta = time.time()
        gen_dump = []
        # parser_gen = execute_parser(parser, paths) # List index error from this line.
        try:
            if par == 'ase':
                if os.path.getsize(path) <= 32:
                    # continue
                    gen_dump.append({'error': 'file too small to process', 'extract_time': time.time()-ta})
                    meta_dictionary[par] = gen_dump 
                    #meta_dictionary['extraction_time'] = time.time() - ta
                    continue

            
            parser_gen = run_all_parsers_on_group(group=paths, adapter_map="match", include_parsers=[par])
            # print(parser_gen)
            for item in parser_gen:
                gen_dump.append({'mdata': item, 'extract_time': time.time() - ta})
            # print(f"Item for {par}: {item}")
        except Exception as e:
            gen_dump.append({'error': 'Unable to execute parser on group', 'parser': par, 'extract_time': time.time()-ta})
        
        meta_dictionary[par] = gen_dump

    t1 = time.time()
    meta_dictionary['extraction_time'] = t1-t0

    meta_dictionary["CONTAINER_VERSION"] = os.environ['CONTAINER_VERSION']

    total_time = time.time() - t0
    meta_dictionary.update({"time": total_time})

    return meta_dictionary


def execute_extractor(paths, debug=False):

    if not debug:
        # Need this to shush pycalphad
        f = open('/dev/null', 'w')
        sys.stdout = f



    mdata = extract_matio(paths)
    return mdata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--paths', nargs='+', help='list of files to parse',
                        type=str, required=True)
    parser.add_argument('--parser', type=str, required=False)
    # print(get_available_parsers().keys())
    args = parser.parse_args()
    meta = execute_extractor(args.paths, debug=False)

    # sys.stdout = t

    print(meta)
