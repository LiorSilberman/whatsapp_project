from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# options: using cookies to skip QR code scaning
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
    find_user = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    find_user.click()
    find_user.clear()
    find_user.send_keys(name)
    sleep(1)
    find_user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
    find_user.click()
    # sleep(2)
    
    # search image
    image_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div').click()
    image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(image)
    sleep(1)
    msg_box = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')
    
    # add message and send
    msg_box.send_keys(msg)
    

# send message only
def send_msg(name, msg):
    # find user contact
    find_user = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    find_user.click()
    find_user.send_keys(name)
    find_chat = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
    find_chat.click()
    # sleep(1)
    
    # # write message and send
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    msg_box.send_keys(msg)
    find_user.clear()

    
def main():
    
    # image
    image_to_send = "C:/Users/silbe/iCloudDrive/Computer_science/myProjects/mil.jpeg"
    # message
    message = 'write whatever you want to send'
    
    # read contacts list name by name
    with open("contacts.txt", encoding="utf8") as names_txt:
        names = [line.strip() for line in names_txt]
    names_txt.close()
    
    # iterate the contacts list and send messages
    for name in names:
        send_image_with_msg(name, image_to_send, message)
        
main()
