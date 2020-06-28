#https://price.btcfans.com/
import requests
import os
from lxml import etree
max=10000;min=4000;sendemail="0";info=''
url='https://price.btcfans.com/'
html = etree.HTML(requests.get(url).text)
price = float(html.xpath('//li[@id="coin-bitcoin"]//span[@class="last-price"]/text()')[0].replace(',',''))
if (price>max):
    sendemail="1"
    info="The current bitcoin price is ${0}, it is recommended to sell".format(price)
if (price<min):
    sendemail="1"
    info="The current bitcoin price is ${0}, it is recommended to buy".format(price)
os.environ['SENDMAIL']=sendemail
os.environ['INFO']=info
