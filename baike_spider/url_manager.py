class UrlManager(object):
    def __init__(self):
        self.new_urls=set()#创建一个待爬取url列表
        self.old_urls=set()#创建一个已爬取url列表


    def add_new_url(self, url):#向管理器中添加1个URL
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:#既不在待爬取的url列表里，也不在已爬取的url列表里
            self.new_urls.add(url)#用来待爬取

    def add_new_urls(self, urls):#向管理器中添加批量个URL
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)#调用add_new_url进行单个添加

    def has_new_url(self):#判断管理器中是否有新的待爬取的URL
        return len(self.new_urls) !=0

    def get_new_url(self):#从管理器中获取一个新的待爬取的URL
        new_url=self.new_urls.pop()#pop方法：从列表中获取这个URL并移除
        self.old_urls.add(new_url)
        return new_url