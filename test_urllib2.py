
import urllib2
url="http://www.baidu.com"
print("第一种方法")
response1=urllib2.urlopen(url)
print(response1.getcode())
print (len(response1.read()))