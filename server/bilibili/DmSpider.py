import os.path
from bs4 import BeautifulSoup
import re
import requests
import time
import datetime
import pandas as pd
import jieba
from bilibili import InfoSpider


headers = {
    "cookie": "buvid3=7BAF3F51-80C7-4A07-AFC1-178C175A1F9D53950infoc; LIVE_BUVID=AUTO2715820713588762; rpdid=|(u))uuRm)Jl0J'ul)kRYuYm|; blackside_state=1; _uuid=E9A99A3D-6222-A977-0429-654A9987DFB723266infoc; buvid_fp=7BAF3F51-80C7-4A07-AFC1-178C175A1F9D53950infoc; CURRENT_QUALITY=80; fingerprint=ce9d251e9a59d1a46c62a6dd41ac8aa8; buvid_fp_plain=7BAF3F51-80C7-4A07-AFC1-178C175A1F9D53950infoc; SESSDATA=4b96168c,1648198971,8a41d*91; bili_jct=ade772c8ae27ec2cf4a2ed2a9068d1c2; DedeUserID=168036077; DedeUserID__ckMd5=de5e5aeec9be9769; sid=ci78nq0y; CURRENT_FNVAL=976; video_page_version=v_old_home_10; bp_video_offset_168036077=588884967412435748; PVID=1; bp_t_offset_168036077=591767805296310276; innersign=1",
    "origin": "https://www.bilibili.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
dm_url = 'https://comment.bilibili.com/'
history_dm_Url = "https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&"+"oid="

api_url = "https://api.bilibili.com/x/player/pagelist?bvid="
savePath = '.\\bilibili\\source\\'

def get_dm_limit(bv):
     time_nature = []
     comments = []
     cid = InfoSpider.getVideoCid(bv)
     url = dm_url+str(cid)+'.xml'
     request = requests.get(url,headers=headers)
     request.encoding = 'utf-8'
     soup = BeautifulSoup(request.text,'lxml')
     results = soup.find_all('d')
     for t in results:
         time_nature.append(t.attrs['p'])
         comments.append(t.text)
         print(t.attrs['p'])
         print(t.text)
     df = pd.DataFrame()
     df['Time_Attribute'] = time_nature
     df['Comments'] = comments
     df.to_excel(bv+'.xls')

def get_time_list(start):
    time_list = []
    date_list = pd.date_range(start, datetime.datetime.now(), freq='D')
    for item in date_list:
        item = str(item).split(" ")[0]
        time_list.append(item)
    return time_list


# # 爬取弹幕
def get_dm_history(bv):
    # 爬取数据并且返回必要的dm信息 Dm_Info:{date_info:{date_list:[],date_count:[]}}
    Dm_Info = {
        'date_info':{
            'date_list':[],
            'date_count':[]
        }
    }
    path = savePath + bv + "\\"
    if not os.path.exists(path):
        os.mkdir(path)
    video_info = InfoSpider.getVideoInfo(bv)
    baseUrl = history_dm_Url+str(video_info['cid'])+"&date="
    time_list = get_time_list(video_info['pub_date'])
    Dm_Info['date_info']['date_list'] = time_list
    for item in time_list:
        url = baseUrl + item
        date_path = path+'\\'+str(item)+".txt"
        # 已经爬取过的则不再爬取
        if os.path.exists(date_path):
            with open(date_path,'r',encoding='utf-8') as f:
                temp_list = f.readlines()
                Dm_Info['date_info']['date_count'].append(len(temp_list))
            continue
        response = requests.get(url, headers=headers, verify=False)
        html = response.text
        # print(html)
        data_list = re.findall('.*?([\u4e00-\u9fa5]+\s*).*', html)
        # 将当天的弹幕数据量封装传入返回对象中
        Dm_Info['date_info']['date_count'].append(len(data_list))
        time.sleep(3)
        with open(date_path, mode='a', encoding='utf-8') as f:
            for index in data_list:
                f.write(index)
                f.write('\n')
    return Dm_Info

# def main():
#     bv = 'BV1N34y1d7av'
#     dm_info = get_dm(bv)
#     print(dm_info)
#     # get_dms(bv)

# if __name__ == '__main__':
#     main()