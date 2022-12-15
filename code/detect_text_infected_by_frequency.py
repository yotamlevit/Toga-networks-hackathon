import glob
import os
from itertools import islice


frequency_diff_precentage_from_avarage = 0.15
txt_prefixes = ["", "txt", "xml", "html", "coli", "c"]

files = {}
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
        files[f"{dir_name}{file_name}"] = 50
        continue

      char_count = {}
      counter = 0
      for c in data:
        counter += 1
        if c not in char_count:
          char_count[c] = 1
        else:
          char_count[c] += 1
      
      avg = counter / len(char_count.keys())
      
      precentage = 50
      for v in char_count.values():
        min_avg = avg - (avg * frequency_diff_precentage_from_avarage)
        max_avg = avg + (avg * frequency_diff_precentage_from_avarage)
        if not(min_avg <= v <= max_avg):
          precentage -= 5
        else:
          precentage += 1
      
      files[f"{dir_name}{file_name}"] = precentage


min_p = 0
max_p = 0
for p in files.values():
  if p < min_p:
    min_p = p
  elif p > max_p:
    max_p = p

max_p = max_p + abs(min_p)


f = open(f"infected_text_files_by_frequency_result.json", "w")
f.write("{\n")
for file, p in files.items():
  f.write(f"\t\"{file}\": {int(((p+abs(min_p)) / max_p) * 100)},\n")

f.write("}")
f.close()