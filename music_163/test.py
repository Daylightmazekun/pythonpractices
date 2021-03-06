#!/usr/bin/env python  
# encoding: utf-8  
# author: Glad Ma Zekun
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_ntes_nnid=7eced19b27ffae35dad3f8f2bf5885cd,1476521011210; _ntes_nuid=7eced19b27ffae35dad3f8f2bf5885cd; usertrack=c+5+hlgB7TgnsAmACnXtAg==; Province=025; City=025; NTES_PASSPORT=6n9ihXhbWKPi8yAqG.i2kETSCRa.ug06Txh8EMrrRsliVQXFV_orx5HffqhQjuGHkNQrLOIRLLotGohL9s10wcYSPiQfI2wiPacKlJ3nYAXgM; P_INFO=hourui93@163.com|1476523293|1|study|11&12|jis&1476511733&mail163#jis&320100#10#0#0|151889&0|g37_client_check&mailsettings&mail163&study&blog|hourui93@163.com; NTES_SESS=Fa2uk.YZsGoj59AgD6tRjTXGaJ8_1_4YvGfXUkS7C1NwtMe.tG1Vzr255TXM6yj2mKqTZzqFtoEKQrgewi9ZK60ylIqq5puaG6QIaNQ7EK5MTcRgHLOhqttDHfaI_vsBzB4bibfamzx1.fhlpqZh_FcnXUYQFw5F5KIBUmGJg7xdasvGf_EgfICWV; S_INFO=1476597594|1|0&80##|hourui93; NETEASE_AUTH_SOURCE=space; NETEASE_AUTH_USERNAME=hourui93; _ga=GA1.2.1405085820.1476521280; JSESSIONID-WYYY=cbd082d2ce2cffbcd5c085d8bf565a95aee3173ddbbb00bfa270950f93f1d8bb4cb55a56a4049fa8c828373f630c78f4a43d6c3d252c4c44f44b098a9434a7d8fc110670a6e1e9af992c78092936b1e19351435ecff76a181993780035547fa5241a5afb96e8c665182d0d5b911663281967d675ff2658015887a94b3ee1575fa1956a5a%3A1476607977016; _iuqxldmzr_=25; __utma=94650624.1038096298.1476521011.1476595468.1476606177.8; __utmb=94650624.20.10.1476606177; __utmc=94650624; __utmz=94650624.1476521011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.szjt.gov.cn/apts/APTSLine.aspx?LineGuid=52f67e87-dcb7-43ff-b632-e2a582c9f544&LineInfo=120(%E8%BD%A6%E5%9D%8A%E9%A6%96%E6%9C%AB%E7%AB%99=%3E%E8%BD%A6%E5%9D%8A%E9%A6%96%E6%9C%AB%E7%AB%99)',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def get_bus_station(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body

    #hot_artists = body.find_all('a', attrs={'t': 'msk'})
    #bus = body.find_all('a',attrs={'href': 'default.aspx?StandCode=EBW&StandName=新加花园东'})
    tables = body.find_all('table')
    bus_table = tables[0]
    for tr in bus_table.find_all('tr'):
        for td in tr.find_all('td'):
            print td.getText()

if __name__ == '__main__':
    url = 'http://www.szjt.gov.cn/apts/APTSLine.aspx?LineGuid=52f67e87-dcb7-43ff-b632-e2a582c9f544&LineInfo=120(%E8%BD%A6%E5%9D%8A%E9%A6%96%E6%9C%AB%E7%AB%99=%3E%E8%BD%A6%E5%9D%8A%E9%A6%96%E6%9C%AB%E7%AB%99)'
    get_bus_station(url)