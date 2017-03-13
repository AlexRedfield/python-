# coding:utf8
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager
import urllib.parse
import urllib.request

class SpiderMain(object):#创建SpiderMain方法
    def __init__(self):
        self.urls=url_manager.UrlManager()                   #初始化启动url管理器
        self.downloader=html_downloader.HtmlDownloader()     #初始化启动下载器
        self.parser=html_parser.HtmlParser()                 #初始化启动解析器
        self.outputer=html_outputer.HtmlOutputer()           #初始化启动输入器

    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url)#把入口url添加进url管理器
        while self.urls.has_new_url():#如果有待爬取的url
            try:
                new_url=self.urls.get_new_url()#取一个出来
                print('craw %d : %s'%(count,new_url))#打印出取的url是第几个url
                html_cont=self.downloader.download(new_url)#下载对应的页面
                new_urls,new_data=self.parser.parse(new_url,html_cont)#下载好后，进行页面的解析，得到新的url和数据
                self.urls.add_new_urls(new_urls)#把新的url补充进url管理器
                self.outputer.collect_data(new_data)#进行数据的收集

                if count==1000:#爬取1000个页面
                    break

                count+=1
            except Exception as e:
                print(e)
                print('craw failed')


        self.outputer.output_html()#输出output收集下载好的数据


if __name__=='__main__':#编写main函数
    root_url='http://baike.baidu.com/link?url=EVK5YVkghv3Uqs0p6kcv8l86NyeMeFN73qmaEiHUb71zRUvO7QHEfE7rmgPj8x0h2OzMoQQzaC-PuwCjI3CCna'#设置入口url
    obj_spider=SpiderMain()#创建obj_spider
    obj_spider.craw(root_url)#调用spider的craw方法启动爬虫