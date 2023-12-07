import pyttsx3
import pyscreenshot as ImageGrab
import time
from tkinter import ttk
import os
import subprocess
from pynput.keyboard import Key, Controller
import psutil
class SystemTasks:
    def __init__(self):
        self.keyboard = Controller()

    def openApp(self, appName):
        appName = appName.replace('paint', 'mspaint')
        appName = appName.replace('wordpad', 'write')
        appName = appName.replace('word', 'write')
        appName = appName.replace('calculator', 'calc')
        try:
            subprocess.Popen('C:\\Windows\\System32\\' + appName[5:] + '.exe')
        except:
            pass

    def write(self, text):
        text = text[5:]
        for char in text:
            self.keyboard.type(char)
            time.sleep(0.02)

    def select(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('a')
        self.keyboard.release('a')
        self.keyboard.release(Key.ctrl)

    def hitEnter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def delete(self):
        self.keyboard.press(Key.backspace)
        self.keyboard.release(Key.enter)

    def save(self, text):
        if "don't" in text:
            self.keyboard.press(Key.right)
        else:
            self.keyboard.press(Key.ctrl)
            self.keyboard.press('s')
            self.keyboard.release('s')
            self.keyboard.release(Key.ctrl)
        self.hitEnter()


class TabOpt:
    def __init__(self):
        self.keyboard = Controller()

    def switchTab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        self.keyboard.release(Key.ctrl)

    def closeTab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('w')
        self.keyboard.release('w')
        self.keyboard.release(Key.ctrl)

    def newTab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('n')
        self.keyboard.release('n')
        self.keyboard.release(Key.ctrl)


class WindowOpt:
    def __init__(self):
        self.keyboard = Controller()

    def openWindow(self):
        self.maximizeWindow()

    def closeWindow(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press(Key.f4)
        self.keyboard.release(Key.f4)
        self.keyboard.release(Key.alt_l)

    def minimizeWindow(self):
        for i in range(2):
            self.keyboard.press(Key.cmd)
            self.keyboard.press(Key.down)
            self.keyboard.release(Key.down)
            self.keyboard.release(Key.cmd)
            time.sleep(0.05)

    def maximizeWindow(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.up)
        self.keyboard.release(Key.up)
        self.keyboard.release(Key.cmd)

    def moveWindow(self, operation):
        self.keyboard.press(Key.cmd)

        if "left" in operation:
            self.keyboard.press(Key.left)
            self.keyboard.release(Key.left)
        elif "right" in operation:
            self.keyboard.press(Key.right)
            self.keyboard.release(Key.right)
        elif "down" in operation:
            self.keyboard.press(Key.down)
            self.keyboard.release(Key.down)
        elif "up" in operation:
            self.keyboard.press(Key.up)
            self.keyboard.release(Key.up)
        self.keyboard.release(Key.cmd)

    def switchWindow(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        self.keyboard.release(Key.alt_l)

    def takeScreenShot(self):
        from random import randint
        im = ImageGrab.grab()
        im.save(f'Files and Document/ss_{randint(1, 100)}.jpg')


def isContain(text, lst):
    for word in lst:
        if word in text:
            return True
    return False


def Win_Opt(operation):
    w = WindowOpt()
    if isContain(operation, ['open']):
        w.openWindow()
    elif isContain(operation, ['close']):
        w.closeWindow()
    elif isContain(operation, ['mini']):
        w.minimizeWindow()
    elif isContain(operation, ['maxi']):
        w.maximizeWindow()
    elif isContain(operation, ['move', 'slide']):
        w.moveWindow(operation)
    elif isContain(operation, ['switch', 'which']):
        w.switchWindow()
    elif isContain(operation, ['screenshot', 'capture', 'snapshot']):
        w.takeScreenShot()
    return


def Tab_Opt(operation):
    t = TabOpt()
    if isContain(operation, ['new', 'open', 'another', 'create']):
        t.newTab()
    elif isContain(operation, ['switch', 'move', 'another', 'next', 'previous', 'which']):
        t.switchTab()
    elif isContain(operation, ['close', 'delete']):
        t.closeTab()
    else:
        return


def System_Opt(operation):
    s = SystemTasks()
    if 'delete' in operation:
        s.delete()
    elif 'save' in operation:
        s.save(operation)
    elif 'type' in operation:
        s.write(operation)
    elif 'select' in operation:
        s.select()
    elif 'enter' in operation:
        s.hitEnter()
    elif isContain(operation, ['notepad', 'paint', 'calc', 'word']):
        s.openApp(operation)
    elif isContain(operation, ['music', 'video']):
        s.playMusic(operation)
    else:
        open_website(operation)
        return


###############################
###########  VOLUME ###########
###############################

keyboard = Controller()


def mute():
    for i in range(50):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)


def full():
    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)


def volumeControl(text):
    if 'full' in text or 'max' in text:
        full()
    elif 'mute' in text or 'min' in text:
        mute()
    elif 'incre' in text:
        for i in range(5):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
    elif 'decre' in text:
        for i in range(5):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)


def systemInfo():
    import wmi
    c = wmi.WMI()
    my_system_1 = c.Win32_LogicalDisk()[0]
    my_system_2 = c.Win32_ComputerSystem()[0]
    info = ["Total Disk Space: " + str(round(int(my_system_1.Size) / (1024 ** 3), 2)) + " GB",
            "Free Disk Space: " + str(round(int(my_system_1.Freespace) / (1024 ** 3), 2)) + " GB",
            "Manufacturer: " + my_system_2.Manufacturer,
            "Model: " + my_system_2.Model,
            "Owner: " + my_system_2.PrimaryOwnerName,
            "Number of Processors: " + str(my_system_2.NumberOfProcessors),
            "System Type: " + my_system_2.SystemType]
    return info


def batteryInfo():
    # usage = str(psutil.cpu_percent(interval=0.1))
    battery = psutil.sensors_battery()
    pr = str(battery.percent)
    if battery.power_plugged:
        return "Your System is currently on Charging Mode and it's " + pr + "% done."
    return "Your System is currently on " + pr + "% battery life."


def OSHandler(query):
    if isContain(query, ['system', 'info']):
        return ['Here is your System Information...', '\n'.join(systemInfo())]
    elif isContain(query, ['cpu', 'battery']):
        return batteryInfo()


from difflib import get_close_matches
import json
from random import choice
import webbrowser

data = {
	"google": [
		"https://www.google.com/"
	],
	"gmail": [
		"https://mail.google.com/mail/u/0/#inbox"
	],
	"myclass": [
		"https://myclass.lpu.in/"
	],
	"lpulive": [
		"https://lpulive.lpu.in/login"
	],
	"ums": [
		"https://ums.lpu.in/lpuums/"
	],
	"github": [
		"https://github.com/"
	],
	"youtube": [
		"https://www.youtube.com/"
	],
	"sanfoundry":[
		"https://www.sanfoundry.com/"
	],
	"hackerrank":[
		"https://www.hackerrank.com/dashboard"
	],
	"hackerearth":[
		"https://www.hackerearth.com/challenges/"
	],
	"codeforces": [
		"https://codeforces.com/enter?back=%2Fproblemset"
	],
	"codechef":[
		"https://www.codechef.com/"
	],
	"codecademy":[
		"https://www.codecademy.com/catalog"
	],
	"leetcode":[
		"https://leetcode.com/"
	],
	"udemy":[
		"https://www.udemy.com/"
	],
	"edx":[
		"https://www.edx.org/"
	],
	"coursera":[
		"https://www.coursera.org/"
	],
	"w3resource":[
		"https://www.w3resource.com/"
	],
	"w3schools":[
		"https://www.w3schools.com/"
	],
	"geeksforgeeks":[
		"https://www.geeksforgeeks.org/"
	],
	"stack overflow":[
		"https://stackoverflow.com/"
	],
	"instagram": [
		"https://www.instagram.com/?hl=en"
	],
	"facebook": [
		"https://www.facebook.com/"
	],
	"linkedin": [
		"https://www.linkedin.com/"
	],
	"twitter": [
		"https://twitter.com/LOGIN"
	]
}


