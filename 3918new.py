from flask import Flask, request, abort

import requests

import re


import pymysql


count = 0
for i in range(50):
    inputlist = input('請優雅的輸入UN:')
    if inputlist.isdigit():
        headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"}
        res = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vTfHqhAoeOGajlma3K7Ym1CngD2VI3ua99fwPc767QpExzAMyV81S6L1IZ6TwzSPLO2irkZt96QA-3h/pubhtml", headers=headers)
        DG = re.findall('</div></th><td class="s0" dir="ltr">(.*?)</td><td class=', res.content.decode('utf-8'), re.S)
        SH = re.findall('td class="s0 softmerge" dir="ltr"><div class="softmerge-inner" style="width: 27px; left: -1px;">(.*?)</div></td><td class="s4" dir="ltr">', res.content.decode('utf-8'), re.S)
        EMS = re.findall('</div></td><td class="s4" dir="ltr">.*?</td><td class="s0" dir="ltr">(.*?)</td><td', res.content.decode('utf-8'), re.S)
        SS = re.findall('px;">QQQ(.*?)AAA</div>', res.content.decode('utf-8'), re.S)
        DG.remove('un_no')
        SS.remove('stowage_and_segregation')
        for D in range(0,2853):
            if inputlist == DG[D]:
                    print(DG[D])
                    print ("這是"+SH[D]+",ems為"+EMS[D])
                    print (SS[D])
                    count += 1
        if count == 10:
            print("你查了10次，感覺有點累了")
        elif count == 50:
            print("猛！爆！你查了50次，求求你休息一下，至少重開程式去喝個水")
        else:
            continue
    elif inputlist.isdigit() is not True and len(inputlist) == 9:
        try:
            a,b = inputlist.split(",")
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"}
            res = requests.get(
                "https://docs.google.com/spreadsheets/d/e/2PACX-1vTfHqhAoeOGajlma3K7Ym1CngD2VI3ua99fwPc767QpExzAMyV81S6L1IZ6TwzSPLO2irkZt96QA-3h/pubhtml",
                headers=headers)
            unno = re.findall('</div></td><td class="s4" dir="ltr">(.*?)</td><td class=', res.content.decode('utf-8'), re.S)
            DG = re.findall('</div></th><td class="s0" dir="ltr">(.*?)</td><td class=', res.content.decode('utf-8'),
                            re.S)
            SS = re.findall('px;">QQQ(.*?)AAA</div>', res.content.decode('utf-8'), re.S)
            DG.remove('un_no')
            SS.remove('stowage_and_segregation')
            for R in range(0,2853):
                if a == DG[R]:
                    first = unno[R]
                    index1 = SS[R]
            for K in range(0,2853):
                if b == DG[K]:
                    second = unno[K]
                    index2 = SS[K]
            print(first,second,index1,index2)



            db = pymysql.connect(host='db4free.org', port=3306, user='billdarkest', passwd='darkest17', db='billdarkest')

            # 使用cursor()方法得到操作指標
            cursor = db.cursor()

            # SQL 語法
            sql = "SELECT LEVEL FROM dg where classA = '%s' and classB = '%s'"%(first,second)
            cursor.execute(sql)
            slevel = cursor.fetchone()  # 用一個變數來接受fetchall（）查詢所有這個函式返回的值。10
            slevel = str(slevel).strip('(,)')

            if slevel == "'X'" or "'1'":

                if "SG36" in index1 and "SG35" in index2 or "SG35" in index1 and "SG36" in index2: #先做酸檢判定
                    print("(2)","注意!查詢內容已幫你完成酸鹼隔離判定")
                elif "SG25" in index1 and ("3" or "2.1") in second:  #好亂!!這是25判定
                    if "SG26" in index1 and ("2.1" or "3") in second:
                        print("(2)", "注意!查詢內容已幫你完成SG25判定...等等我還偵測到SG26:甲板上須隔2個櫃位")
                    elif "SG26" in index2 and ("2.1" or "3") in first:
                        print("(2)", "注意!查詢內容已幫你完成SG25判定...等等我還偵測到SG26:甲板上須隔2個櫃位")
                    else:
                        print("(2)", "注意!查詢內容已幫你完成SG25判定")

                elif "SG25" in index2 and ("2.1" or "3") in first:  #超亂!!這是第二次25判定
                    if "SG26" in index1 and ("2.1" or "3") in second:
                        print("(2)", "注意!查詢內容已幫你完成SG25判定...等等我還偵測到SG26:甲板上須隔2個櫃位")
                    elif "SG26" in index2 and ("2.1" or "3") in first:
                        print("(2)", "注意!查詢內容已幫你完成SG25判定...等等我還偵測到SG26:甲板上須隔2個櫃位")
                    else:
                        print("(2)", "注意!查詢內容已幫你完成SG25判定")

                elif "SG38" in index2 and "SGG2" in index1:   #SG38 ammonium 感謝Kevin老闆提醒
                    print("(2)", "注意!查詢內容已幫你完成SG38判定")
                elif "SG38" in index1 and "SGG2" in index2:
                    print("(2)", "注意!查詢內容已幫你完成SG38判定")
                elif "SG39" in index1 and "SGG2" in index2 and "1444" not in (first or second):  #SG39判定,1444例外
                    print("(2)", "注意!查詢內容已幫你完成SG39判定")
                elif "SG39" in index2 and "SGG2" in index1 and "1444" not in (first or second):
                    print("(2)", "注意!查詢內容已幫你完成SG39判定")
                else:
                    print(slevel)
            else:
                print(slevel)
        except NameError:
            print("有這UN number?")
    else:
        print("你打錯了嗎")

