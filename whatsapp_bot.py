from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pyperclip
from selenium.webdriver import ActionChains
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import openpyxl
import copy




# send image + message
def send_image_with_msg():
    names = contant_list()
    
    # message + image
    msg = pyperclip.copy(str(message.get()))
    image = str(image_input.get())
    
    for name in names:
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
        sleep(2)
        msg_box = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')
        
        # add message and send
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        # msg_box.send_keys(Keys.ENTER)
        sleep(2)

# send message only
def send_msg():
    names = contant_list()
    
    # message
    msg = pyperclip.copy(str(message.get()))
    
    for name in names:
        print(name)
        # find user contact
        find_user = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
        find_user.click()
        find_user.send_keys(name)
        sleep(2)
        find_chat = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
        find_chat.click()
        
        
        # write message and send
        msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
        
        act = ActionChains(driver)
        # act.key_down(keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        # msg_box.send_keys(Keys.ENTER)
        find_user.clear()
        sleep(2)


def open_whatsapp():
    global driver
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    

def switch():
    verify_button.config(state='disable')
    msg_button.config(state='normal')
    msg_image_button.config(state='normal')
    image_button.config(state='normal')

def browse():
    root.filename = filedialog.askopenfilename(initialdir="C:/", filetypes=(("png files", ".jpg"),("all files", "*.*")))
    image_input.set(str(root.filename))

def contant_list():
    # Define variable to load the dataframe
    dataframe = openpyxl.load_workbook("contacts.xlsx")
     
    # Define variable to read sheet
    dataframe1 = dataframe.active
    names = [dataframe1[row+1][0].value for row in range(1, dataframe1.max_row)]
    print(names)
    return names


#GUI
is_on = True
root= tk.Tk()
root.title("Whatsapp Bot")
root.iconbitmap('money.ico')
root.geometry("800x500")
root.resizable(height=False,width=False)

# font
label_font = 'Verdana 14 bold italic'
messege_font = 'Verdana 14 italic'

whatsapp_icon = PhotoImage(file = 'whatsapp1.png')
send_image = PhotoImage(file = 'send-message.png')
browse_icom = PhotoImage(file = 'search.png')

# whatsapp button
step1 = Label(root, text="1.",font=label_font, fg='green').place(relx=.05,y=130,anchor="center")
whatsapp_button = tk.Button(root,text='Open whatsapp: ', image=whatsapp_icon,font=label_font, command=open_whatsapp, borderwidth=0, compound = RIGHT)
whatsapp_button.place(relx=.22,y=130,anchor="center")

# verify whatsapp is ready
step2 = Label(root, text="2.",font=label_font, fg='green').place(relx=.05,y=180,anchor="center")
verify_button = tk.Button(root, text="Click when whatsapp is ready",font=label_font, command=switch, borderwidth=0.5)
verify_button.place(relx=.292,y=180,anchor="center")

# Message label
step3 = Label(root, text="3.", font=label_font, fg='green').place(relx=.05,y=240,anchor="center")
Label(root,text="Enter Message: ",font=label_font).place(x=50,y=250)
message=StringVar()
msg_Box = Entry(root,textvariable=message,font=messege_font,justify = RIGHT)
msg_Box.place(x=300,y=250)

# image label
image_button = Button(root, text="Browse ",state='disabled',image=browse_icom,font=label_font, command=browse, borderwidth=0, compound = RIGHT)
image_button.place(x=50, y=300)
image_input = StringVar()
imageBox = Entry(root,textvariable=image_input, font=messege_font)
imageBox.place(x=300, y=300)

# send buttons
step4 = Label(root, text="4.",font=label_font, fg='green').place(relx=.05,y=400,anchor="center")
msg_button = tk.Button(root,text="Send message", state='disable', image=send_image, command=send_msg, font=label_font, borderwidth=0, compound = RIGHT)
msg_button.place(relx=.2,y=400,anchor="center")
msg_image_button = tk.Button(root,text="Send message with image",state='disable', image=send_image, command=send_image_with_msg, font=label_font, borderwidth=0, compound = RIGHT)
msg_image_button.place(relx=.7,y=400,anchor="center")


root.mainloop()