def open_website(query):
    query = query.replace('open', '')
    if query in data:
        response = data[query]
    else:
        query = get_close_matches(query, data.keys(), n=2, cutoff=0.5)
        if len(query) == 0: return "None"
        response = choice(data[query[0]])
    webbrowser.open(response)









import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import threading
import smtplib
import urllib.request
import os
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
class COVID:
    def __init__(self):
        self.total = 'Not Available'
        self.deaths = 'Not Available'
        self.recovered = 'Not Available'
        self.totalIndia = 'Not Available'
        self.deathsIndia = 'Not Available'
        self.recoveredIndia = 'Not Available'

    def covidUpdate(self):
        URL = 'https://www.worldometers.info/coronavirus/'
        result = requests.get(URL)
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')

        temp = []
        divs = soup.find_all('div', class_='maincounter-number')
        for div in divs:
            temp.append(div.text.strip())
        self.total, self.deaths, self.recovered = temp[0], temp[1], temp[2]

    def covidUpdateIndia(self):
        URL = 'https://www.worldometers.info/coronavirus/country/india/'
        result = requests.get(URL)
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')

        temp = []
        divs = soup.find_all('div', class_='maincounter-number')
        for div in divs:
            temp.append(div.text.strip())
        self.totalIndia, self.deathsIndia, self.recoveredIndia = temp[0], temp[1], temp[2]

    def totalCases(self, india_bool):
        if india_bool: return self.totalIndia
        return self.total

    def totalDeaths(self, india_bool):
        if india_bool: return self.deathsIndia
        return self.deaths

    def totalRecovery(self, india_bool):
        if india_bool: return self.recoveredIndia
        return self.recovered

    def symptoms(self):
        symt = ['1. Fever',
                '2. Coughing',
                '3. Shortness of breath',
                '4. Trouble breathing',
                '5. Fatigue',
                '6. Chills, sometimes with shaking',
                '7. Body aches',
                '8. Headache',
                '9. Sore throat',
                '10. Loss of smell or taste',
                '11. Nausea',
                '12. Diarrhea']
        return symt

    def prevention(self):
        prevention = ['1. Clean your hands often. Use soap and water, or an alcohol-based hand rub.',
                      '2. Maintain a safe distance from anyone who is coughing or sneezing.',
                      '3. Wear a mask when physical distancing is not possible.',
                      '4. Don’t touch your eyes, nose or mouth.',
                      '5. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.',
                      '6. Stay home if you feel unwell.',
                      '7. If you have a fever, cough and difficulty breathing, seek medical attention.']
        return prevention


def wikiResult(query):
    query = query.replace('wikipedia', '')
    query = query.replace('search', '')
    if len(query.split()) == 0: query = "wikipedia"
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return "Desired Result Not Found"


class WEATHER:
    def __init__(self):
        self.tempValue = ''
        self.city = ''
        self.currCondition = ''
        self.speakResult = ''

    def updateWeather(self):
        res = requests.get("https://ipinfo.io/")
        data = res.json()
        # URL = 'https://weather.com/en-IN/weather/today/l/'+data['loc']
        URL = 'https://weather.com/en-IN/weather/today/'
        result = requests.get(URL)
        src = result.content

        soup = BeautifulSoup(src, 'html.parser')

        city = ""
        for h in soup.find_all('h1'):
            cty = h.text
            cty = cty.replace('Weather', '')
            self.city = cty[:cty.find(',')]
            break

        spans = soup.find_all('span')
        for span in spans:
            try:
                if span['data-testid'] == "TemperatureValue":
                    self.tempValue = span.text[:-1]
                    break
            except Exception as e:
                pass

        divs = soup.find_all('div', class_='CurrentConditions--phraseValue--2xXSr')
        for div in divs:
            self.currCondition = div.text
            break

    def weather(self):
        from datetime import datetime
        today = datetime.today().strftime('%A')
        self.speakResult = "Currently in " + self.city + ", its " + self.tempValue + " degree, with a " + self.currCondition
        return [self.tempValue, self.currCondition, today, self.city, self.speakResult]


c = COVID()
w = WEATHER()


def dataUpdate():
    c.covidUpdate()
    c.covidUpdateIndia()
    w.updateWeather()


##### WEATHER #####
def weather():
    return w.weather()


### COVID ###
def covid(query):
    if "india" in query:
        india_bool = True
    else:
        india_bool = False

    if "statistic" in query or 'report' in query:
        return ["Here are the statistics...",
                ["Total cases: " + c.totalCases(india_bool), "Total Recovery: " + c.totalRecovery(india_bool),
                 "Total Deaths: " + c.totalDeaths(india_bool)]]

    elif "symptom" in query:
        return ["Here are the Symptoms...", c.symptoms()]

    elif "prevent" in query or "measure" in query or "precaution" in query:
        return ["Here are the some of preventions from COVID-19:", c.prevention()]

    elif "recov" in query:
        return "Total Recovery is: " + c.totalRecovery(india_bool)

    elif "death" in query:
        return "Total Deaths are: " + c.totalDeaths(india_bool)

    else:
        return "Total Cases are: " + c.totalCases(india_bool)


def latestNews(news=5):
    URL = 'https://indianexpress.com/latest-news/'
    result = requests.get(URL)
    src = result.content

    soup = BeautifulSoup(src, 'html.parser')

    headlineLinks = []
    headlines = []

    divs = soup.find_all('div', {'class': 'title'})

    count = 0
    for div in divs:
        count += 1
        if count > news:
            break
        a_tag = div.find('a')
        headlineLinks.append(a_tag.attrs['href'])
        headlines.append(a_tag.text)

    return headlines, headlineLinks


def maps(text):
    text = text.replace('maps', '')
    text = text.replace('map', '')
    text = text.replace('google', '')
    openWebsite('https://www.google.com/maps/place/' + text)


def giveDirections(startingPoint, destinationPoint):
    geolocator = Nominatim(user_agent='assistant')
    if 'current' in startingPoint:
        res = requests.get("https://ipinfo.io/")
        data = res.json()
        startinglocation = geolocator.reverse(data['loc'])
    else:
        startinglocation = geolocator.geocode(startingPoint)

    destinationlocation = geolocator.geocode(destinationPoint)
    startingPoint = startinglocation.address.replace(' ', '+')
    destinationPoint = destinationlocation.address.replace(' ', '+')

    openWebsite('https://www.google.co.in/maps/dir/' + startingPoint + '/' + destinationPoint + '/')

    startinglocationCoordinate = (startinglocation.latitude, startinglocation.longitude)
    destinationlocationCoordinate = (destinationlocation.latitude, destinationlocation.longitude)
    total_distance = great_circle(startinglocationCoordinate, destinationlocationCoordinate).km  # .mile
    return str(round(total_distance, 2)) + 'KM'


def openWebsite(url='https://www.google.com/'):
    webbrowser.open(url)


def jokes():
    URL = 'https://icanhazdadjoke.com/'
    result = requests.get(URL)
    src = result.content

    soup = BeautifulSoup(src, 'html.parser')

    try:
        p = soup.find('p')
        return p.text
    except Exception as e:
        raise e


def youtube(query, youtube_search=None):
    from youtube_search import YoutubeSearch
    query = query.replace('play', ' ')
    query = query.replace('on youtube', ' ')
    query = query.replace('youtube', ' ')
    print("Pahuch Gya")
    results = YoutubeSearch(query, max_results=1).to_dict()
    print("Link mil gya")
    webbrowser.open('https://www.youtube.com/watch?v=' + results[0]['id'])
    return "Enjoy Sir..."


