# cutfiles

Cutting file tool.

### Installation

-  Run ``pip3 install cutfiles`` or alternatively download
   the tarball and run ``python3 setup.py install``


### Examples


- file: file path
- cut_size: file split size in bytes, default 100M
- out_dir: save file path
- return:None
```
from cutfiles.cutfiles import CutFiles

cf = CutFiles()
cf.cuttings(file="tourist_dict.pkl", cut_size=1024*1024, out_dir="/usr/local/data/")
```
