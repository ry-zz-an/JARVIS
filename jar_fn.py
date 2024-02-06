import nltk
import webbrowser
import requests, json
from pynput.keyboard import Key,Controller
keyboard = Controller()
import datetime
from datetime import date
from datetime import timedelta
import pdfplumber
import os.path
import time

# tokenizer
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

# stop words
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
words = ['I', 'am', 'a', 'writer']
[word for word in words if word not in english_stops]


# lemmatizer(better)
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


# main
def process(inpt):
    inpt_tok = tokenizer.tokenize(inpt)
    inpt_sw = [word for word in inpt_tok if word not in english_stops]
    inpt_lem = []
    for i in inpt_sw:
        x = lemmatizer.lemmatize(i)
        inpt_lem.append(x)
    if len(inpt_lem) != 0:
        if inpt_lem[0] == 'ok':
            inpt_lem.pop(0)
    return inpt_lem

def execute(search):
    url = 'https://google.com/search?q='+ search
    webbrowser.get(chrome_loc).open(url)
    x = 'this is what i found for'+ search
    return x

#weather
chrome_loc = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Bengaluru"
API_KEY = "af87a1020f3bc84a5311ddac6468382e"
W_URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(W_URL)

def weather(x):
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temp = (main['temp'])-273
        humidity = main['humidity']
        pressure = (main['pressure'])*0.0009869233
        if x=='weather':
            a = 'The current temperature is '+str(int(temp))+' degree celcius'+'. The current humidity is '+str(humidity)+' percentage. The current pressure is '+str(round(pressure,3))+' atm'
        elif x=='temperature':
            a='The current temperature is '+str(int(temp))+' degree celcius'
        elif x=='humidty':
            a='The current humidity is '+str(humidity)+'percentage'
        elif x=='pressure':
            a='. The current pressure is '+str(round(pressure,3))+' atm'
        return a
    else:
        return 'Sorry! Could not get weather report.'
# volume control
def volume_up():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

def volume_down():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)

def mute():
    keyboard.press(Key.media_volume_mute)
    keyboard.release(Key.media_volume_mute)

#time
def k_time():
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    hours=time.strftime("%H", curr_time)
    mins=time.strftime("%M", curr_time)
    if int(hours)<12:
        txt='the current time is '+str(hours)+' '+str(mins)+' am'
    else:
        txt='the current time is '+str(int(hours)-12)+' '+str(mins)+' pm'
    return txt

#date
def k_date(x):
    tdy = date.today()
    if x=='today\'s':
        n_tdy = change_date(str(tdy))
        y = 'today\'s date is'+n_tdy
    elif x=='yesterday\'s':
        ystdy = tdy - timedelta(days=1)
        n_ystdy = change_date(str(ystdy))
        y = 'yesterday\'s date was'+n_ystdy
    elif x=='tomorrow\'s':
        tmw = tdy + timedelta(days=1)
        n_tmw = change_date(str(tmw))
        y = 'tomorrow\'s date is'+n_tmw
    return y

#narrator
def narrator(loc,x):
    print(loc)
    with pdfplumber.open(loc) as pdf:
        page = pdf.pages[x-1]
        return page.extract_text()

#open file
def pdf_open(loc):
    webbrowser.open_new(r'file://'+loc)

def change_date(x):
    D={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    L=x.split('-')
    return L[2]+' '+D[L[1]]+' '+L[0]

def k_open(x,y):
    D={'exe':'exe','pdf':'pdf','python':'py','document':'doc','excel':'xlsx','text':'txt'}
    file_name=x+'.'+D[y]
    t = 0
    for r,d,f in os.walk("c:\\"):
        for files in f:
            if files == file_name:
                file_loc=os.path.join(r,files)
                webbrowser.open_new(r'file://'+file_loc)
                t = 1
                break
        if t==1:
            break
    else:
        return 'sorry could not find the specified file'
    return 'ok sir'

def clear_sl(x):
    f=open('shopping_list.csv','r+',newline='')
    csv_r=csv.reader(f)
    found=0
    L=[]
    for rec in csv_r:
        if rec[0]==x:
            rec[1]=''
        L.append(rec)
    f.close()
    f=open('shopping_list.csv','w',newline='')
    csv_w=csv.writer(f)
    for j in L:
        print(j)
        csv_w.writerow(j)
    f.close()
    

def update_sl(x,y):
    f=open('shopping_list.csv','r+',newline='')
    csv_r=csv.reader(f)
    found=0
    L=[]
    for rec in csv_r:
        if rec[0]==x:
            print(y)
            for i in y:
                try:
                    rec[1]+=(','+i)
                except:
                    pass
        L.append(rec)
    f.close()
    f=open('shopping_list.csv','w',newline='')
    csv_w=csv.writer(f)
    for j in L:
        print(j)
        csv_w.writerow(j)
    f.close()

def del_sl(x,y):
    f=open('shopping_list.csv','r',newline='')
    csv_r=csv.reader(f)
    found=0
    L=[]
    for rec in csv_r:
        if rec[0]==x:
            for i in y:
                try:
                    print(rec[1])
                    rec[1]=rec[1].replace((','+i),'')
                except:
                    pass
        L.append(rec)
    f.close()
    f=open('shopping_list.csv','w',newline='')
    csv_w=csv.writer(f)
    for j in L:
        print(j)
        csv_w.writerow(j)
    f.close()

def read_sl(x):
    f=open('shopping_list.csv','r',newline='')
    csv_r=csv.reader(f)
    for rec in csv_r:
        if rec[0]==x:
            return rec[1]
    f.close()


chattext=[]
replytext=[]