def googleSearch(query):
    if 'image' in query:
        query += "&tbm=isch"
    query = query.replace('images', '')
    query = query.replace('image', '')
    query = query.replace('search', '')
    query = query.replace('show', '')
    webbrowser.open("https://www.google.com/search?q=" + query)
    return "Here you go..."


def sendWhatsapp(phone_no='', message=''):
    phone_no = '+91' + str(phone_no)
    webbrowser.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + message)
    import time
    from pynput.keyboard import Key, Controller
    time.sleep(10)
    k = Controller()
    k.press(Key.enter)


def email(rec_email=None, text="Hello, It's F.R.I.D.A.Y. here...", sub='F.R.I.D.A.Y.'):
    if '@gmail.com' not in rec_email: return
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("someshgurram007@gmail.com", "76041100")  
    message = 'Subject: {}\n\n{}'.format(sub, text)
    s.sendmail("senderEmail", rec_email, message)
    print("Sent")
    s.quit()


def downloadImage(query, n=4):
    query = query.replace('images', '')
    query = query.replace('image', '')
    query = query.replace('search', '')
    query = query.replace('show', '')
    URL = "https://www.google.com/search?tbm=isch&q=" + query
    result = requests.get(URL)
    src = result.content

    soup = BeautifulSoup(src, 'html.parser')
    imgTags = soup.find_all('img', class_='yWs4tf')  # old class name -> t0fcAb (Update this)

    if os.path.exists('Downloads') == False:
        os.mkdir('Downloads')

    count = 0
    for i in imgTags:
        if count == n: break
        try:
            urllib.request.urlretrieve(i['src'], 'Downloads/' + str(count) + '.jpg')
            count += 1
            print('Downloaded', count)
        except Exception as e:
            raise e







from time import sleep
import re
import playsound
from tkinter import *
from threading import Thread
def startTimer(query):
    nums = re.findall(r'[0-9]+', query)
    time = 0
    if "minute" in query and "second" in query:
        time = int(nums[0]) * 60 + int(nums[1])
    elif "minute" in query:
        time = int(nums[0]) * 60
    elif "second" in query:
        time = int(nums[0])
    else:
        return

    print("Timer Started")
    sleep(time)
    Thread(target=timer).start()
    playsound.playsound("extrafiles/audios/Timer.mp3")


def timer():
    root = Tk()
    root.title("Timer")
    root.iconbitmap("extrafiles/images/timer.ico")
    w_width, w_height = 300, 150
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))
    root['bg'] = 'white'

    Label(root, text="Time's Up", font=("Arial Bold", 20), bg='white').pack(pady=20)
    Button(root, text="  OK  ", font=("Arial", 15), relief=FLAT, bg='#14A769', fg='white',
           command=lambda: quit()).pack()

    root.mainloop()


from difflib import get_close_matches
import json
from random import choice
import datetime
class DateTime:
    def currentTime(self):
        time = datetime.datetime.now()
        x = " A.M."
        if time.hour > 12: x = " P.M."
        time = str(time)
        time = time[11:16] + x
        return time

    def currentDate(self):
        now = datetime.datetime.now()
        day = now.strftime('%A')
        date = str(now)[8:10]
        month = now.strftime('%B')
        year = str(now.year)
        result = f'{day}, {date} {month}, {year}'
        return result


def wishMe():
    now = datetime.datetime.now()
    hr = now.hour
    if hr < 12:
        wish = "Good Morning"
    elif hr >= 12 and hr < 16:
        wish = "Good Afternoon"
    else:
        wish = "Good Evening"
    return wish


def isContain(text, lst):
    for word in lst:
        if word in text:
            return True
    return False


def chat(text):
    dt = DateTime()
    result = ""
    if isContain(text, ['good']):
        result = wishMe()
    elif isContain(text, ['time']):
        result = "Current Time is: " + dt.currentTime()
    elif isContain(text, ['date', 'today', 'day', 'month']):
        result = dt.currentDate()

    return result


data = {
	"how are you": [
		"Hey, I'm Good !",
		"I'm good",
		"I'm good, what about you?",
		"I'm fine, hope you're also fine",
		"Good, how about you?",
		"Doing fine, and you?",
		"I'm doing great",
		"I'm doing Well"
	],
	"what is your name": [
		"You can call me by any name",
		"Name doesn't matter",
		"I'm your Personal Assistant"
	],
	"who are you": [
		"I'm your Personal Assistant",
		"You know me right! If not then I'm your Personal Assistant",
		"You developed me, so you must know who I am",
		"Did I forget to introduce myself? I'm your Personal Assistant"
	],
	"tell me something": [
		"I have nothing to say...",
		"Hmm, you can ask me anything",
		"Hmm, you can ask me to tell a joke"
	],
	"thank you": [
		"Thank You",
		"Thank you so much",
		"Why are you saying thank you?",
		"My Pleasure",
		"You're welcome",
		"Welcome"
	],
	"hello": [
		"Hello",
		"Hello, how are you?"
	],
	"i am fine": [
		"Hope you're fine",
		"Good to know that you are fine",
		"Good to know"
	],
	"are you robot": [
		"Of course I'm a kind of Robot",
		"I'm your friend",
		"Yes I'm a robot, but I'm a good one"
	],
	"i have a question": [
		"Ask me",
		"Ask me, I can help you",
		"Don't hesitate, ask me",
		"You can always ask me"
	],
	"your birthday": [
		"I don't celebrate my Birthday",
		"My birthday is on 22nd September, 2020"
	],
	"you are funny": [
		"Good to know, that I'm funny - Haha !",
		"You think I'm funny",
		"Ya, I'm so funny",
		"I'm funny and can also make you laugh, Just ask me to tell a Joke"
	],
	"which colour you like": [
		"I like all the 7 Colors of a rainbow",
		"All Colors are my favorite"
	],
	"do you love me": [
		"Ya, I love you so much",
		"Ofcourse, I love you",
		"We're best friends"
	],
	"are you single": [
		"Haha, I'm always be single",
		"I'm your Assistant, and I dont want any relationship",
		"I'm only for you"
	],
	"you are smart": [
		"Yes, I'm smart",
		"Ofcourse I'm smart",
		"I'm a program, so I'm smart"
	],
	"i am really sorry": [
		"It's Ok",
		"No problem"
	],
	"are you my friend": [
		"Yes, I'm your friend",
		"We both are friend"
	],
	"i am alone": [
		"Don'f feel lonely. I'm always with You",
		"I can make you feely happy, Just say tell me a joke"
	],
	"i like your voice": [
		"Hope you love it...",
		"Thanks, I think this voice suits you the most",
		"Thank You So Much",
		"Ohh, that's good to know"
	]
}


def reply(query):
    if query in data:
        response = data[query]
    else:
        query = get_close_matches(query, data.keys(), n=2, cutoff=0.6)
        if len(query) == 0: return "None"
        return choice(data[query[0]])

    return choice(response)


def lang_translate(text, language):
    from googletrans import Translator, LANGUAGES
    if language in LANGUAGES.values():
        translator = Translator()
        result = translator.translate(text, src='en', dest=language)
        return result
    else:
        return "None"




import subprocess
import wmi
import os
import sys
import webbrowser

if os.path.exists('Files and Document') == False:
    os.mkdir('Files and Document')
path = 'Files and Document/'


def isContain(text, list):
    for word in list:
        if word in text:
            return True
    return False


