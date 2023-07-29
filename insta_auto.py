from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from moviepy.editor import *
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests
import random
from csv import DictReader
import datetime

# ----------------------validating program is running today or not----------------------------

with open("./log.txt",'r')as f:
    for date in f:
        if date==f'{str(datetime.date.today())}\n':
            print("Instagram shorts video is already uploaded today.")
            exit()

print("Program is running...")

browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# browser=webdriver.Firefox() this code is working prefectly with but some errors
# then i used upper layer of code for this you have to install:- pip install webdriver-manager

browser_for_shorts_download=browser

# -----if insta_reels_url.csv has link then not open instagram again for url
# -----as soon as we download instagram video we will delete one by one url------------------
all_url=[]
with open("./insta_reels_url_file.csv",'r')as f:
    reader = DictReader(f)
    for row in reader:
        insta_reels_url=row['url']
        all_url.append(insta_reels_url)
        
if len(all_url)>0:
    print("found all")
else:

    browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(10)
    # 
    # 
    def get_cookie_here(file):
        with open(file, 'r') as f:
            reader = DictReader(f)
            for row in reader:
                time.sleep(0.5)
                browser.add_cookie(dict(row))
            f.close()
    # 
    # 
    get_cookie_here("./instagram_cookie.csv")
    # 
    # 
    browser.refresh()
    time.sleep(10)
    elem = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(3)
    ele= browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[3]/span/div/a/div').click()
    time.sleep(6)
    ele=browser.find_element(By.XPATH,'/html/body').send_keys(Keys.END)
    time.sleep(6)
    ele=browser.find_element(By.XPATH,'/html/body').send_keys(Keys.END)
    time.sleep(6)
    ele=browser.find_element(By.XPATH,'/html/body').send_keys(Keys.END)
    time.sleep(4)
    # 
    # 
    # 
    # 
    all_code=browser.page_source
    # print(all_code)
    # 
    # ------------------------------code is working here prefectly
    # 
    # print(type(all_code))
    time.sleep(3)
    with open("./insta_sorce.html", "w", encoding="utf-8") as f:
        f.write(all_code)
    # 
    # browser.close()
    # 
    time.sleep(3)
    # --------------------------code is workin till here prefectly
    # 
    # 
    # 
    # -----------------------now work of beautyfull shoup------------------
    # 
    from bs4 import BeautifulSoup
    # 
    with open("./insta_sorce.html", encoding="utf8") as f:
        content=f.read()
    soup = BeautifulSoup(content, "html.parser")
    # 
    all_Links=[]
    for link in soup.find_all('a', href=True):
        all_Links.append(link['href'])
    # 
    target_content=[]
    for link in all_Links:
        if link.startswith("/p/"):
            target_content.append(link)
    # 
    print(target_content)
    # 
    with open("./insta_reels_url_file.csv", "a") as f:
        for link in target_content:
            f.write(link+"\n")
    # 



# # # -----------------------now download insta video from link --------------------


save_insta_url=[]

with open("./insta_reels_url_file.csv",'r')as f:
    reader = DictReader(f)
    for row in reader:
        insta_url=row['url']
        save_insta_url.append(insta_url)

downloaded_video=[]
for file in os.listdir("./insta_Shorts/"):
        if file.endswith(".mp4"):
            downloaded_video.append(file)

if len(downloaded_video) > 0:
    print ("video already downloaded")
