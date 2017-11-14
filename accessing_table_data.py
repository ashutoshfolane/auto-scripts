from selenium import webdriver
import re

# driver = webdriver.PhantomJS('C:/Users/afolane/Documents/GitHub/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver = webdriver.Chrome('C://Users//afolane//Documents//GitHub//chromedriver.exe')
# driver.set_window_size(1120, 550)
driver.get('')
driver.find_element_by_xpath('').click()

table_body = driver.find_element_by_css_selector('')
rows = table_body.find_elements_by_tag_name('')
header = driver.find_element_by_css_selector('')
print('header:', header.text)
headers = [h.text for h in header.find_elements_by_tag_name('td')]

table_data = {}
for row_number, row in enumerate(rows):
    column_dict = {}
    columns = row.find_elements_by_tag_name('td')
    for column_number, column in enumerate(columns):
        # print('row#:', row_number, 'column#: ', column_number, column.text)
        column_dict[headers[column_number]] = column.text
        # column_dict[column_number] = column.text
    table_data[row_number] = column_dict
print(table_data)


# for x in table_data:
#     print(x)
#     for y in table_data[x]:
#         print(y, ':', table_data[x][y])

for row_number, row in table_data.items():
    if (row['Subject'] == 'Retention'):
        print("row#: ", row_number, "values: ", row['CaseId'])
        assert row['Subject'] == 'Retention'
        assert row['Queue'] == 'Retention - Customer Initiated'
        assert row['Flow Status'] == 'Closed - Account Cancelled'
        print(row['CaseId'])
