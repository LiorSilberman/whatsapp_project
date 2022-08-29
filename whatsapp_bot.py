from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:/Users/silbe/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.get('https://web.whatsapp.com/')
driver.maximize_window()

# continue only when whatsapp is ready
ask = input("whatsapp is ready? ")


# send image + message
def send_image_with_msg(name, image, msg):

    # find user contact
    find_user = driver.find_element(By.XPATH, '//div[@title = "תיבת טקסט להזנת החיפוש"]')
    find_user.click()
    find_user.send_keys(name + Keys.ENTER)
    
    # search image
    driver.find_element_by_xpath('//div[@title = "הוספת קובץ"]').click()
    image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(image)
    sleep(1)
    msg_box = driver.find_element(By.XPATH, '//div[@data-testid = "media-caption-input-container"]')
    find_user.clear()
    
    # add message and send
    msg_box.send_keys(msg + Keys.ENTER)


# send message only
def send_msg(name, msg):
    # find user contact
    find_user = driver.find_element(By.XPATH, '//div[@title = "תיבת טקסט להזנת החיפוש"]')
    find_user.click()
    find_user.send_keys(name + Keys.ENTER)

    # write message and send
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msg_box.send_keys(msg + Keys.ENTER)



def main():
    # read contacts list name by name
    with open("users.txt", encoding="utf8") as names_txt:
        names = []
        for name in names_txt:
            names.append(name)
    names_txt.close
    
    # image
    image_to_send = "add path to image here"
    
    # message
    message = 'write whatever you want to send'
    
    # iterate the contacts list and send messages
    for name in names:
        send_msg(name, message)
        sleep(4)

main()