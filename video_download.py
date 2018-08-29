import requests

headers = {
        'Cookie': 'SSOLoginState=1535502849; ALF=1538094849; _T_WM=310acc7dfc5518de6472fedf65d99659; MLOGIN=0; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D3%2526q%253D%25E6%259E%2597%25E5%25B0%258F%25E5%25B0%258F%25E6%259D%25B0%2526t%253D0%26from%3Dpage_100306%26oid%3D4272857673906973%26fid%3D1005052487801744%26uicode%3D10000011',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    }

def getUrlList():
    page = 1
    url = 'https://m.weibo.cn/api/container/getIndex'
    urlsList = []
    while True:
        params = {
            'uid' : '1594052081',
            'luicode': '10000011',
            'lfid': '100103type=1&q=朱一龙',
            'type': 'uid',
            'value': '1594052081',
            'containerid': '1076031594052081',
            'page': page
        }
        weiboList  = requests.get(url, params=params, headers=headers).json().get('data').get('cards')
        if weiboList == [] :
            break
        else:
            for weibo in weiboList:
                mblog = weibo.get('mblog')
                if mblog != None and "page_info" in mblog:
                    media = mblog.get('page_info').get('media_info')
                    if media != None and "stream_url" in media:
                        urlsList.append(media.get('stream_url'))
                    else:
                        continue
                elif mblog != None and "retweeted_status" in mblog:
                    media = mblog.get('retweeted_status').get('page_info')
                    if media:
                        media = media.get('media_info')
                        if media != None and "stream_url" in media:
                            urlsList.append(media.get('stream_url'))
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
        page += 1
    return urlsList


def getVideos(urlsList):
    index = 1
    for url in urlsList:
        try:
            print('开始下载第' + str(index) + '个视频')
            video = requests.get(url, headers=headers)
            with open('E:/spider/video/' + str(index) + '.mp4', 'wb') as f:
                f.write(video.content)
            if index == len(urlsList):
                print('下载完成')
            else:
                index += 1
        except:
            index += 1
            continue

if __name__ == '__main__':
    getVideos(getUrlList())
