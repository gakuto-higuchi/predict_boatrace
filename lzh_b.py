#%%
"""
START_DATE = "2016-04-01"
END_DATE = "2023-03-01"
"""
START_DATE = "2023-01-23"
END_DATE = "2023-03-01"
SAVE_DIR = "/volume_dir/boatrace/boat_data/timetable_lzh/"

INTERVAL= 2

FIXED_URL = "https://www1.mbrace.or.jp/od2/B/"
#%%
from datetime import datetime as dt
from datetime import timedelta as td
from requests import get
from os import makedirs
from time import sleep
#%%
print("作業を開始します。")

makedirs(SAVE_DIR, exist_ok=True)

start_date = dt.strptime(START_DATE, "%Y-%m-%d")
end_date = dt.strptime(END_DATE, "%Y-%m-%d")

days_num = (end_date - start_date).days + 1

date_list = []

for d in range(days_num):
    target_date = start_date + td(days=d)

    date_list.append(target_date.strftime("%Y%m%d"))

for date in date_list:
    yyyymm = date[0:4] + date[4:6]
    yymmdd = date[2:4] + date[4:6] + date[6:8]

    variable_url = FIXED_URL + yyyymm + "/b" + yymmdd + ".lzh"
    file_name = "b" + yymmdd + ".lzh"

    r = get(variable_url)

    if r.status_code == 200:
        f = open(SAVE_DIR + file_name, "wb")
        f.write(r.content)
        f.close()
        print(variable_url + "をダウンロードしました。")

    else:
        print(variable_url + "をダウンロードに失敗しました。")

    sleep(INTERVAL)

print("作業を終了しました。")
