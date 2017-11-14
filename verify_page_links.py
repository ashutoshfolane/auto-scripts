from selenium import webdriver
import requests

driver = webdriver.Chrome('C://Users//afolane//Documents//GitHub//chromedriver.exe')

driver.get('http://only-testing-blog.blogspot.in/2013/09/testing.html')

try:
total_links = driver.find_elements_by_tag_name('a')
print('Links for status codes which are NOT 200: ')
for link in total_links:
link_name = link.text
link_url = link.get_attribute('href')
if link_url is not None:
if 'https:' in link_url:
r = requests.head(link_url)
url_status_code = r.status_code
if url_status_code is not 200:
print('Link name: {}, :Link url:{}, Status Code: {}'.format(link_name, link_url, url_status_code))

except requests.ConnectionError:
print("failed to connect")

