# import asyncio
# from bilibili_api import video,Credential

# SESSDATA = ""
# BILI_JCT = ""
# BUVID3 = ""

# async def main():
#     # 实例化 Credential 类
#     credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUVID3)
#     # 实例化 Video 类
#     v = video.Video(bvid="BV1544y1e77G", credential=credential)
#     # 获取视频信息
#     info = v.get_info()
#     # 打印视频信息
#     print(info)
#     # 给视频点赞
#     # await v.like(True)

# if __name__ == '__main__':
#     # 主入口
#     asyncio.get_event_loop().run_until_complete(main())

from bilibili_api import sync, video

v = video.Video('BV15f4y1M7qm')

dms = sync(v.get_danmakus(0))
print(len(dms))
# for dm in dms:
#     print(dm)