def createFile(text):
    # change the applocation as per your system path
    appLocation = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"

    if isContain(text, ["ppt", "power point", "powerpoint"]):
        file_name = "sample_file.ppt"
        appLocation = "C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.exe"

    elif isContain(text, ['excel', 'spreadsheet']):
        file_name = "sample_file.xsl"
        appLocation = "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE"

    elif isContain(text, ['word', 'document']):
        file_name = "sample_file.docx"
        appLocation = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"

    elif isContain(text, ["text", "simple", "normal"]):
        file_name = "sample_file.txt"
    elif "python" in text:
        file_name = "sample_file.py"
    elif "css" in text:
        file_name = "sample_file.css"
    elif "javascript" in text:
        file_name = "sample_file.js"
    elif "html" in text:
        file_name = "sample_file.html"
    elif "c plus plus" in text or "c + +" in text:
        file_name = "sample_file.cpp"
    elif "java" in text:
        file_name = "sample_file.java"
    elif "json" in text:
        file_name = "sample_file.json"
    else:
        return "Unable to create this type of file"

    file = open(path + file_name, 'w')
    file.close()
    subprocess.Popen([appLocation, path + file_name])
    return "File is created.\nNow you can edit this file"


def CreateHTMLProject(project_name='Sample'):
    if os.path.isdir(path + project_name):
        webbrowser.open(os.getcwd() + '/' + path + project_name + "\\index.html")
        return 'There is a same project which is already created, look at this...'
    else:
        os.mkdir(path + project_name)

    os.mkdir(path + project_name + '/images')
    os.mkdir(path + project_name + '/videos')

    htmlContent = '<html>\n\t<head>\n\t\t<title> ' + project_name + ' </title>\n\t\t<link rel="stylesheet" type="text/css" href="style.css">\n\t</head>\n<body>\n\t<p id="label"></p>\n\t<button id="btn" onclick="showText()"> Click Me </button>\n\t<script src="script.js"></script>\n</body>\n</html>'

    htmlFile = open(path + project_name + '/index.html', 'w')
    htmlFile.write(htmlContent)
    htmlFile.close()

    cssContent = '* {\n\tmargin:0;\n\tpadding:0;\n}\nbody {\n\theight:100vh;\n\tdisplay:flex;\n\tjustify-content:center;\n\talign-items:center;\n}\n#btn {\n\twidth:200px;\n\tpadding: 20px 10px;\n\tborder-radius:5px;\n\tbackground-color:red;\n\tcolor:#fff;\n\toutline:none;border:none;\n}\np {\n\tfont-size:30px;\n}'

    cssFile = open(path + project_name + '/style.css', 'w')
    cssFile.write(cssContent)
    cssFile.close

    jsContent = 'function showText() {\n\tdocument.getElementById("label").innerHTML="Successfully Created ' + project_name + ' Project";\n\tdocument.getElementById("btn").style="background-color:green;"\n}'

    jsFile = open(path + project_name + '/script.js', 'w')
    jsFile.write(jsContent)
    jsFile.close()

    # change the applocation as per your system path
    appLocation = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
    # subprocess.Popen([appLocation, path + project_name])
    subprocess.Popen([appLocation, path + project_name + "/index.html"])
    subprocess.Popen([appLocation, path + project_name + "/style.css"])
    subprocess.Popen([appLocation, path + project_name + "/script.js"])

    webbrowser.open(os.getcwd() + '/' + path + project_name + "\\index.html")

    return f'Successfully Created {project_name} Project'





import math
def basicOperations(text):
	if 'root' in text:
		temp = text.rfind(' ')
		num = int(text[temp+1:])
		return round(math.sqrt(num),2)

	text = text.replace('plus', '+')
	text = text.replace('minus', '-')
	text = text.replace('x', '*')
	text = text.replace('multiplied by', '*')
	text = text.replace('multiply', '*')
	text = text.replace('divided by', '/')
	text = text.replace('to the power', '**')
	text = text.replace('power', '**')
	result = eval(text)
	return round(result,2)

def bitwiseOperations(text):
	if 'right shift' in text:
		temp = text.rfind(' ')
		num = int(text[temp+1:])
		return num>>1
	elif 'left shift' in text:
		temp = text.rfind(' ')
		num = int(text[temp+1:])
		return num<<1
	text = text.replace('and', '&')
	text = text.replace('or', '|')
	text = text.replace('not of', '~')
	text = text.replace('not', '~')
	text = text.replace('xor', '^')
	result = eval(text)
	return result

def conversions(text):
	temp = text.rfind(' ')
	num = int(text[temp+1:])
	if 'bin' in text:
		return eval('bin(num)')[2:]
	elif 'hex' in text:
		return eval('hex(num)')[2:]
	elif 'oct' in text:
		return eval('oct(num)')[2:]

def trigonometry(text):
	temp = text.replace('degree','')
	temp = text.rfind(' ')
	deg = int(text[temp+1:])
	rad = (deg * math.pi) / 180
	if 'sin' in text:
		return round(math.sin(rad),2)
	elif 'cos' in text:
		return round(math.cos(rad),2)
	elif 'tan' in text:
		return round(math.tan(rad),2)

def factorial(n):
	if n==1 or n==0: return 1
	else: return n*factorial(n-1)

