'''
获取豆瓣评分电影信息列表查询 For python3
'''
import urllib,json
from urllib import request



def douban_url(type='movie',tag='热门',sort='rank',pag_limit='20',page_start='0'):
    '''
    获取豆瓣评分电影信息列表
    @param:
        type --分类：movie、
        tag --标签：热门
        sort --排序方式：rank
        pag_limit --每一页限制查询数量:20
        page_start --起始页编号:0
    @returns:
        None --无结果
        返回查询结果列表
    '''
    d={
        'type':type,
        'tag':tag,
        'sort':sort,
        'pag_limit':pag_limit,
        'page_start':page_start
    }
    postData=urllib.parse.urlencode(d)
    
    url_douban='https://movie.douban.com/j/search_subjects?'
    #构建一个完整的url，示例： 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&pag_limit=20&page_start=0'
    urlSearch=url_douban+postData
    data=getHtml(urlSearch)

    #debug 模式打印数据长度
    print(len(data))
    return data


def getHtml(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers)
    
    
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        return None 
    return response.read()
    
    
def main():
    for page in range(0,100):
        data=douban_url(pag_limit='200', page_start=str(page))
        data=data.decode('utf-8')
        if not data:
            break
        jsonRes=json.loads(data)['subjects']
        
        print(len(jsonRes))
        for val in jsonRes:
            print(val['title'])
            print(' 评分',val['rate'])
            print(' 地址',val['url'])
            if val['playable']:
                print(' 可播放')
            else:
                print(' 不可播放')
    
if __name__ == '__main__':
    main()