#!/user/bin/env python
# coding:utf-8

import selenium
from selenium import webdriver

start_link = 'http://www.aastocks.com/tc/ipo/ListedIPO.aspx'
phantomjs_path = '/home/guan/Software/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'

def get_sotcks_info(ds, outfile):
    stocks = ds.find_elements_by_xpath('//tr[@class="DR" or @class="ADR"]')
    for stock in stocks:
        strtmp = ''
        for element in stock.find_elements_by_xpath('.//td'):
            strtmp += '\t' + element.text.strip('"').strip()
        print strtmp
        print >> outfile, strtmp.strip().encode('utf-8')
    return 0

def crawl_hk_ipo():
    outfile = open('../data/ipo_list', 'w')
    header = 'date' + '\t' + 'code' + '\t' + 'name' + '\t' + 'category' + '\t' + 'ipo_price' + '\t' + 'buy_ratio' + '\t' + 'one_hand' + '\t' + 'draw_prob' + '\t' + 'firstday_performance' + '\t' + 'now_price' + '\t' + 'total_performance'
    print >> outfile, header.encode('utf-8')
    ds = webdriver.PhantomJS(executable_path=phantomjs_path)
    ds.implicitly_wait(10)
    ds.set_page_load_timeout(10)
    ds.maximize_window()
    crawl_finish = 0
    ds.get(start_link)

    while crawl_finish == 0:
    	cur_page_num = str(ds.find_element_by_xpath('//div[@class="paging_cur"]').text)
        cur_page_num = int(cur_page_num)
        print 'Crawling page ' + str(cur_page_num)
        get_sotcks_info(ds, outfile)
       
        try:
            cur_page_num += 1
            next_page_button = ds.find_element_by_xpath('//a[@href="javascript:searchPage('+ str(cur_page_num) + ')"]')
            next_page_button.click()
        except Exception as e:
            #print str(e)
            print 'Crawling Finished!'
            crawl_finish = 1

    return  0

if __name__ == '__main__':
    crawl_hk_ipo()
