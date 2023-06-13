import time
from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.tokopedia.com/search?st=product&q=hijab'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

data = []
for i in range(5): 
     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zeus-root")))
     time.sleep(2)
     
     for j in range (23):
          driver.execute_script("window.scrollBy(0, 250);")
          time.sleep(1)
     
     driver.execute_script("window.scrollBy(50, 0)")
     time.sleep(1)
     soup = BeautifulSoup(driver.page_source, 'html.parser')

     for item in soup.findAll('a', class_= 'pcv3__info-content'):
          nama_produk = item.find(class_= 'prd_link-product-name').text
          harga_produk = item.find(class_= 'prd_link-product-price').text
          penilaian = item.find(class_='prd_rating-average-text')
          rating = penilaian.text if penilaian else '0'
        #   total_penjualan = item.find(class_='prd_label-integrity').text
          total_penjualan_elem = item.find(class_='prd_label-integrity')
          total_penjualan = total_penjualan_elem.text if total_penjualan_elem else '0'
          
          data.append(
               (nama_produk, harga_produk, rating, total_penjualan)
          )
     df = pd.DataFrame(data, columns=['Nama Produk', 'Harga Produk', 'Penilaian', 'Total Penjualan'])
     print (df)
     

     df.to_csv('datascrapinghijab.csv', index = False)
     print('Data Telah Tersimpan')            

driver.close()