else:
    
    browser_for_shorts_download.get('https://sssinstagram.com/')
    time.sleep(5)
    down=browser_for_shorts_download.find_element(By.XPATH,'//*[@id="main_page_text"]').click()
    time.sleep(1)
    # -----------final downloadable link is here-----------
    downoadable_link =[]
    for reel in save_insta_url:
        try:
            time.sleep(2)
            down=browser_for_shorts_download.find_element(By.XPATH,'//*[@id="main_page_text"]').send_keys(Keys.CONTROL+"A",Keys.BACKSPACE)
            time.sleep(2)
            down=browser_for_shorts_download.find_element(By.XPATH,'//*[@id="main_page_text"]').send_keys("https://www.instagram.com"+reel)
            time.sleep(3)
            down=browser_for_shorts_download.find_element(By.XPATH,'//*[@id="submit"]').click()
            time.sleep(30)
            down=browser_for_shorts_download.find_element(By.XPATH,'//*[@id="response"]/div[1]/div/div/a')
            time.sleep(8)
            downoadable_link.append(down.get_attribute('href'))
            time.sleep(5)
            # print(downoadable_link)
            print(len(downoadable_link))
            time.sleep(3)
            browser_for_shorts_download.delete_all_cookies()
            time.sleep(1)
            browser_for_shorts_download.refresh()
            time.sleep(4)
        except:
            print("error")  

    # browser_for_shorts_download.close()   



    # # ----------------------------------video download code---------------
    print("----------now video is downloading started---------------")

    for link in downoadable_link:
        video_name=random.randrange(990, 2000)
        video_name=str(video_name)
    
        # URL='https://media-flow.net/get?__sig=2feXG0wQB15zy_DKmbNGOA&__expires=1690372661&uri=https%3A%2F%2Fscontent-iev1-1.cdninstagram.com%2Fo1%2Fv%2Ft16%2Ff1%2Fm82%2F2840B61B4A390DD6D8AA967A181BB59E_video_dashinit.mp4%3Fefg%3DeyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uNzIwLmNsaXBzLmJhc2VsaW5lIn0%26_nc_ht%3Dscontent-iev1-1.cdninstagram.com%26_nc_cat%3D110%26vs%3D934289527644690_1888155743%26_nc_vs%3DHBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC8yODQwQjYxQjRBMzkwREQ2RDhBQTk2N0ExODFCQjU5RV92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVABgkR0ROMzZSTnQ2RjVhT2dBQkFDMmEzQTY3T3BrVmJwUjFBQUFGFQICyAEAKAAYABsAFQAAJu68q96mlPJAFQIoAkMzLBdAMW7ZFocrAhgSZGFzaF9iYXNlbGluZV8xX3YxEQB1%252FgcA%26_nc_rid%3D7c8f3bf989%26ccb%3D9-4%26oh%3D00_AfCcm1ihCgy6-B6DxvwxurQ6ugCCeXbFxHmKdE9Q5Nn4jw%26oe%3D64C2A06D%26_nc_sid%3D2999b8%26dl%3D1&filename=......%E0%A4%85%E0%A4%AA%E0%A4%A8%E0%A5%87%20%E0%A4%AA%E0%A4%B8%E0%A4%82%E0%A4%A6%E0%A5%80%E0%A4%A6%E0%A4%BE%20%E0%A4%AA%E0%A4%B0%E0%A4%BF%E0%A4%B5%E0%A4%BE%E0%A4%B0%20%E0%A4%95%E0%A5%87%20%E0%A4%B8%E0%A4%A6%E0%A4%B8%E0%A5%8D%E0%A4%AF%20%20%20comment%20%E0%A4%95%E0%A5%80%E0%A4%9C%E0%A4%BF%E0%A4%AF%E0%A5%87%20%23brands%20%23family%20%23marketing%20%23%E0%A4%AE%E0%A5%8B%E0%A4%9F%E0%A5%80%E0%A4%B5%E0%A5%87%E0%A4%B6%E0%A4%A8%E0%A4%B2%20%20%23%E0%A4%B9%E0%A4%BF%E0%A4%82%E0%A4%A6%E0%A5%80%20%23%E0%A4%B8%E0%A5%80%E0%A4%96%20%23%E0%A4%B0%E0%A4%BE%E0%A4%AE%20%23%E0%A4%B5%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AA%E0%A4%BE%E0%A4%B0%20%23motivationalquotes%20%23lifequotes%20%23lifequotes%20%23sell%20%23buy%20%23divinity%20%23answers%20%23%E0%A4%85%E0%A4%B5%E0%A4%A7%20%23%E0%A4%93%E0%A4%9D%E0%A4%BE%20%23%E0%A4%B8%E0%A4%B0%20%23awadh%20%23avadh%20%23ojha%20%23sir%20%23wisdom%20%23success%20%23entrepreneurship%20%23hustle.mp4&ua=-&referer=https%3A%2F%2Fwww.instagram.com%2F'
        response = requests.get(link, stream = True)

        with open("./insta_Shorts/"+video_name+".mp4","wb") as f:
        	for chunk in response.iter_content(chunk_size=1024):
        		if chunk:
        			f.write(chunk)



