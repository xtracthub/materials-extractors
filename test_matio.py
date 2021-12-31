
from xtract_sdk.packagers.family import Family
from xtract_sdk.packagers.family_batch import FamilyBatch

import os

def create_mock_event(files, parser=None):
    mock_event = dict()

    fam_batch = FamilyBatch()

    test_fam_1 = Family()
    group_file_objs = []

    for file in files:
        #test_fam_1 = Family()
        base_path = file
        group_file_objs.append({'path': base_path, 'metadata': dict()})
        test_fam_1.download_type = "LOCAL"
    
    test_fam_1.add_group(files=group_file_objs, parser=parser)
    fam_batch.add_family(test_fam_1)

    mock_event['family_batch'] = fam_batch
    return mock_event


def base_extractor(event):
    import json
    from xtract_sdk.agent.xtract import XtractAgent

    # Load endpoint configuration. Init the XtractAgent.
    xtra = XtractAgent(ep_name=event['ep_name'],
                       xtract_dir=event['xtract_dir'],
                       sys_path_add=event['sys_path_add'],
                       module_path=event['module_path'],
                       recursion_depth=event['recursion_limit'],
                       metadata_write_path=event['metadata_write_path'])

    # Execute the extractor on our family_batch.
    xtra.execute_extractions(family_batch=event['family_batch'], input_type=event['type'])

    # All metadata are held in XtractAgent's memory. Flush to disk!
    paths = xtra.flush_metadata_to_files(writer=event['writer'])
    stats = xtra.get_completion_stats()
    stats['mdata_paths'] = paths

    return stats

base_dir = "/home/tskluzac/.xtract/.test_files/matio-data"
event = create_mock_event([os.path.join(base_dir, 'INCAR'), 
                           os.path.join(base_dir, 'OUTCAR'),
                           os.path.join(base_dir, 'POSCAR')], parser='dft')
event['ep_name'] = 'foobar'
event['xtract_dir'] = "/home/tskluzac/.xtract"
event['module_path'] = "xtract_matio_main"
event['sys_path_add'] = "/"
event['metadata_write_path'] = "/home/tskluzac/mdata"
event['recursion_limit'] = 5000
event['type'] = str
event['writer'] = 'json-np'
base_extractor(event)
