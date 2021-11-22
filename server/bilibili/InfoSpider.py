from bs4 import BeautifulSoup
import re
from bs4.element import Script
import requests
import json
import datetime
# 视频信息爬虫

headers = {
    "cookie": "buvid3=7BAF3F51-80C7-4A07-AFC1-178C175A1F9D53950infoc; LIVE_BUVID=AUTO2715820713588762; rpdid=|(u))uuRm)Jl0J'ul)kRYuYm|; blackside_state=1; _uuid=E9A99A3D-6222-A977-0429-654A9987DFB723266infoc; buvid_fp=7BAF3F51-80C7-4A07-AFC1-178C175A1F9D53950infoc; CURRENT_QUALITY=80; fingerprint=ce9d251e9a59d1a46c62a6dd41ac8aa8; buvid_fp_plain=7BAF3F51-80C7-4A07-AFC1-178C175A1F9D53950infoc; SESSDATA=4b96168c%2C1648198971%2C8a41d%2A91; bili_jct=ade772c8ae27ec2cf4a2ed2a9068d1c2; DedeUserID=168036077; DedeUserID__ckMd5=de5e5aeec9be9769; sid=ci78nq0y; CURRENT_FNVAL=976; bp_video_offset_168036077=579782870861588529; bp_t_offset_168036077=579782870861588529; innersign=1; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f; PVID=1",
    "origin": "https://www.bilibili.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

find_click_num = re.compile(r'<span.*?title="总播放数(\d*)">')
find_dm_num = re.compile(r'<span.*?title="历史累计弹幕数(\d*)">')
find_initial_state = re.compile(r'<script>window.__INITIAL_STATE__=(.*)</script>')
find_video_data = re.compile(r'{(.*)};')
api_url = "https://api.bilibili.com/x/player/pagelist?bvid="

# 根据视频bv号获取视频的cid
def getVideoCid(bv):
    get_cid_url = api_url+bv
    result = requests.get(get_cid_url, headers=headers)
    get_json = result.json()
    info_data = get_json['data'][0]
    return info_data['cid']

def getVideoInfo(bv):
    video_info = {}
    infoUrl = "https://www.bilibili.com/video/" + str(bv)
    response = requests.get(infoUrl, headers=headers)
    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    scripts = str(soup.find_all('script'))
    initial_info = re.findall(find_initial_state,scripts)[0]
    after_info = re.findall(find_video_data,initial_info)[0]
    after_info =json.loads('{'+str(after_info)+'}')
    data_info = after_info['videoData']
    video_info['bv_id'] = data_info['bvid']
    video_info['cid'] = data_info['cid']
    video_info['tag'] = data_info['tname']
    video_info['title'] = data_info['title']
    date = datetime.datetime.utcfromtimestamp(data_info['pubdate']).strftime("%Y-%m-%d %H:%M:%S")
    video_info['pub_date'] = date
    video_info['description'] = data_info['desc']
    video_info['owner'] = data_info['owner']
    video_info['link'] = 'https://www.bilibili.com/video/'+bv
    video_info['stat'] = data_info['stat']
    print(video_info)
    return video_info
