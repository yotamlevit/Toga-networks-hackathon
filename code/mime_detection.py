import magic
import os
import json
import mimetypes
import pathlib


root_dir = os.getcwd()
root_dir = root_dir.replace('\\', '/')
root_dir += '/data'

magic.MAGIC_CHECK
mime = magic.Magic(mime=True)
file_detections = {}

for dirname in os.listdir(root_dir):
    dir_path = root_dir + f'/{dirname}'

    for snapshot in os.listdir(dir_path):
        snapshot_dir = dir_path + f'/{snapshot}'

        for filename in os.listdir(snapshot_dir):
            filetype = pathlib.Path(filename).suffix
            mimetype = mimetypes.types_map.get(filetype)
            if mimetype:
                content_mime_type = mime.from_file(f'{snapshot_dir}/{filename}')
                if content_mime_type != 'text/plain' and mimetype != 'text/plain' and 'cannot open' not in content_mime_type:
                    file_detections[f'{snapshot_dir}/{filename}'] = 100 if content_mime_type != mimetype else 0
                else:
                    file_detections[f'{snapshot_dir}/{filename}'] = 0
            else:
                file_detections[f'{snapshot_dir}/{filename}'] = 0



with open("infected_files_by_mime_type_result.json", 'w') as f:
    f.write(json.dumps(file_detections))