import urllib
import urllib.request
import re

from collections import deque

queue=deque()
visited=set()

url='http://news.dbanotes.net'

queue.append(url)
cnt=0

while queue:
    url=queue.popleft()
    visited |={url}
    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    cnt += 1
    urlop = urllib.request.urlopen(url)
    if 'html' not in urlop.getheader('Content-Type'):
      continue

  # 避免程序异常中止, 用try..catch处理异常
    try:
      data = urlop.read().decode('utf-8')
    except:
      continue

  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
      if 'http' in x and x not in visited:
        queue.append(x)
        print('加入队列 --->  ' + x)






