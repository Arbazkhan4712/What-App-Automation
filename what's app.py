from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('C:/Users/HACKER47/Downloads/chromedriver.exe')
print("Scan the QR code")
driver.get("https://web.whatsapp.com/")

def Sendmsg():
    name = input("Enter the name of user or group : ")
    msg = input("Enter the message : ")
    count = int(input("Enter Number of count : "))

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name("_3u328")

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name("_3M-N-")
        button.click()

def sendimgvid():
    name = input("Enter the name of user or group : ")
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

print("Press 1 for sending multiple messages \nPress 2 to send an image or video \nPress  to exit")
n = int(input())
if (n == 1):
    Sendmsg()

elif(n == 2):
    sendimgvid()

elif(n==3):
    quit()