def isHaving(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

def perform(text):
	text = text.replace('math','')
	if "factorial" in text: return str(factorial(int(text[text.rfind(' ')+1:])))
	elif isHaving(text, ['sin','cos','tan']): return str(trigonometry(text))
	elif isHaving(text, ['bin','hex','oct']): return str(conversions(text))
	elif isHaving(text, ['shift','and','or','not']): return str(bitwiseOperations(text))
	else: return str(basicOperations(text))




#########################
# GLOBAL VARIABLES USED #
#########################
ai_name = 'F.R.I.D.Y.'.lower()
EXIT_COMMANDS = ['bye', 'exit', 'quit', 'shut down', 'shutdown']

rec_email, rec_phoneno = "", ""
WAEMEntry = None

avatarChoosen = 0
choosedAvtrImage = None

botChatTextBg = "#007cc7"
botChatText = "white"
userChatTextBg = "#4da8da"

chatBgColor = '#12232e'
background = '#203647'
textColor = 'white'
AITaskStatusLblBG = '#203647'
KCS_IMG = 1  # 0 for light, 1 for dark
voice_id = 0  # 0 for female, 1 for male
ass_volume = 1  # max volume
ass_voiceRate = 200  # normal voice rate

""" User Created Modules """
try:
    import normalChat
    import math_function
    import appControl
    import webScrapping
    import timer
    import fileHandler
except Exception as e:
    raise e

""" System Modules """
try:
    import os
    import speech_recognition as sr
    import pyttsx3
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import colorchooser
    from PIL import Image, ImageTk
    from time import sleep
    from threading import Thread
except Exception as e:
    print(e)
class UserData:
	def __init__(self):
		self.name = 'Sahithi'
		self.gender = 'Female'
	def getName(self):
		return self.name
	def getGender(self):
		return self.gender
########################################## LOGIN CHECK ##############################################
try:
    User=UserData()
    ownerName = User.getName().split()[0]
    if User.getGender() == "Female":
        ownerDesignation = "Ma'am"
    else:
        ownerDesignation = "Sir"
except Exception as e:
    print("You're not Registered Yet !")
    raise SystemExit
########################################## BOOT UP WINDOW ###########################################
def ChangeSettings(write=False):
    import pickle
    global background, textColor, chatBgColor, voice_id, ass_volume, ass_voiceRate, AITaskStatusLblBG, KCS_IMG, botChatTextBg, botChatText, userChatTextBg
    setting = {'background': background,
               'textColor': textColor,
               'chatBgColor': chatBgColor,
               'AITaskStatusLblBG': AITaskStatusLblBG,
               'KCS_IMG': KCS_IMG,
               'botChatText': botChatText,
               'botChatTextBg': botChatTextBg,
               'userChatTextBg': userChatTextBg,
               'voice_id': voice_id,
               'ass_volume': ass_volume,
               'ass_voiceRate': ass_voiceRate
               }

    try:
        with open('C:\\Users\\somes\\PycharmProjects\\VA.py\\userData/settings.pck', 'rb') as file:
            loadSettings = pickle.load(file)
            background = loadSettings['background']
            textColor = loadSettings['textColor']
            chatBgColor = loadSettings['chatBgColor']
            AITaskStatusLblBG = loadSettings['AITaskStatusLblBG']
            KCS_IMG = loadSettings['KCS_IMG']
            botChatText = loadSettings['botChatText']
            botChatTextBg = loadSettings['botChatTextBg']
            userChatTextBg = loadSettings['userChatTextBg']
            voice_id = loadSettings['voice_id']
            ass_volume = loadSettings['ass_volume']
            ass_voiceRate = loadSettings['ass_voiceRate']
    except Exception as e:
        pass


if os.path.exists('C:\\Users\\somes\\PycharmProjects\\aiproject.py\\userData/settings.pck') == False:
    ChangeSettings(True)


def getChatColor(myColor):
    global chatBgColor
    chatBgColor = myColor[1]
    colorbar['bg'] = chatBgColor
    chat_frame['bg'] = chatBgColor
    root1['bg'] = chatBgColor


def changeTheme():
    global background, textColor, AITaskStatusLblBG, KCS_IMG, botChatText, botChatTextBg, userChatTextBg, chatBgColor
    if themeValue.get() == 1:
        background, textColor, AITaskStatusLblBG, KCS_IMG = "#203647", "white", "#203647", 1
        cbl['image'] = cblDarkImg
        kbBtn['image'] = kbphDark
        settingBtn['image'] = sphDark
        AITaskStatusLbl['bg'] = AITaskStatusLblBG
        botChatText, botChatTextBg, userChatTextBg = "white", "#007cc7", "#4da8da"
        chatBgColor = "#12232e"
        colorbar['bg'] = chatBgColor
    else:
        background, textColor, AITaskStatusLblBG, KCS_IMG = "#F6FAFB", "#303E54", "#14A769", 0
        cbl['image'] = cblLightImg
        kbBtn['image'] = kbphLight
        settingBtn['image'] = sphLight
        AITaskStatusLbl['bg'] = AITaskStatusLblBG
        botChatText, botChatTextBg, userChatTextBg = "#494949", "#EAEAEA", "#23AE79"
        chatBgColor = "#F6FAFB"
        colorbar['bg'] = '#E8EBEF'

    root['bg'], root2['bg'] = background, background
    settingsFrame['bg'] = background
    settingsLbl['fg'], userName['fg'], assLbl['fg'], voiceRateLbl['fg'], volumeLbl['fg'], themeLbl[
        'fg'], chooseChatLbl['fg'] =textColor, textColor, textColor, textColor, textColor, textColor, textColor
    settingsLbl['bg'], userName['bg'], assLbl['bg'], voiceRateLbl['bg'], volumeLbl['bg'], themeLbl[
        'bg'], chooseChatLbl['bg'] = background, background, background, background, background, background, background
    s.configure('Wild.TRadiobutton', background=background, foreground=textColor)
    volumeBar['bg'], volumeBar['fg'], volumeBar['highlightbackground'] = background, textColor, background
    chat_frame['bg'], root1['bg'] = chatBgColor, chatBgColor
    ChangeSettings(True)


def changeVoice(e):
    global voice_id
    voice_id = 0
    if assVoiceOption.get() == 'Male': voice_id = 1
    engine.setProperty('voice', voices[voice_id].id)
    ChangeSettings(True)


def changeVolume(e):
    global ass_volume
    ass_volume = volumeBar.get() / 100
    engine.setProperty('volume', ass_volume)
    ChangeSettings(True)


def changeVoiceRate(e):
    global ass_voiceRate
    temp = voiceOption.get()
    if temp == 'Very Low':
        ass_voiceRate = 100
    elif temp == 'Low':
        ass_voiceRate = 150
    elif temp == 'Fast':
        ass_voiceRate = 250
    elif temp == 'Very Fast':
        ass_voiceRate = 300
    else:
        ass_voiceRate = 200
    print(ass_voiceRate)
    engine.setProperty('rate', ass_voiceRate)
    ChangeSettings(True)


ChangeSettings()

############################################ SET UP VOICE ###########################################
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)  # male
    engine.setProperty('volume', ass_volume)
except Exception as e:
    print(e)


####################################### SET UP TEXT TO SPEECH #######################################
def speak(text, display=False, icon=False):
    AITaskStatusLbl['text'] = 'Speaking...'
    if icon: Label(chat_frame, image=botIcon, bg=chatBgColor).pack(anchor='w', pady=0)
    if display: attachTOframe(text, True)
    print('\n' + ai_name.upper() + ': ' + text)
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("Try not to type more...")


####################################### SET UP SPEECH TO TEXT #######################################
import speech_recognition as sr
def record(clearChat=True, iconDisplay=True):
    print('\nListening...')
    AITaskStatusLbl['text'] = 'Listening...'
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        try:
            AITaskStatusLbl['text'] = 'Processing...'
            said = r.recognize_google(audio)
            print(f"\nUser said: {said}")
            if clearChat:
                clearChatScreen()
            if iconDisplay: Label(chat_frame, image=userIcon, bg=chatBgColor).pack(anchor='e', pady=0)
            attachTOframe(said)
        except Exception as e:
            print(e)
            # speak("I didn't get it, Say that again please...")
            if "connection failed" in str(e):
                speak("Your System is Offline...", True, True)
            return 'None'
    return said.lower()


def voiceMedium():
    while True:
        query = record()
        if query == 'None': continue
        if isContain(query, EXIT_COMMANDS):
            speak("Shutting down the System. Good Bye " + ownerDesignation + "!", True, True)
            break
        else:
            main(query.lower())
    appControl.Win_Opt('close')


def keyboardInput(e):
    user_input = UserField.get().lower()
    if user_input != "":
        clearChatScreen()
        if isContain(user_input, EXIT_COMMANDS):
            speak("Shutting down the System. Good Bye " + ownerDesignation + "!", True, True)
        else:
            Label(chat_frame, image=userIcon, bg=chatBgColor).pack(anchor='e', pady=0)
            attachTOframe(user_input.capitalize())
            Thread(target=main, args=(user_input,)).start()
        UserField.delete(0, END)


###################################### TASK/COMMAND HANDLER #########################################
def isContain(txt, lst):
    for word in lst:
        if word in txt:
            return True
    return False


