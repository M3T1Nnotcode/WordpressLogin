from selenium import webdriver

#Wordpress giriş bilgileri
USERNAME = 'mm'
PASSWORD = '1234'

#Kullanılacak tarayıcı ve site
driver = webdriver.Firefox()
driver.get('https://site.com/wp-admin')


#Login Giriş
user_input = driver.find_element_by_id('user_login')
user_input.send_keys(USERNAME)

#Parola
password_input = driver.find_element_by_id('user_pass')
password_input.send_keys(PASSWORD)

#Butona basılması
login_button = driver.find_element_by_id('wp-submit')
login_button.click()
