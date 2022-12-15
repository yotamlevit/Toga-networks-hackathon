import glob
import os
import json

""" sample
{
filename: {snapshot_nam: {size: size, prefix: prefix, hash: hash}}
}
"""

for j in range(1,4):
  files = {}

  for i in range(1,11):
    dir_name = f"vol_{j}\\snapshot_{i}\\"
    list_of_files = filter( os.path.isfile, glob.glob(dir_name + '*') )
    
    files_with_size = [ (file_path, os.stat(file_path).	st_size) for file_path in list_of_files ]
    
    for file_path, file_size in files_with_size:
      file_name = file_path.split('\\')[-1]
      name = file_name
      prefix = ""
      if '.' in file_name:
        name = file_name.split('.')[0]
        prefix = "".join(file_name.split('.')[1:])
        
      if name not in files:
        files[name] = {f"snapshot_{i}": {"size": file_size, "prefix": prefix}}  
      else:
        last_record = list(files[name].values())[-1]
        if last_record["size"] != file_size or last_record["prefix"] != prefix:
          files[name][f"snapshot_{i}"] = {"size": file_size, "prefix": prefix}


  f = open(f"vol_{j}_files_stages.json", "w")
  f.write("{\n")
  for k, v in files.items():
    if len(v) == 1 and "snapshot_1" in v:
      continue

    f.write(f"\t\"{k}\":\n")
    f.write("\t\t{\n")
    for sk, sv in v.items():
      f.write(f"\t\t\t{json.dumps({sk:sv})},\n")
    f.write("\t\t}\n")
  f.write("}\n")
  f.close()
