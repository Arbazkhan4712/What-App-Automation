from selenium import webdriver
from time import sleep

#get the driver for individual browser
driver = webdriver.Chrome() # add the path to chrome driver 

#scan the QR code
print("Scan the QR code")
driver.get("https://web.whatsapp.com/")

#send message function
def Sendmsg():

    #enter name of receiver
    name = input("Enter the name of user or group : ")
    #enter the message
    msg = input("Enter the message : ")
    #enter the count
    count = int(input("Enter Number of count : "))

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpaths('//*[@id="main"]/footer/div[1]/div[3]')
        button.click()

#send image or video file function
def sendimgvid():
    #enter name of receiver
    name = input("Enter the name of user or group : ")
    #enter file path
    filepath = input("Enter the file path (Image,Video) : ")

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()

    imgvid_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    imgvid_box.send_keys(filepath)

    sleep(3)

    send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
    send_button.click()

#user input
print("Press 1 for sending multiple messages \nPress 2 to send an image or video \n Press 3  to exit")
n = int(input())
if (n == 1):
    Sendmsg()

elif(n == 2):
    sendimgvid()

elif(n==3):
    quit()
