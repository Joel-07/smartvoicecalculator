from functools import reduce
import re
import speech_recognition as sr
import os
from gtts import gTTS
import random


def add(args):
    sum1=reduce(lambda x,y:x+y,args)
    return(sum1)

def subtract(args):
    sub1=reduce(lambda x,y:x-y,args)
    return(sub1)

def multiplication(args):
    mul1=reduce(lambda x,y:x*y,args)
    return(mul1)

def division(args):
    div1=reduce(lambda x,y:x/y,args)
    return(div1)

def recaudio():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Something')
        audio=r.listen(source)


        data=''
        try:
            data=r.recognize_google(audio)
            print('You said',data)
        except sr.UnknownValueError:
            print('Couldn\'t understand that')
        except sr.RequestError as e:
            print('Request error',e)
        return (data)



def response(text):
    print(text)

    obj=gTTS(text=text,lang='en',slow=False)

    obj.save('response.mp3')

    os.system('open response.mp3')


def wakeword(text):
    wake=['hey','what','hello']
    text=text.lower()
    for word in wake:
        if word in text:
            return True
    return False


def greet(text):
    greetinp=['hey','hi','hello']
    greetresp=['hey','hello','hey there','hola','heyy buddy']

    for word in text.split():
        if word.lower() in greetinp:
            return random.choice(greetresp)
    return ' '


a1=[]
while True:
    text=recaudio()
    resp=''

    if wakeword(text)==True:
        
        resp=resp+greet(text)
        text1=text.split()
        #addition
        if 'add' in text or 'addition' in text or '+' in text:
            for i in text1:
                if i.isdigit() or re.fullmatch(r"^[0-9]{1,}.[0-9]{1,}$",i):
                    a1.append(float(i))
            summ=add(a1)
            resp=resp+' the addition is'+str(summ)
            a1=[]
        
        #subtraction
        elif 'sub' in text or 'subtract' in text or 'minus' in text or 'difference' in text or '-' in text:
            for i in text1:
                    if i.isdigit() or re.fullmatch(r"^[0-9]{1,}.[0-9]{1,}$",i):
                        a1.append(float(i))
            subb=subtract(a1)
            resp=resp+' the difference is'+str(subb)
            a1=[]

        #Multiplication
        elif 'multiple' in text or 'into' in text or 'multiply' in text or 'multiplication' in text or 'times' in text:
            for i in text1:
                    if i.isdigit() or re.fullmatch(r"^[0-9]{1,}.[0-9]{1,}$",i):
                        a1.append(float(i))
            mull=multiplication(a1)
            resp=resp+' the multiplication is'+str(mull)
            a1=[]
    
        #Division
        elif 'divide' in text or 'div' in text or '/' in text:
            for i in text1:
                if i.isdigit() or re.fullmatch(r"^[0-9]{1,}.[0.9]{1,}$",i):
                    a1.append(float(i))
            divv=division(a1)
            resp=resp+' the division is'+str(divv)

        #square
        elif 'square' in text:
            for i in text1:
                if i.isdigit():
                    sq=int(i)**2
                    resp=resp+' the square of'+i+'is'+str(sq)

        #cube
        elif 'cube' in text:
            for i in text1:
                if i.isdigit():
                    cu=int(i)**3
                    resp=resp+' the square of'+i+'is'+str(cu)
        
        else:
             resp=resp + "This operation is not available"

    

        response(resp)
    if text=='ok bye':
        respo=['Have a lovely day','thankyou','hope you use me again']
        resp=random.choice(respo)
        response(resp)
        break