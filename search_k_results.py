#こっちが新しい方の競走成績のcsv
TXT_FILE_DIR = "/volume_dir/boatrace/boat_data/results_txt/"

CSV_FILE_DIR = "/volume_dir/boatrace/results_csv/"

CSV_FILE_NAME = "results.csv"

#CSV_FILE_HEADER = "レースコード,日次,レース日,レース場,レース回,\
#着順,ポジション,登番,選手名,モータ,ボート,展示,進入,stタイム,raceタイム,type,weather,wind,wind_strong,wave\n"
CSV_FILE_HEADER = "race_code,date,race_date,place,round,\
order,position,number,name,motor,boat,display,in,st_time,race_time,type,weather,wind,wind_strong,wave\n"

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
            text_file.readline()
            text_file.readline()
            line = text_file.readline()
            day = line[3:7].replace(" ", "")
            date = line[17:27].replace(" ", "0")
            stadium = line[62:65].replace("\u3000", "")

        if re.search(r"H",contents):
            race_round_d = contents[2:5].replace(' ','')
            weather = contents[-23:-21].replace(" ", "").replace("　", "") #22
            wind  = contents[-17:-14].replace(" ", "").replace("　", "").replace('風','')
            wind_strong = contents[-12].replace(" ", "").replace('m', '').replace('　','').replace("波","").replace('波1','').strip()
            wave = contents[-4].replace(" ", "").replace('cm','').replace('　','').replace('波','').replace('m','').strip()
            line = text_file.readline()
            type = line[50:60].replace(' ','').replace('　','').strip()
            text_file.readline()
            line = text_file.readline()
            while line != "\n":
                rank = line[3] + ',' + line[6] + ',' + line[8:12].replace(' ','') + ',' + line[13:21].replace('\u3000','').replace(' ','') + ','\
                    +line[21:24].replace(' ','') + ',' + line[26:29].replace(' ','') + ',' +line[31:35].replace(' ','') + ',' + line[38] + ',' + line[43:47].replace(' ','') + ',' + line[52:58].replace(' ','') + ','\
                    +type+ ',' +weather+ ',' +wind+ ',' +wind_strong+ ',' +wave



                dict_stadium = {'桐生': 'KRY', '戸田': 'TDA', '江戸川': 'EDG', '平和島': 'HWJ',
                            '多摩川': 'TMG', '浜名湖': 'HMN', '蒲郡': 'GMG', '常滑': 'TKN',
                            '津': 'TSU', '三国': 'MKN', 'びわこ': 'BWK', '琵琶湖': 'BWK', '住之江': 'SME',
                            '尼崎': 'AMG', '鳴門': 'NRT', '丸亀': 'MRG', '児島': 'KJM',
                            '宮島': 'MYJ', '徳山': 'TKY', '下関': 'SMS', '若松': 'WKM',
                            '芦屋': 'ASY', '福岡': 'FKO', '唐津': 'KRT', '大村': 'OMR'
                            }
                race_round = contents[2:5].replace(' ','0')
                race_code = date[0:4] + date[5:7] + date[8:10] + dict_stadium[stadium] +\
                        race_round
    #着順,ポジション,登番,選手名,モータ,ボート,展示,進入,stタイム,raceタイム,type,weather,wind,wind_strong,wave,long\n"
                csv_file.write(race_code + "," + day + "," + date + "," + stadium + "," + race_round_d + ',' +\
                    rank + "\n")

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