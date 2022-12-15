import json

results = {}
with open("result.json", 'r') as result_handler:
    results = json.loads(result_handler.read())

volumues = {
    "vol_1": {},
    "vol_2": {},
    "vol_3": {}
}


for file, score in results.items():
    if score < 75:
        continue

    file_paths = file.split('\\')
    if file_paths[3] not in volumues[file_paths[1]]:
        volumues[file_paths[1]][file_paths[3]] = file_paths[2]


for vol, files in volumues.items():

    with open(f"Volume  {vol}", "w") as sub:
        volume_number = vol.split('_')[1]
        sub.write(f"File name   Infected at\n")

        for file, snap_num in files.items():
            sub.write(f"{file}  {snap_num}\n")