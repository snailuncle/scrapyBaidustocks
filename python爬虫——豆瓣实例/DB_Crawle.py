#DB_Crawle.py
import re,urllib.request,urllib.parse
import time 
from DouBan_Lei import novel_b
from DouBan_Lei import Downloader
from DouBan_Lei import DiskCache


def get(html):
	# 解码网页内容
	html=html.decode('utf-8')
    # 匹配特殊网址
	pattern_a=re.compile('(https://book.douban.com/subject/[\d]{7,8}/|/tag/小说\?start=[\d]{2,3}&amp;type=T)')
	#print(pattern_a.findall(html))
    # 返回找到的所有符合正则的URL
	return(pattern_a.findall(html))


def crawl(seed_url,regex,max_depth=1,novel_a=None,cache=None):
	base_url=seed_url
	crawl_queue=[seed_url]
	over_url={seed_url:0}
	D=Downloader(cache)
	start=time.time()
	while crawl_queue:
		links_url=crawl_queue.pop()
		depth=over_url[links_url]
		
		html=D(links_url)
		#print('1')
		if html: 	#如果网页是不存在的网页，则不进行下去
			if novel_a:
				novel_a(links_url,html)
			if depth!=max_depth:
				for link  in get(html):
					if re.search(regex,link):
					
						a=urllib.parse.urljoin(base_url,link)
					
						if a not in over_url:
							over_url[a]=depth+1
							crawl_queue.append(a)
	end=time.time()
	
	print('爬取所花时间%s秒' % (end-start))	
	return(over_url)						
	
			

				
if __name__=='__main__':
	crawl('https://book.douban.com/tag/小说','/(subject|tag)',max_depth=3,novel_a=novel_b(),cache=DiskCache())
	