from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import time

# settings
driver = webdriver.Chrome()
url_magalu = 'https://www.magazineluiza.com.br/'
driver.get(url_magalu)
product = 'Motor Endodôntico Endopen Wireless - Schuster'

# search product
input_product = driver.find_element_by_id('input-search')
time.sleep(3)
input_product.send_keys(product)
time.sleep(3)
input_product.submit()
time.sleep(3)

# get product and copy price
bt_product = driver.find_element_by_xpath(
    '//*[@id="__next"]/div/main/section[4]/div[3]/div/ul/li[2]/a/div[2]/img')
time.sleep(5)
bt_product.click()
time.sleep(4)
price = driver.find_element_by_css_selector(
    '#__next > div > main > section:nth-child(6) > div.sc-brSvTw.ftYRnC > div > div > div > p').text
time.sleep(4)
parcel_price = driver.find_element_by_css_selector(
    '#__next > div > main > section:nth-child(6) > div:nth-child(5) > section > div > div:nth-child(2) > p.sc-hKwDye.hGyLnp.sc-jWUzzU.jXgGHC').text

# copy details
seller = driver.find_element_by_css_selector(
    '#__next > div > main > section:nth-child(6) > div.sc-brSvTw.bdNWMD > div.sc-jRQBWg.bBRmdK > p:nth-child(1) > label').text
time.sleep(4)

# send email
sender = 'seuemailt@outlook.com'
receivers = ['destinatario@hotmail.com']
# smtp
smtpHost = 'smtp.office365.com'
smtpPort = 587
password = "Password"
subject = "Confira o preco do Motor Endodontico hoje na Magalu!"
# Add the From: and To: headers at the start!
message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
           % (sender, ", ".join(receivers), subject))
message += f"Na Magazine, o valor do Motor Endodontico hoje e {price} e voce pode pagar em {parcel_price}. \n\nProduto vendido por {seller}. \n\nSeu link para compra https://www.magazineluiza.com.br/motor-endodontico-endopen-wireless-schuster/p/jcagk04jb3/cp/itmo/"

smtpObj = smtplib.SMTP(smtpHost, smtpPort)
# smtpObj.set_debuglevel(1)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(sender, password)
smtpObj.sendmail(sender, receivers, message)
smtpObj.quit()

print(".............................")
print("bot finalizado com sucesso!!!")
print(".............................")