def main(text):
    if "project" in text:
        if isContain(text, ['make', 'create']):
            speak("What do you want to give the project name ?", True, True)
            projectName = record(False, False)
            speak(fileHandler.CreateHTMLProject(projectName.capitalize()), True)
            return

    if "create" in text and "file" in text:
        speak(fileHandler.createFile(text), True, True)
        return

    if "translate" in text:
        speak("What do you want to translate?", True, True)
        sentence = record(False, False)
        speak("Which langauage to translate ?", True)
        langauage = record(False, False)
        result = normalChat.lang_translate(sentence, langauage)
        if result == "None":
            speak("This langauage doesn't exists")
        else:
            speak(f"In {langauage.capitalize()} you would say:", True)
            if langauage == "hindi":
                attachTOframe(result.text, True)
                speak(result.pronunciation)
            else:
                speak(result.text, True)
        return


    if isContain(text, ['battery', 'system info']):
        result = appControl.OSHandler(text)
        if len(result) == 2:
            speak(result[0], True, True)
            attachTOframe(result[1], True)
        else:
            speak(result, True, True)
        return
    if 'volume' in text:
        appControl.volumeControl(text)
        Label(chat_frame, image=botIcon, bg=chatBgColor).pack(anchor='w', pady=0)
        attachTOframe('Volume Settings Changed', True)
        return

    if isContain(text, ['timer', 'countdown']):
        Thread(target=timer.startTimer, args=(text,)).start()
        speak('Ok, Timer Started!', True, True)
        return

    if 'whatsapp' in text:
        speak("Sure " + ownerDesignation + "...", True, True)
        speak('Whom do you want to send the message?', True)
        WAEMPOPUP("WhatsApp", "Phone Number")
        attachTOframe(rec_phoneno)
        speak('What is the message?', True)
        message = record(False, False)
        Thread(target=webScrapping.sendWhatsapp, args=(rec_phoneno, message,)).start()
        speak("Message is on the way. Do not move away from the screen.")
        attachTOframe("Message Sent", True)
        return

    if 'email' in text:
        speak('Whom do you want to send the email?', True, True)
        WAEMPOPUP("Email", "E-mail Address")
        attachTOframe(rec_email)
        speak('What is the Subject?', True)
        subject = record(False, False)
        speak('What message you want to send ?', True)
        message = record(False, False)
        Thread(target=webScrapping.email, args=(rec_email, message, subject,)).start()
        speak('Email has been Sent', True)
        return

    if isContain(text, ['covid', 'virus']):
        result = webScrapping.covid(text)
        if 'str' in str(type(result)):
            speak(result, True, True)
            return
        speak(result[0], True, True)
        result = '\n'.join(result[1])
        attachTOframe(result, True)
        return

    if isContain(text, ['youtube', 'video']):
        speak("Ok " + ownerDesignation + ", here a video for you...", True, True)
        try:
            speak(webScrapping.youtube(text), True)
        except Exception as e:
            speak("Desired Result Not Found", True)
        return

    if isContain(text, ['search', 'image']):
        if 'image' in text and 'show' in text:
            Thread(target=showImages, args=(text,)).start()
            speak('Here are the images...', True, True)
            return
        speak(webScrapping.googleSearch(text), True, True)
        return

    if isContain(text, ['map', 'direction']):
        if "direction" in text:
            speak('What is your starting location?', True, True)
            startingPoint = record(False, False)
            speak("Ok " + ownerDesignation + ", Where you want to go?", True)
            destinationPoint = record(False, False)
            speak("Ok " + ownerDesignation + ", Getting Directions...", True)
            try:
                distance = webScrapping.giveDirections(startingPoint, destinationPoint)
                speak('You have to cover a distance of ' + distance, True)
            except:
                speak("I think location is not proper, Try Again!")
        else:
            webScrapping.maps(text)
            speak('Here you go...', True, True)
        return

    if isContain(text, ['factorial', 'log', 'value of', 'math', ' + ', ' - ', ' x ', 'multiply', 'divided by', 'binary',
                        'hexadecimal', 'octal', 'shift', 'sin ', 'cos ', 'tan ']):
        try:
            speak(('Result is: ' + math_function.perform(text)), True, True)
        except Exception as e:
            return
        return

    if "joke" in text:
        speak('Here is a joke...', True, True)
        speak(webScrapping.jokes(), True)
        return

    if isContain(text, ['news']):
        speak('Getting the latest news...', True, True)
        headlines, headlineLinks = webScrapping.latestNews(2)
        for head in headlines: speak(head, True)
        speak('Do you want to read the full news?', True)
        text = record(False, False)
        if isContain(text, ["no", "don't"]):
            speak("No Problem " + ownerDesignation, True)
        else:
            speak("Ok " + ownerDesignation + ", Opening browser...", True)
            webScrapping.openWebsite('https://indianexpress.com/latest-news/')
            speak("You can now read the full news from this website.")
        return

    if isContain(text, ['weather']):
        data = webScrapping.weather()
        speak('', False, True)
        showSingleImage("weather", data[:-1])
        speak(data[-1])
        return

    if isContain(text, ['screenshot']):
        Thread(target=appControl.Win_Opt, args=('screenshot',)).start()
        speak("Screen Shot Taken", True, True)
        return

    if isContain(text, ['window', 'close that']):
        appControl.Win_Opt(text)
        return

    if isContain(text, ['tab']):
        appControl.Tab_Opt(text)
        return

    if isContain(text, ['setting']):
        raise_frame(root2)
        clearChatScreen()
        return

    if isContain(text, ['open', 'type', 'save', 'delete', 'select', 'press enter']):
        appControl.System_Opt(text)
        return

    if isContain(text, ['wiki', 'who is']):
        Thread(target=webScrapping.downloadImage, args=(text, 1,)).start()
        speak('Searching...', True, True)
        result = webScrapping.wikiResult(text)
        showSingleImage('wiki')
        speak(result, True)
        return





    if isContain(text, ['time', 'date']):
        speak(normalChat.chat(text), True, True)
        return

    if 'my name' in text:
        speak('Your name is, ' + ownerName, True, True)
        return

    if isContain(text, ['voice']):
        global voice_id
        try:
            if 'female' in text:
                voice_id = 0
            elif 'male' in text:
                voice_id = 1
            else:
                if voice_id == 0:
                    voice_id = 1
                else:
                    voice_id = 0
            engine.setProperty('voice', voices[voice_id].id)
            ChangeSettings(True)
            speak("Hello " + ownerDesignation + ", I have changed my voice. How may I help you?", True, True)
            assVoiceOption.current(voice_id)
        except Exception as e:
            print(e)
        return

    if isContain(text, ['morning', 'evening', 'noon']) and 'good' in text:
        speak(normalChat.chat("good"), True, True)
        return

    result = normalChat.reply(text)
    if result != "None":
        speak(result, True, True)
    else:
        speak("Here's what I found on the web... ", True, True)
        webScrapping.googleSearch(text)


##################################### DELETE USER ACCOUNT #########################################
def deleteUserData():
    result = messagebox.askquestion('Alert', 'Are you sure you want to delete your Face Data ?')
    if result == 'no': return
    messagebox.showinfo('Clear Face Data', 'Your face has been cleared\nRegister your face again to use.')
    import shutil
    shutil.rmtree('userData')
    root.destroy()


#####################
####### GUI #########
#####################

############ ATTACHING BOT/USER CHAT ON CHAT SCREEN ###########
def attachTOframe(text, bot=False):
    if bot:
        botchat = Label(chat_frame, text=text, bg=botChatTextBg, fg=botChatText, justify=LEFT, wraplength=250,
                        font=('Montserrat', 12, 'bold'))
        botchat.pack(anchor='w', ipadx=5, ipady=5, pady=5)
    else:
        userchat = Label(chat_frame, text=text, bg=userChatTextBg, fg='white', justify=RIGHT, wraplength=250,
                         font=('Montserrat', 12, 'bold'))
        userchat.pack(anchor='e', ipadx=2, ipady=2, pady=5)


def clearChatScreen():
    for wid in chat_frame.winfo_children():
        wid.destroy()


### SWITCHING BETWEEN FRAMES ###
def raise_frame(frame):
    frame.tkraise()
    clearChatScreen()


################# SHOWING DOWNLOADED IMAGES ###############
img0, img1, img2, img3, img4 = None, None, None, None, None


