import glob
import os
from itertools import islice

non_ascii_percentage_for_infection = 0.05
txt_prefixes = ["", "txt", "xml", "html", "coli", "c"]

infected_files = []
warning_files = []
for j in range(1,4):

  for i in range(1,11):
    dir_name = f"data\\vol_{j}\\snapshot_{i}\\"
    list_of_files = filter( os.path.isfile, glob.glob(dir_name + '*') )

    for file_path in list_of_files:
      file_name = file_path.split('\\')[-1]
      prefix = ""
      if '.' in file_name:
        prefix = "".join(file_name.split('.')[1:])
      
      if prefix not in txt_prefixes:
        continue

      data = ""
      try:
        with open(file_path, "rb") as myfile:
          data = myfile.read()
      except:
        warning_files.append(f"{dir_name}{file_name}")
        continue

      char_count = 0
      non_ascii_count = 0
      for c in data:
        char_count+=1
        if not (0 <= c <= 127):
          non_ascii_count+=1
      
      if non_ascii_count / char_count > non_ascii_percentage_for_infection:
        infected_files.append(f"{dir_name}{file_name}")

f = open(f"infected_files.json", "w")
f.write(f"infected_files:\n\n")
for file in infected_files:
  f.write(f"{file}\n")

f.write(f"\n\n\nfiles that didn't open:\n\n")
for file in warning_files:
  f.write(f"{file}\n")

f.close()