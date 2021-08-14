
import csv
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import speech_recognition as sr
import pyttsx3
import re
import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy as np
from word2number import w2n
import spreadsheets
def dob_nums(date):
    #print('Enter DOB: ')
    #date = input()            #[22 10 1998]
    
    DOB = []
    date = date.split(" ")    #[22 10 1998]
    
    date[2] = " ".join(date[2:])
    date = date[0:3]
    if date[0].isalpha():
      for d in date:
        print(d)
        d = w2n.word_to_num(d)
        DOB.append(d)
    print("date", date)
    date = np.array(DOB)
    print(date)
    birthday = ""
    for i in range (len(date)):
          if date[0] <= 31:
            birthday += str(date[i]) 
            birthday += "/"
          else:
            birthday += date[len(date)-i-1]
            birthday += "/"
    birthday = birthday[:-1]
    bday = []
    bday.append(birthday)
    return bday
def dob(date):
    Months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    DOB = []
    bday = ""
    #date input
    date=date.split()
    if(len(date[-1])==4):
        DOB=date[0]+"/"+str(Months[date[1]])+"/"+date[2]
    else:
        DOB=date[2]+"/"+str(Months[date[1]])+"/"+date[0]
        
   
    
    return DOB
def live_audio_to_text():
        r = sr.Recognizer() 
        speak = [ "cancer", "diabetes", "Thyroid"]
        speak = set(speak)
        answer = []
# def SpeechtoText(command):
#          engine = pyttsx3.init()
#          engine.say(command) 
#          engine.runAndWait()
    
#         while(1):    
#             try:
              
           
#             with sr.Microphone() as source2:
                   
#                 r.adjust_for_ambient_noise(source2, duration=0.2)
#                 audio2 = r.listen(source2)
                  
                
#                 Text = r.recognize_google(audio2)
#                 Text = Text.lower()
      
#                 print("You said"+Text)
#                 Text=Text.split(" ")
#                 ans = [x for x in Text if x in speak]
#                 print(answer)
#                 answer.append(ans)
                  
#                 except sr.RequestError as e:
#                     print("Could not request results; {0}".format(e))
              
#             except sr.UnknownValueError:
#                 print("We could not catch that, please repeat")
            
def audio_to_text(file):
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    
    # Reading Audio file as source
    # listening the audio file and store in audio_text variable
    
    with sr.AudioFile('audio_files/'+file) as source:
        
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            
            return text
         
        except:
             print('Sorry.. run again...')
def create_file(output_file,text):
    with open(output_file, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(["textinput" ,"value"])
        tsv_writer.writerow([text])
        #tsv_writer.writerow([text+" "])
def q1(word,key_words):
    important=words[0].split()
    compare=[]
    disease=[]
    flag=0
    for i in important:
        if(i=='no'):
            break
        elif(i=='diseas'):
            break
        else:
            compare.append(i)
        
    compare = ['diabetes' if i=='diabet' else i for i in compare]
    compare = [i.capitalize() for i in compare]
    for i in compare:
            
            if i in key_words:
                disease.append(i)
               
            else:
                if('Others' not in disease)&('Others' in key_words):
                    flag=1
    if flag==1:
        disease.append('Others')
    if(len(compare)==0)&('None' in key_words):
        disease.append('None')
    return disease
def q2(input1,key_words):
    numbers = []
    for i in key_words:
        numbers.append(i.replace('lakh',''))
        
    digit=[]
    operator=[]
    for i in numbers:
        for k in i:
            if k.isdigit():
                digit.append(k)
            else:
                operator.append(k)
    for i in range(len(operator)):
       numbers[i]= numbers[i].replace(operator[i],'t')
    num=[]
    for i in range(len(numbers)):
        num.append(tuple(numbers[i].split('t')))
    count=0
    for i in num:
        if(i[0]==""):
            if(input1<int(i[1])):
                index=0
        elif(i[1]==""):
            if(input1>int(i[0])):
                index=-1
        else:
            if(int(i[0])<input1)&(int(i[1])>input1):
                index=count
        count+=1
    return [key_words[index]]

def extract_words(dataset):
    corpus = []
    for i in range(0,len(dataset)):
      review = re.sub('[^a-zA-Z]', ' ', dataset['textinput'][i])
      review = review.lower()
      review = review.split()
      ps = PorterStemmer()
      all_stopwords = stopwords.words('english')
      all_stopwords.remove('no')
    
      review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
      review = ' '.join(review)
      corpus.append(review)
    
    return corpus

if __name__=='__main__':
    
    key=['q1','q2','q3']
    key_words_q1=['Cholestrol','Diabetes','Others']
    key_words_q2=["<5lakh","5lakh-10lakh","10lakh-15lakh","15lakh>"]
    file="a4.wav"
    #a1,
    #a6
    #a8
    output_file='./trial2.tsv'
    text=audio_to_text(file)
    create_file(output_file,text)
    dataset = pd.read_csv(output_file, delimiter = '\t', quoting = 3)
    words=extract_words(dataset)
    #print("choose question"):
    # select_q='q3'
    # if select_q=='q1':
    #     disease=q1(words,key_words_q1)
    #     print(disease)
    # if select_q=='q2':
    #     income=q2(int(text[0]),key_words_q2)
    # if select_q=='q3':
    #     birth=dob(text)
    #     #bday=dob_nums(birth)
    
    disease=q1(words,key_words_q1)
    file="j7.wav"
    text=audio_to_text(file)
    income=q2(int(text[0]),key_words_q2)
    file="a8.wav"
    text=audio_to_text(file)
    birth=dob(text)
    with open('form_filled','wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(["Question" ,"user_answer"])
        tsv_writer.writerow(["Do you suffer from any health diseases?",disease])
        tsv_writer.writerow(["What is your annual income?",income])
        tsv_writer.writerow(["What is your dob?",birth])
        
    