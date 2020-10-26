# cutfiles
<br />
Cutting file tool.

### Installation
<br />
*Run ``pip3 install cutfiles`` or alternatively download the tarball and run ``python3 setup.py install``*


### Examples
<br />

*file: file path
<br />
cut_size: file split size in bytes, default 100M
<br />
out_dir: save file path
<br />
return:None*
<br />
```
from cutfiles.cutfiles import CutFiles

cf = CutFiles()
cf.cuttings(file="tourist_dict.pkl", cut_size=1024*1024, out_dir="/usr/local/data/")
```
