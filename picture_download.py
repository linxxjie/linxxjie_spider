import requests

# 获取图片链接
def getImageUrl(page, keyword):
    # 参数
    params = {
        "tn": "resultjson_com",
        "tn": "resultjson_com",
        "ipn": "rj",
        "ct": "201326592",
        "is": "0,0",
        "fp": "detail",
        "cl": "2",
        "lm": "-1",
        "ie": "utf - 8",
        "oe": "utf - 8",
        "adpicid": "0",
        "lpn": "0",
        "st": "-1",
        "word": keyword,
        "z": "0",
        "ic": "undefined",
        "s": "undefined",
        "se": "",
        "tab": "0",
        "width": "undefined",
        "height": "undefined",
        "face": "undefined",
        "istype":"0",
        "qc": "",
        "nc": "",
        "fr": "",
        "simics": "",
        "srctype": "",
        "bdtype": "0",
        "rpstart": "0",
        "rpnum": "0",
        "cs": "2529640483,1496420241",
        "catename": "",
        "cardserver": "",
        "tabname": "",
        "pn": "0",
        "rn": page*30,
        "gsm": "0",
        "1535072934907": ""
    }
    url = 'https://image.baidu.com/search/acjson'
    # 使用requests库爬取data中的数据
    r = requests.get(url, params=params).json().get('data')
    #从数据中获取图片url
    imgUrlsList = []
    for data in r:
        imgUrl = data.get('thumbURL')
        if(imgUrl != None):
            imgUrlsList.append(imgUrl)

    return imgUrlsList

# 图片下载
def downLoadImgs(urlsList, name, num, path):
    index = 1
    for i in urlsList:
        img = requests.get(i)
        print('正在下载第' + str(index) + '张图片')
        with open(path + '/name' + str(index) + '.jpg', 'wb') as f:
            f.write(img.content)
            if(index == num):
                print('下载完成')
                break
            else:
                index += 1

if __name__ == '__main__':
    # 用户输入
    title = input('请输入需要下载的图片名称:')
    num = input('请输入需要下载的图片数量:')
    path = input('请设置图片保存的位置:')
    # 计算页数
    page = int(num) // 30
    if int(num) % 30 != 0:
        page += 1

    urls = getImageUrl(page, title)
    downLoadImgs(urls, title, int(num), path.replace('/', '\\'))