# ------------------------------------all video link catch ready to download----
# -------------------beping sound-------------------
import winsound
frequency = 3000  # Set Frequency To 2500 Hertz
duration = 20000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)



# ---------------------------------beeping sound end----------------
all_video_cheack = input("have you cheacked all downloaded video ? y: ")
if all_video_cheack=="y":
    print("all video cheacked")
# ---------------------------Reading insta_shorts file to get downloaded insta reels ----------
    print("----------now video eaditing started---------------")

    for file in os.listdir("./insta_Shorts/"):
        if file.endswith(".mp4"):
            print(file)
        time.sleep(1)

        try:

            clip=VideoFileClip(r"./insta_Shorts/"+str(file))
            clip_with_borders = clip.margin(top=10, bottom=10,left=10,right=10,color=(255, 153, 0))
            edited_clips_name=str(random.randrange(990, 2000))
            
            clip_with_borders.write_videofile(edited_clips_name+'clips.mp4', fps=24)
            
            
            # ------------------instagram open for video upload --------------------------------
            browser = webdriver.Firefox()
            browser.get('https://www.instagram.com/')
            time.sleep(2)
        
        
            def get_cookie_here(file):
                with open(file, 'r') as f:
                    reader = DictReader(f)
                    for row in reader:
                        browser.add_cookie(dict(row))
                    f.close()
        
        
            get_cookie_here("./instagram_cookie.csv")
        
        
            browser.refresh()
            
            time.sleep(10)
            elem = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
            time.sleep(4)
            ele= browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div').click()
            time.sleep(4)
            # ele=browser.find_element(By.CLASS_NAME,'_ac69').send_keys(os.getcwd()+"./1177clips.mp4")
            # ele=browser.find_element(By.CLASS_NAME,'_ac69').send_keys("./1177clips.mp4")
            inputs = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input')
            time.sleep(2)
            # inputs.click()
            # time.sleep(2)
            inputs.send_keys(os.path.abspath('./'+edited_clips_name+'clips.mp4'))
            time.sleep(35)
            next=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button').click()
            time.sleep(3)
            select_video_ratio=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button/div').click()
            time.sleep(3)
            select_video_ratio=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div').click()
            time.sleep(3)
            next=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
            time.sleep(4)
            next=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
            time.sleep(3)
            write_caption=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').click()
            time.sleep(3)
            write_caption=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys('p')
            time.sleep(3)
            write_caption=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys(Keys.CONTROL+'A')
            time.sleep(1)
            write_caption=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys('''Drop❤ if 'u' like this😍
            
            Dm for get feature 👍
            Follow :- @hinitishisback
            
            Credit :- All credit goes to their respective owners
            DM for Credit & Remove 📩❣️
            
            #model #travel #f #cute #followers #beauty #followback #likeforlike #tiktok #comment #trending #photographer #lifestyle #viral #followforfollow #explore #music #motivation #photoshoot #instamood #instapic #girl #quotes #selfie #naturephotography #memes #inspiration #explorepage #k #makeup
            ''')
            
            
            time.sleep(4)
            share_reels=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div").click()
            time.sleep(70)
            share_reels=browser.find_element(By.XPATH,"/html/body").send_keys(Keys.ESCAPE)
            time.sleep(2)
            browser.close()
            time.sleep(2)
        except:
            print("err to upload" + file)
    

# # ------------------now removing all downloaded video_names --------------------------------

for file in os.listdir("./insta_Shorts/"):
    if file.endswith(".mp4"):
        os.remove("./insta_Shorts/"+str(file))

for file in os.listdir("./"):
    if file.endswith(".mp4"):
            os.remove("./"+str(file))

with open("insta_reels_url_file.csv", "w") as f:
    f.write("url"+'\n')

with open("./log.txt","a")as f:
    f.write(f'{str(datetime.date.today())}\n')
time.sleep(2)
print('------------------All your Downloaded video and edited as wll as insta scraped url is deleted and program is sucessfull see you tomorow Thanks for using me-------------------')
