def jarvis():
    import pyttsx3
    import sys
    import speech_recognition as sr
    import jar_fn as jf
    import webbrowser
    import time
    import os
    import os.path
    import urllib.request
    import re
    import random
    import wikipedia
    import pdfplumber
    import csv

    #loaction of chrome app
    chrome_loc = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    # command for speech to text
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
        
    r = sr.Recognizer()

    ch_hist=open('history.txt','a')


    def takeCommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            ch_hist.write("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            ch_hist.write("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            ch_hist.write('You said:', query)

        except Exception as e:   
            x = "Say that again please..."
            ch_hist.write(x)
            return x
        return query.lower()


    close = ['shutdown', 'sleep', 'close', 'goodbye', 'bye', 'shut']
    status = True

    speak('Allow me to introduce myself. I am Jarvis, a virtual artificial intelligence and I\'m here to assist you in variety of task as best I can, 24 hours day, seven days a week. Importing all preferences from home interface. Systems are now fully operational')

    #__main__
    while status:
        # take input from mic
        query = takeCommand()

        
        if query not in jf.chattext:
            pro_query = jf.process(query)

            # search for the specified thing 
            if pro_query[0] in ['search', 'google']:
                s = pro_query[1:]
                s_text = ' '.join(map(str, s))
                speak(jf.execute(s_text))

            #close the program
            elif pro_query[-1] in close:
                speak('i hope you liked my sevice, goodbye')
                status = False


            #time
            elif pro_query[-1] == 'time':
                txt = jf.k_time()
                speak(txt)
                ch_hist.write(txt)

            #date
            elif pro_query[-1] == 'date':
                txt = jf.k_date(pro_query[-2])
                speak(txt)
                ch_hist.write(txt)

            #pause the program
            elif pro_query[0] == 'wait':
                time.sleep(5)

            # weather
            try:
                if pro_query[-1] in ['weather', 'temperature', 'humidity', 'pressure'] or pro_query[-2] in ['weather', 'temperature', 'humidity', 'pressure']:
                    speak(jf.weather(pro_query[-1]))
            except:
                pass

            # increase or decrease the volume
            if 'volume' in pro_query:
                if pro_query[pro_query.index('volume')-1] == 'increase':
                    jf.volume_up()
                    ch_hist.write('Volume increased')
                elif pro_query[pro_query.index('volume')-1] == 'decrease':
                    jf.volume_down()
                    ch_hist.write('Volume decreased')
            # mute
            elif 'mute' in pro_query or 'unmute' in pro_query:
                jf.mute()
                ch_hist.write('Program muted')

            
            # tell about a specific person or thing from wikipedia
            elif query[:7] in ['who is ','what is'] or query[:13] == 'tell me about':
                if pro_query[0] == 'tell':
                    pro_query.remove('tell')
                search_word = ''.join(pro_query)
                ch_hist.write('Searched for '+search_word)
                try:
                    result = wikipedia.summary(search_word, sentences = 2)
                    speak('wikipedia says' + result)
                except:
                    x = ' '.join(pro_query)
                    wiki_link = "https://en.wikipedia.org/wiki/" + x
                    webbrowser.get(chrome_loc).open(wiki_link)

            # play music 
            elif pro_query[-1] in ['music', 'beat', 'song']:
                found= True
                while found:
                    speak('which song do You want me to play')
                    mus_f=takeCommand()
                    if mus_f != "Say that again please...":
                        found = False
                        file_path="C:/Users/bkvve/Desktop/sahil/jarback/music/"+mus_f+'.mp3'
                        my_file = os.path.exists(file_path)
                        if my_file:
                            speak('ok sir, playing'+mus_f)
                            os.startfile(file_path)
                            time.sleep(5)
                        elif mus_f in ['random','any random song','whatever you like','random song','anything']:
                            f_loc=random.choice(os.listdir("C:/Users/bkvve/Desktop/sahil/jarback/music"))
                            speak('ok sir')
                            os.startfile("C:/Users/bkvve/Desktop/sahil/jarback/music/"+f_loc)
                            time.sleep(5)
                        else:
                            x = mus_f.replace(' ','+')
                            html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+x)
                            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                            vid_link="https://www.youtube.com/watch?v=" + video_ids[0]
                            speak('ok sir, playing'+mus_f)
                            webbrowser.get(chrome_loc).open(vid_link)
                ch_hist.write('Played Music')

            # narrator
            elif  pro_query == ['open','pdf']:
                speak('which file do you want to open')
                file_name = takeCommand()
                loc="C:/Users/bkvve/Desktop/sahil/J.A.R.V.I.S/pdf/"+file_name+'.pdf'
                if  not os.path.isfile(loc):
                    speak('sorry could not find the pdf')
                    continue
                speak('Do you want me to read it for you?')
                resp = takeCommand()
                if 'yes' in resp:
                    speak('which page number')
                    Page_no = int(takeCommand())
                    jf.pdf_open(loc)
                    txt=jf.narrator(loc,Page_no)
                    ch_hist.write(txt)
                    speak(txt)
                    
                else:
                    jf.pdf_open(loc)
                ch_hist.write('Read file: '+loc)

            # shopping list
            elif 'shopping' in pro_query:
                if 'read' in pro_query:
                    jf.speak(read_sl(pro_query[-1]))
                    ch_hist.write('Read shopping list')
                    continue
                elif 'clear' in pro_query:
                    jf.clear_sl(pro_query[-1])
                    ch_hist.write('Cleared shopping list')
                    continue
                L = list(pro_query)
                a = L.pop(0)
                b = L.pop(-1)
                if b == 'three':
                    b = '3'
                try:
                    L.remove('shopping')
                    L.remove('list')
                except:
                    pass
                if a in ['remove', 'delete']:
                    jf.del_sl(b,L)
                elif a in ['add']:
                    jf.update_sl(b,L)

            # search for a specfied file or application in the C drive
            elif 'open' in pro_query:
                Fname = pro_query[-1]
                speak('What is the file type?')
                y = takeCommand()
                speak(jf.k_open(Fname, y))
                ch_hist.write('Opened file: '+jf.k_open(Fname,y))
        else:
            chat_list = jf.chattext
            chat_index = chat_list.index(query)
            reply_text = jf.replytext[chat_index]
            speak(reply_text)
            
        speak(query)
        
    ch_hist.close()
