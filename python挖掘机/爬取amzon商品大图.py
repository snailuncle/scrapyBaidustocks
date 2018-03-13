import requests
from lxml import etree 
import re
url="https://www.amazon.com/LEGO-Holiday-Easter-Building-Piece/dp/B06VT7QZQ4/ref=zg_bs_toys-and-games_home_1?_encoding=UTF8&psc=1&refRID=8EQKVHKJJ8SGTQN8T98Q"
r=requests.get(url)
r.raise_for_status()
html=etree.HTML(r.text)
# print(r.text)
picture_script=html.xpath("//*[@id='imageBlock_feature_div']/script/text()")[0]
picture_script_str=str(picture_script)
# print(picture_script_str)
pat=re.compile('(?<=hiRes":")http[^"]+')
matchObj = pat.findall(picture_script_str)
# print(matchObj)
for link in matchObj:
    print(link)
