#!/usr/bin/env python  
# encoding: utf-8  
# author: Glad Ma Zekun
'''
get search result from baidu top 5(max)
'''
import pyperclip, sys, requests, bs4, webbrowser


def main():
    if len(sys.argv) > 1:
        keyword = ' '.join(sys.argv[1:])
    else:
        keyword = pyperclip.paste()

    res = requests.get('http://google.com/search?q=' + keyword)
    res.raise_for_status()  # throw exception
    print res.text
    soup = bs4.BeautifulSoup(res.text)
    linkelems = soup.select('.r a')
    numopen = min(5, len(linkelems))
    for i in range(numopen):
        webbrowser.open('http://google.com' + linkelems[i].get('href'))

if __name__ == "__main__":
    main()