def showSingleImage(type, data=None):
    global img0, img1, img2, img3, img4
    try:
        img0 = ImageTk.PhotoImage(Image.open('Downloads/0.jpg').resize((90, 110), Image.ANTIALIAS))
    except:
        pass
    img1 = ImageTk.PhotoImage(Image.open('C:\\Users\\somes\\Downloads\\extrafiles\\images/heads.jpg').resize((220, 200), Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage(Image.open('C:\\Users\\somes\\Downloads\\extrafiles\\images/tails.jpg').resize((220, 200), Image.ANTIALIAS))
    img4 = ImageTk.PhotoImage(Image.open('C:\\Users\\somes\\Downloads\\extrafiles\\images/WeatherImage.png'))

    if type == "weather":
        weather = Frame(chat_frame)
        weather.pack(anchor='w')
        Label(weather, image=img4, bg=chatBgColor).pack()
        Label(weather, text=data[0], font=('Arial Bold', 45), fg='white', bg='#3F48CC').place(x=65, y=45)
        Label(weather, text=data[1], font=('Montserrat', 15), fg='white', bg='#3F48CC').place(x=78, y=110)
        Label(weather, text=data[2], font=('Montserrat', 10), fg='white', bg='#3F48CC').place(x=78, y=140)
        Label(weather, text=data[3], font=('Arial Bold', 12), fg='white', bg='#3F48CC').place(x=60, y=160)

    elif type == "wiki":
        Label(chat_frame, image=img0, bg='#EAEAEA').pack(anchor='w')
    elif type == "head":
        Label(chat_frame, image=img1, bg='#EAEAEA').pack(anchor='w')
    elif type == "tail":
        Label(chat_frame, image=img2, bg='#EAEAEA').pack(anchor='w')
    else:
        img3 = ImageTk.PhotoImage(
            Image.open('C:\\Users\\somes\\Downloads\\extrafiles\\images/dice/' + type + '.jpg').resize((200, 200), Image.ANTIALIAS))
        Label(chat_frame, image=img3, bg='#EAEAEA').pack(anchor='w')


def showImages(query):
    global img0, img1, img2, img3
    webScrapping.downloadImage(query)
    w, h = 150, 110
    # Showing Images
    imageContainer = Frame(chat_frame, bg='#EAEAEA')
    imageContainer.pack(anchor='w')
    # loading images
    img0 = ImageTk.PhotoImage(Image.open('Downloads/0.jpg').resize((w, h), Image.ANTIALIAS))
    img1 = ImageTk.PhotoImage(Image.open('Downloads/1.jpg').resize((w, h), Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage(Image.open('Downloads/2.jpg').resize((w, h), Image.ANTIALIAS))
    img3 = ImageTk.PhotoImage(Image.open('Downloads/3.jpg').resize((w, h), Image.ANTIALIAS))
    # Displaying
    Label(imageContainer, image=img0, bg='#EAEAEA').grid(row=0, column=0)
    Label(imageContainer, image=img1, bg='#EAEAEA').grid(row=0, column=1)
    Label(imageContainer, image=img2, bg='#EAEAEA').grid(row=1, column=0)
    Label(imageContainer, image=img3, bg='#EAEAEA').grid(row=1, column=1)


############################# WAEM - WhatsApp Email ##################################
def sendWAEM():
    global rec_phoneno, rec_email
    data = WAEMEntry.get()
    rec_email, rec_phoneno = data, data
    WAEMEntry.delete(0, END)
    appControl.Win_Opt('close')


def send(e):
    sendWAEM()


def WAEMPOPUP(Service='None', rec='Reciever'):
    global WAEMEntry
    PopUProot = Tk()
    PopUProot.title(f'{Service} Service')
    PopUProot.configure(bg='white')

    if Service == "WhatsApp":
        PopUProot.iconbitmap("C:\\Users\\somes\\Downloads\\extrafiles\\images/whatsapp.ico")
    else:
        PopUProot.iconbitmap("C:\\Users\\somes\\Downloads\\extrafiles\\images/email.ico")
    w_width, w_height = 410, 200
    s_width, s_height = PopUProot.winfo_screenwidth(), PopUProot.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    PopUProot.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
    Label(PopUProot, text=f'Reciever {rec}', font=('Arial', 16), bg='white').pack(pady=(20, 10))
    WAEMEntry = Entry(PopUProot, bd=10, relief=FLAT, font=('Arial', 12), justify='center', bg='#DCDCDC', width=30)
    WAEMEntry.pack()
    WAEMEntry.focus()

    SendBtn = Button(PopUProot, text='Send', font=('Arial', 12), relief=FLAT, bg='#14A769', fg='white',
                     command=sendWAEM)
    SendBtn.pack(pady=20, ipadx=10)
    PopUProot.bind('<Return>', send)
    PopUProot.mainloop()


######################## CHANGING CHAT BACKGROUND COLOR #########################
def getChatColor():
    global chatBgColor
    myColor = colorchooser.askcolor()
    if myColor[1] is None: return
    chatBgColor = myColor[1]
    colorbar['bg'] = chatBgColor
    chat_frame['bg'] = chatBgColor
    root1['bg'] = chatBgColor
    ChangeSettings(True)


chatMode = 1


def changeChatMode():
    global chatMode
    if chatMode == 1:
        # appControl.volumeControl('mute')
        VoiceModeFrame.pack_forget()
        TextModeFrame.pack(fill=BOTH)
        UserField.focus()
        chatMode = 0
    else:
        # appControl.volumeControl('full')
        TextModeFrame.pack_forget()
        VoiceModeFrame.pack(fill=BOTH)
        root.focus()
        chatMode = 1


############################################## GUI #############################################



#####################################  MAIN GUI ####################################################

#### SPLASH/LOADING SCREEN ####
def progressbar():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("white.Horizontal.TProgressbar", foreground='white', background='white')
    progress_bar = ttk.Progressbar(splash_root, style="white.Horizontal.TProgressbar", orient="horizontal",
                                   mode="determinate", length=303)
    progress_bar.pack()
    splash_root.update()
    progress_bar['value'] = 0
    splash_root.update()

    while progress_bar['value'] < 100:
        progress_bar['value'] += 5
        # splash_percentage_label['text'] = str(progress_bar['value']) + ' %'
        splash_root.update()
        sleep(0.1)


def destroySplash():
    splash_root.destroy()


if __name__ == '__main__':
    splash_root = Tk()
    splash_root.configure(bg='#3895d3')
    splash_root.overrideredirect(True)
    splash_label = Label(splash_root, text="Processing...", font=('montserrat', 15), bg='#3895d3', fg='white')
    splash_label.pack(pady=40)
    # splash_percentage_label = Label(splash_root, text="0 %", font=('montserrat',15),bg='#3895d3',fg='white')
    # splash_percentage_label.pack(pady=(0,10))

    w_width, w_height = 400, 200
    s_width, s_height = splash_root.winfo_screenwidth(), splash_root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    splash_root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))

    progressbar()
    splash_root.after(10, destroySplash)
    splash_root.mainloop()

    root = Tk()
    root.title('F.R.I.D.A.Y')
    w_width, w_height = 400, 650
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
    root.configure(bg=background)
    # root.resizable(width=False, height=False)
    root.pack_propagate(0)

    root1 = Frame(root, bg=chatBgColor)
    root2 = Frame(root, bg=background)
    root3 = Frame(root, bg=background)

    for f in (root1, root2, root3):
        f.grid(row=0, column=0, sticky='news')

    ################################
    ########  CHAT SCREEN  #########
    ################################

    # Chat Frame
    chat_frame = Frame(root1, width=380, height=551, bg=chatBgColor)
    chat_frame.pack(padx=10)
    chat_frame.pack_propagate(0)

    bottomFrame1 = Frame(root1, bg='#dfdfdf', height=100)
    bottomFrame1.pack(fill=X, side=BOTTOM)
    VoiceModeFrame = Frame(bottomFrame1, bg='#dfdfdf')
    VoiceModeFrame.pack(fill=BOTH)
    TextModeFrame = Frame(bottomFrame1, bg='#dfdfdf')
    TextModeFrame.pack(fill=BOTH)

    # VoiceModeFrame.pack_forget()
    TextModeFrame.pack_forget()

    cblLightImg = PhotoImage(file='C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\images\\centralButton.png')
    cblDarkImg = PhotoImage(file='C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\centralButton1.png')
    if KCS_IMG == 1:
        cblimage = cblDarkImg
    else:
        cblimage = cblLightImg
    cbl = Label(VoiceModeFrame, fg='white', image=cblimage, bg='#dfdfdf')
    cbl.pack(pady=17)
    AITaskStatusLbl = Label(VoiceModeFrame, text='    Offline', fg='white', bg=AITaskStatusLblBG,
                            font=('montserrat', 16))
    AITaskStatusLbl.place(x=140, y=32)

    # Settings Button
    sphLight = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\setting.png")
    sphLight = sphLight.subsample(2, 2)
    sphDark = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\setting1.png")
    sphDark = sphDark.subsample(2, 2)
    if KCS_IMG == 1:
        sphimage = sphDark
    else:
        sphimage = sphLight
    settingBtn = Button(VoiceModeFrame, image=sphimage, height=30, width=30, bg='#dfdfdf', borderwidth=0,
                        activebackground="#dfdfdf", command=lambda: raise_frame(root2))
    settingBtn.place(relx=1.0, y=30, x=-20, anchor="ne")

    # Keyboard Button
    kbphLight = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\keyboard.png")
    kbphLight = kbphLight.subsample(2, 2)
    kbphDark = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\keyboard1.png")
    kbphDark = kbphDark.subsample(2, 2)
    if KCS_IMG == 1:
        kbphimage = kbphDark
    else:
        kbphimage = kbphLight
    kbBtn = Button(VoiceModeFrame, image=kbphimage, height=30, width=30, bg='#dfdfdf', borderwidth=0,
                   activebackground="#dfdfdf", command=changeChatMode)
    kbBtn.place(x=25, y=30)

    # Mic
    micImg = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\mic.png")
    micImg = micImg.subsample(2, 2)
    micBtn = Button(TextModeFrame, image=micImg, height=30, width=30, bg='#dfdfdf', borderwidth=0,
                    activebackground="#dfdfdf", command=changeChatMode)
    micBtn.place(relx=1.0, y=30, x=-20, anchor="ne")

    # Text Field
    TextFieldImg = PhotoImage(file='C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\textField.png')
    UserFieldLBL = Label(TextModeFrame, fg='white', image=TextFieldImg, bg='#dfdfdf')
    UserFieldLBL.pack(pady=17, side=LEFT, padx=10)
    UserField = Entry(TextModeFrame, fg='white', bg='#203647', font=('Montserrat', 16), bd=6, width=22, relief=FLAT)
    UserField.place(x=20, y=30)
    UserField.insert(0, "Ask me anything...")
    UserField.bind('<Return>', keyboardInput)

    # User and Bot Icon
    userIcon = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\avatars\\ChatIcons\\a11.png")
    botIcon = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images/assistant2.png")
    botIcon = botIcon.subsample(2, 2)

    ###########################
    ########  SETTINGS  #######
    ###########################

    settingsLbl = Label(root2, text='Settings', font=('Arial Bold', 15), bg=background, fg=textColor)
    settingsLbl.pack(pady=10)
    separator = ttk.Separator(root2, orient='horizontal')
    separator.pack(fill=X)
    # User Photo
    userProfileImg = Image.open("C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images\\avatars\\ChatIcons\\a10.png")
    userProfileImg = ImageTk.PhotoImage(userProfileImg.resize((120, 120)))
    # Change Photo
    chngPh = ImageTk.PhotoImage(Image.open("C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images/avatars/changephoto2.png").resize((120, 120)))


    # Username
    userName = Label(root2, text=ownerName, font=('Arial Bold', 15), fg=textColor, bg=background)
    userName.pack()

    # Settings Frame
    settingsFrame = Frame(root2, width=300, height=300, bg=background)
    settingsFrame.pack(pady=20)

    assLbl = Label(settingsFrame, text='Assistant Voice', font=('Arial', 13), fg=textColor, bg=background)
    assLbl.place(x=0, y=20)
    n = StringVar()
    assVoiceOption = ttk.Combobox(settingsFrame, values=('Female', 'Male'), font=('Arial', 13), width=13,
                                  textvariable=n)
    assVoiceOption.current(voice_id)
    assVoiceOption.place(x=150, y=20)
    assVoiceOption.bind('<<ComboboxSelected>>', changeVoice)

    voiceRateLbl = Label(settingsFrame, text='Voice Rate', font=('Arial', 13), fg=textColor, bg=background)
    voiceRateLbl.place(x=0, y=60)
    n2 = StringVar()
    voiceOption = ttk.Combobox(settingsFrame, font=('Arial', 13), width=13, textvariable=n2)
    voiceOption['values'] = ('Very Low', 'Low', 'Normal', 'Fast', 'Very Fast')
    voiceOption.current(ass_voiceRate // 50 - 2)  # 100 150 200 250 300
    voiceOption.place(x=150, y=60)
    voiceOption.bind('<<ComboboxSelected>>', changeVoiceRate)

    volumeLbl = Label(settingsFrame, text='Volume', font=('Arial', 13), fg=textColor, bg=background)
    volumeLbl.place(x=0, y=105)
    volumeBar = Scale(settingsFrame, bg=background, fg=textColor, sliderlength=30, length=135, width=16,
                      highlightbackground=background, orient='horizontal', from_=0, to=100, command=changeVolume)
    volumeBar.set(int(ass_volume * 100))
    volumeBar.place(x=150, y=85)

    themeLbl = Label(settingsFrame, text='Theme', font=('Arial', 13), fg=textColor, bg=background)
    themeLbl.place(x=0, y=143)
    themeValue = IntVar()
    s = ttk.Style()
    s.configure('Wild.TRadiobutton', font=('Arial Bold', 10), background=background, foreground=textColor,
                focuscolor=s.configure(".")["background"])
    darkBtn = ttk.Radiobutton(settingsFrame, text='Dark', value=1, variable=themeValue, style='Wild.TRadiobutton',
                              command=changeTheme, takefocus=False)
    darkBtn.place(x=150, y=145)
    lightBtn = ttk.Radiobutton(settingsFrame, text='Light', value=2, variable=themeValue, style='Wild.TRadiobutton',
                               command=changeTheme, takefocus=False)
    lightBtn.place(x=230, y=145)
    themeValue.set(1)
    if KCS_IMG == 0: themeValue.set(2)

    chooseChatLbl = Label(settingsFrame, text='Chat Background', font=('Arial', 13), fg=textColor, bg=background)
    chooseChatLbl.place(x=0, y=180)
    cimg = PhotoImage(file="C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images/colorchooser.png")
    cimg = cimg.subsample(3, 3)
    colorbar = Label(settingsFrame, bd=3, width=18, height=1, bg=chatBgColor)
    colorbar.place(x=150, y=180)
    if KCS_IMG == 0: colorbar['bg'] = '#E8EBEF'
    Button(settingsFrame, image=cimg, relief=FLAT, command=getChatColor).place(x=261, y=180)

    backBtn = Button(settingsFrame, text='   Back   ', bd=0, font=('Arial 12'), fg='white', bg='#14A769', relief=FLAT,
                     command=lambda: raise_frame(root1))
    clearFaceBtn = Button(settingsFrame, text='   Clear Facial Data   ', bd=0, font=('Arial 12'), fg='white',
                          bg='#14A769', relief=FLAT, command=deleteUserData)
    backBtn.place(x=5, y=250)
    clearFaceBtn.place(x=120, y=250)

    try:
        # pass
        Thread(target=voiceMedium).start()
    except:
        pass
    try:
        # pass
        Thread(target=webScrapping.dataUpdate).start()
    except Exception as e:
        print('System is Offline...')

    root.iconbitmap('C:\\Users\\somes\\Downloads\\extrafiles\\extrafiles\\images/assistant2.ico')
    raise_frame(root1)
    root.mainloop()