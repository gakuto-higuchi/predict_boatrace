TEXT_FILE_DIR = "/volume_dir/boatrace/boat_data/timetable_txt/"

CSV_FILE_DIR = "/volume_dir/boatrace/timetable_csv/"
#YYYYMMDDには対象期間入れる
CSV_FILE_NAME = "timetable.csv"
"""
win_p 全国勝率
win_p_2 全国2連率
a_win_p 当地勝率
potision 艇番
"""
CSV_FILE_HEADER = "race_code,title,date,place,round,\
race_name,position,number,name,age,area,weight,class,win_p,win_p_2,\
a_win_p,a_win_p_2,motor,motor_p_2,boat,boat_p_2\n"

import os
import re
from tqdm import tqdm
def get_data(text_file):
    csv_file = open(CSV_FILE_DIR + CSV_FILE_NAME, "a", encoding="utf-8")

    for contents in text_file:

        trans_asc = str.maketrans('１２３４５６７８９０Ｒ：　', '1234567890R: ')

        if re.search(r"番組表", contents):

            text_file .readline()

            line = text_file.readline()
            title = line[:-1].strip() # title

            text_file.readline()

            line = text_file.readline()
            day = line[3:7].translate(trans_asc).replace(' ', '').replace(r'[第日]','')
            date = line[17:28].translate(trans_asc).replace(' ', '0')
            stadium = line[52:55].replace("\u3000", "") # place

        if re.search(r"電話投票締切予定", contents):
            line = contents

            if re.search(r"進入固定", line):
                line = line.replace('進入固定 Ｈ', '進入固定     Ｈ')

            race_round = line[0:3].translate(trans_asc).replace(' ', '0')
            race_name = line[5:21].replace(' ', '').replace("\u3000", "") # race_name

            text_file.readline()
            text_file.readline()
            text_file.readline()
            text_file.readline()

            line = text_file.readline()

            while line != "\n":
# line[:16]16までで体重までスキャンしている
                if re.search(r"END", line):
                    break
                racer_data = line[0] + "," + line[2:6] + "," + line[6:10].replace("\u3000","")\
                    + "," + line[10:12] + "," + line[12:14] + "," + line[14:16]\
                    + "," + line[16:18] + "," + line[19:23] + "," + line[24:29] + "," + line[30:34] \
                    + "," + line[35:40] + "," + line[41:43] + "," + line[44:49] \
                    + "," + line[50:52] + "," + line[53:58]
                dict_stadium = {'桐生': 'KRY', '戸田': 'TDA', '江戸川': 'EDG', '平和島': 'HWJ',
                            '多摩川': 'TMG', '浜名湖': 'HMN', '蒲郡': 'GMG', '常滑': 'TKN',
                            '津': 'TSU', '三国': 'MKN', 'びわこ': 'BWK', '琵琶湖': 'BWK', '住之江': 'SME',
                            '尼崎': 'AMG', '鳴門': 'NRT', '丸亀': 'MRG', '児島': 'KJM',
                            '宮島': 'MYJ', '徳山': 'TKY', '下関': 'SMS', '若松': 'WKM',
                            '芦屋': 'ASY', '福岡': 'FKO', '唐津': 'KRT', '大村': 'OMR'
                            }
                race_code = date[0:4] + date[5:7] + date[8:10] + dict_stadium[stadium] +\
                        race_round[0:2] + "R"

                csv_file.write(race_code + "," + title + "," + day + "," + stadium + "," + race_round
                        + "," + race_name + "," + racer_data + "\n")
                line = text_file.readline()
    csv_file.close()


print("作業を開始します。")

os.makedirs(CSV_FILE_DIR, exist_ok = True)

csv_file = open(CSV_FILE_DIR + CSV_FILE_NAME, "w", encoding='utf-8')
csv_file.write(CSV_FILE_HEADER)
csv_file.close()

text_file_list = os.listdir(TEXT_FILE_DIR)

for text_file_name in tqdm(text_file_list):

    if re.search(".TXT", text_file_name):
        text_file = open(TEXT_FILE_DIR + text_file_name, "r", encoding = "shift_jis")
        get_data(text_file)

print(CSV_FILE_DIR + CSV_FILE_NAME + "を作成しました。")

print("作業を終了しました。")