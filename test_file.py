
import xtract_matio_main 


parser = 'dft'

basepath = '/Users/tylerskluzacek/Desktop/matio-data/'

all_items = [f'{basepath}INCAR', f'{basepath}OUTCAR', f'{basepath}POSCAR']

mdata = xtract_matio_main.extract_matio(all_items, parser)

print(mdata)

