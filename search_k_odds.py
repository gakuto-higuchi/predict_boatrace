TXT_FILE_DIR = "/volume_dir/boatrace/boat_data/results_txt/"

CSV_FILE_DIR = "/volume_dir/boatrace/odds_csv/"

CSV_FILE_NAME = "odds.csv"
CSV_FILE_HEADER = "race_code,p_3,p_3_m,p_3_d,\
p_3_d_m,p_2,p_2_m,p_2_d,p_2_d_m\n"
import re
import os
from tqdm import tqdm
print("作業を開始します。")
os.makedirs(CSV_FILE_DIR, exist_ok=True)

csv_file = open(CSV_FILE_DIR + CSV_FILE_NAME, "w", encoding="utf-8")
csv_file.write(CSV_FILE_HEADER)
csv_file.close()

def get_data(text_file):
    csv_file = open(CSV_FILE_DIR + CSV_FILE_NAME, "a", encoding="utf-8")

    for contents in text_file:
        if re.search(r"競走成績",contents):
            text_file.readline()

            line = text_file.readline()
            title = line[:-1].strip()

            text_file.readline()
            line = text_file.readline()
            day = line[3:7].replace(" ", "")
            date = line[17:27].replace(" ", "0")
            stadium = line[62:65].replace("\u3000", "")

        if re.search(r"払戻金", contents):

            line = text_file.readline()

            while line != "\n":
                results =\
                    line[15:20] + "," + line[21:28].strip() + ","\
                    +line[32:37] + "," + line[38:45].strip() + ","\
                    +line[49:52] + "," + line[53:60].strip() + ","\
                    +line[64:67] + "," + line[68:75].strip()


                dict_stadium = {'桐生': 'KRY', '戸田': 'TDA', '江戸川': 'EDG', '平和島': 'HWJ',
                            '多摩川': 'TMG', '浜名湖': 'HMN', '蒲郡': 'GMG', '常滑': 'TKN',
                            '津': 'TSU', '三国': 'MKN', 'びわこ': 'BWK', '琵琶湖': 'BWK', '住之江': 'SME',
                            '尼崎': 'AMG', '鳴門': 'NRT', '丸亀': 'MRG', '児島': 'KJM',
                            '宮島': 'MYJ', '徳山': 'TKY', '下関': 'SMS', '若松': 'WKM',
                            '芦屋': 'ASY', '福岡': 'FKO', '唐津': 'KRT', '大村': 'OMR'
                            }
                race_round = line[10:12].replace(' ','0')
                race_code = date[0:4] + date[5:7] + date[8:10] + dict_stadium[stadium] +\
                        race_round[0:2]
                csv_file.write(race_code + "," + results + "\n")

                line = text_file.readline()

    csv_file.close()

text_file_list = os.listdir(TXT_FILE_DIR)

for txt_file_name in tqdm(text_file_list):
    if re.search(".TXT", txt_file_name):
        text_file = open(TXT_FILE_DIR + txt_file_name, "r", encoding="shift_jis")

        get_data(text_file)

        text_file.close()

print(CSV_FILE_DIR + CSV_FILE_NAME + "を作成しました。")

print("作業を終了しました。")