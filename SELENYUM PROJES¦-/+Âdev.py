from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


 ################################# Kullanacağımız Tarayıcının Varsayılan ayarlarını Değiştirme Dİl Vb.. #####################
class GitHub:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    
    ######################## Ziyaret Etmek İstediğimiz sitenin URL'i ####################
    
    def singIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        
    ################## Kullanıcı Adı ve Şifre Bölümlerinin XPaht'leri
        
        usernameInput = self.browser.find_element_by_xpath("//*[@id='login_field']")
        usernameInput.send_keys(self.username)
        
        passwordInput = self.browser.find_element_by_xpath("//*[@id='password']")
        passwordInput.send_keys(self.password)
        btnSubmit = self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")
        btnSubmit.click()   
        time.sleep(2)

####################### Yazdığımız Fonksiyonu Çalıştırma Komutu ##############

twitter = GitHub(username,password)
twitter.singIn()