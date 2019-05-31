#!/bin/env python3
import re
import os
import gzip
#import ssl
import urllib.request
from datetime import datetime

'''os.environ['https_proxy'] = '***.***.**.**:**'
os.environ['http_proxy'] = '***.***.**.**:**'
proxy = urllib.request.ProxyHandler({
    'http': '***.***.**.**:**',
    'https': '***.***.**.**:**'
}) '''

CVE_DB_PATH = './cve'

def download_xml_nvd():
    url = "https://nvd.nist.gov/vuln/data-feeds"
    #opener = urllib.request.build_opener(proxy)
    #urllib.request.install_opener(opener)
    #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #page = urllib.request.urlopen(url, context = gcontext)
    page = urllib.request.urlopen(url)
    html = page.read()
    linkregex = re.compile('https://nvd.nist.gov/feeds/xml/cve/2.0/nvdcve-2.0-20\d+.xml.gz')
    db_links = linkregex.findall(str(html))
    for link in db_links:
        #filedb = urllib.request.urlopen(link, context = gcontext).read()
        filedb = urllib.request.urlopen(link).read()
        re_link = re.compile('/2.0/' + 'nvdcve-2.0-20\d+.xml.gz')
        re_path = re_link.search(link)
        db_name = re.sub(r'/2.0/', '', re_path.group())
        urllib.request.urlretrieve(link, os.path.join(CVE_DB_PATH, db_name))


def download_json_nvd():
    url = "https://nvd.nist.gov/vuln/data-feeds"
    #opener = urllib.request.build_opener(proxy)
    #urllib.request.install_opener(opener)
    #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #page = urllib.request.urlopen(url, context = gcontext)
    page = urllib.request.urlopen(url)
    html = page.read()
    linkregex = re.compile('https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-20\d+.json.gz')
    db_links = linkregex.findall(str(html))
    for link in db_links:
        #filedb = urllib.request.urlopen(link, context = gcontext).read()
        filedb = urllib.request.urlopen(link).read()
        re_link = re.compile('/1.0/' + 'nvdcve-1.0-20\d+.json.gz')
        re_path = re_link.search(link)
        db_name = re.sub(r'/1.0/', '', re_path.group())
        urllib.request.urlretrieve(link, os.path.join(CVE_DB_PATH, db_name))

def download_bdu():
    url = "http://bdu.fstec.ru/documents/files/vullist.xlsx"
    #opener = urllib.request.build_opener(proxy)
    #urllib.request.install_opener(opener)
    #gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #filedb = urllib.request.urlopen(url, context = gcontext).read()
    filedb = urllib.request.urlopen(url).read()
    db_name = ''.join(["fstec-", datetime.now().strftime("%d-%m-%Y"), ".xlsx"])
    urllib.request.urlretrieve(url, os.path.join(CVE_DB_PATH, db_name))

def main():
    if os.path.exists(CVE_DB_PATH):
        for f in os.listdir(CVE_DB_PATH):
            os.remove(CVE_DB_PATH + '/' + f)
    else:
        os.mkdir(CVE_DB_PATH)
 
if __name__ == '__main__':
    main()