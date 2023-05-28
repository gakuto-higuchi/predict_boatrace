LZH_FILE_DIR = "/volume_dir/boatrace/boat_data/timetable_lzh/"

TEXT_FILE_DIR = "/volume_dir/boatrace/boat_data/timetable_txt/"

import lhafile
import os
import re
print("作業を開始します。")
os.makedirs(TEXT_FILE_DIR, exist_ok=True)
lzh_file_list = os.listdir(LZH_FILE_DIR)

for lzh_file_name in lzh_file_list:

    if re.search(".lzh",lzh_file_name):

        file = lhafile.Lhafile(LZH_FILE_DIR + lzh_file_name)

        info = file.infolist()
        file_name = info[0].filename

        f = open(TEXT_FILE_DIR + file_name, "wb")
        f.write(file.read(file_name))
        f.close

        print(TEXT_FILE_DIR + lzh_file_name + "を解凍しました。")

print("作業を終了しました。")