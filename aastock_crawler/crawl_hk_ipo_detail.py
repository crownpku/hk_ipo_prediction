#!/user/bin/env python
# coding:utf-8

import selenium
from selenium import webdriver
import pandas as pd

base_link = 'http://www.aastocks.com/tc/ipo/CompanySummary.aspx?view=1&Symbol='
phantomjs_path = '/home/guan/Software/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'



def crawl_target_link(code, ds, target_link, outfile):
    fail_count = 0
    while fail_count <= 5:
        try:
            ds.get(target_link)
            values = ds.find_elements_by_xpath('//td[@class="defaulttitle"]/following-sibling::td')
            strtmp = str(code)
            for value in values:
                value = value.text.strip('"').strip().replace('\n', ' ').replace('\r', '')
                strtmp += '\t' + value
            print strtmp
            print >> outfile, strtmp.strip().encode('utf-8')
            return
        except Exception as e:
            print e
            print 'Try ' + str(fail_count+1) + ' Time'
            continue
    



if __name__ == '__main__':
    df = pd.read_csv('../data/ipo_list', sep='\t', index_col='code')
    outfile = open('../data/ipo_details', 'w')
    ds = webdriver.PhantomJS(executable_path=phantomjs_path)
    ds.implicitly_wait(10)
    ds.set_page_load_timeout(10)
    ds.maximize_window()
    for code in df.index:
        print 'Crawling ' + str(code)
        target_link = base_link + str(code)
        crawl_target_link(code, ds, target_link, outfile)