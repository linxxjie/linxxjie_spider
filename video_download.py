import requests

headers = {
        'Cookie': 'your cookie',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    }

def getUrlList():
    print('开始获取视频地址...')
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


def getVideos(urlsList, path):
    index = 1
    for url in urlsList:
        try:
            print('开始下载第' + str(index) + '个视频')
            video = requests.get(url, headers=headers)
            with open(path + '/' + str(index) + '.mp4', 'wb') as f:
                f.write(video.content)
            if index == len(urlsList):
                print('下载完成')
            else:
                index += 1
        except:
            index += 1
            continue

if __name__ == '__main__':
    path = input(('请输入保存位置：'))
    getVideos(getUrlList(), path.replace('/', '\\'))
