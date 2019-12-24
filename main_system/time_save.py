import csv
from pathlib import Path
import time,locale, calendar
import os
import re

'''def csv_write(data,name):
    with open("./flag/" + name + "time.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=['in_flag', 't1','login'])
        writer.writeheader()  
        writer.writerows(data)
        return []
'''
def csv_read(name):
    with open("./flag/" + name + "time.csv") as f:
        reader = csv.DictReader(f)
        data = list(reader)[0] 
    return data

def save(name):
    try:
        data = csv_read(name)
    except:
        data = []
        in_time = {"in_flag" : 0}
        data.append(in_time)
        #csv_write(data,name)
        with open("flag/" + name + "time.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=['in_flag', 't1','login'])
            writer.writeheader()
            writer.writerows(data)
        data = csv_read(name)
    flag = data["in_flag"]
    flag = int(flag)
        #flag = bool(flag)

    if flag == False:
        locale.setlocale(locale.LC_ALL, (None,None))
        now = time.ctime()
        t1 = time.time()
        cnvtime = time.strptime(now)
        login = time.strftime("%Y/%m/%d %H:%M", cnvtime)
        print(name + "さん、おはようございます")
        time.sleep(1)
        print("出社時間を記録します")
        time.sleep(2)
        print()
        print("出社時間 : " + login)
        print()
        data = []
        in_time = {"in_flag":1,"t1":t1,"login":login}
        data.append(in_time)
        #csv_write(data,name)
        with open("./flag/" + name + "time.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=['in_flag', 't1','login'])
            writer.writeheader()
            writer.writerows(data)

    elif flag == True:
            locale.setlocale(locale.LC_ALL, (None,None))
            data = csv_read(name)
            t1 = float(data['t1'])
            login = str(data["login"])
            now2 = time.ctime()
            t2 = time.time()
            cnvtime2 = time.strptime(now2)
            logout = time.strftime("%Y/%m/%d %H:%M", cnvtime2)
            total_time = (t2 - t1)/3600
            total_time = round(total_time,1)
            print(name + "さん、お疲れ様です")
            time.sleep(1)
            print("退社時間を記録します")
            time.sleep(2)
            print()
            print("退社時間 : " + logout)
            time.sleep(1)
            print("勤務時間 : " + str(total_time) + "時間")
            print()
            data = []
            in_time = {"in_flag":0,"t1":t1,"login":login}
            data.append(in_time)
            #csv_write(data,name)
            with open("./flag/" + name + "time.csv", "w") as f:
                writer = csv.DictWriter(f, fieldnames=['in_flag', 't1','login'])
                writer.writeheader()
                writer.writerows(data)
            total = []
            out_time = {"出社時間":login,"退社時間":logout, "勤務時間":str(total_time) + str("時間")}
            total.append(out_time)
            exists = Path("./出勤簿/" + name + "出勤簿.csv").exists()
            with open("./出勤簿/" + name + "出勤簿.csv","a" ,encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['出社時間', '退社時間','勤務時間'])
                if not exists:
                    writer.writeheader()  
                writer.writerows(total)
