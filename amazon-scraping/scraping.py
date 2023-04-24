from selenium import webdriver
from selenium.webdriver.common.by import By

book = {}

driver = webdriver.Chrome()
PATH = "https://www.amazon.com.br/gp/product/B06XWS4W4S?ref_=dbs_b_r_brws_rfy_recs_l_p1_4&storeType=ebooks"

driver.get(PATH)
book_title = driver.find_element(By.ID, 'productTitle')
book['title'] = book_title.text
print(book['title'])

book_price = driver.find_element(By.ID, 'kindle-price')
book['price'] = book_price.text
print(book['price'])

book_description = driver.find_element(By.XPATH, '//*[@id="bookDescription_feature_div"]/div/div[1]/span[2]')
book['description'] = book_description.text
print(book['description'])

book_pages = driver.find_element(By.XPATH, '//*[@id="rpi-attribute-book_details-ebook_pages"]/div[3]/span/a/span')
book['pages'] = book_pages.text
print(book['pages'])

book_idiom = driver.find_element(By.XPATH, '//*[@id="rpi-attribute-language"]/div[3]/span')
book['idiom'] = book_idiom.text
print(book['idiom'])

book_publishing = driver.find_element(By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[2]/span/span[2]')
book['publishing'] = book_publishing.text
print(book['publishing'])

book_author = driver.find_element(By.XPATH, '//*[@id="bylineInfo"]/span[1]/a')
book['author'] = book_author.text
print(book['author'])

book_gender = driver.find_element(By.XPATH, '//*[@id="detailBulletsWrapper_feature_div"]/ul[1]/li/span/ul/li[2]/span/a')
book['gender'] = book_gender.text
print(book['gender'])

driver.quit()
