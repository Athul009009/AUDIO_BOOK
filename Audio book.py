# IMPORT THE NESSERY MODULES
import pyttsx3
import PyPDF2
import speech_recognition as sp

# OPEN THE FILE THAT IS IN .PDF FORMAT

f=open("123456.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(f)  #CALL PDF FILE READER
pages=pdfReader.numPages             #CALL NUM PAGES
print("THE TOTAL NO OF PAGES =",pages)   

speaker=pyttsx3.init()

# listener =sp.Recognizer()
# Engine=pyttsx3.init()
# voices=Engine.getProperty('voice')
# Engine.setProperty('voice',voices[2])
# Engine.say("PLEASE ENTER THE PAGE NUMBER THAT U WANT TO START :")
# Engine.runAndWait()

s=0
start1=int(input("PLEASE ENTER THE PAGE NUMBER THAT U WANT TO START :"))
end1=int(input("ENTER THE LAST PAGE THAT YOU WANT TO END    :"))

if start1==end1:
        print("STARTING AND ENDING CANNOT BE THE SAME!!! \n AUTO CORRECTING ..... \n DONE !! (^_^)")
        end=end1+1

f3=open("memmory.txt","a")
obj2=f3.write(f"\n\nsession={s} \n LAST STARTING SECTION WAS  :{start1} \n LAST ENDING SECTION WAS    :{end},{end1}")
f=open("memmory.txt")
obj3=f.read()
print(obj3)
        
for i in range(start1,end1):
    page=pdfReader.getPage(start1)  #TO GET THE PAGE 
    text=page.extractText()         #TO GET THE TEXT 
    speaker.say(text)               
    speaker.runAndWait() 
    s=s+1
    break

def mem():
    pass

# def __init__():
#     f22=open("memmory.txt","a")
#     f22.write(f"\n\nLAST SESSION \n SIR YOU STARTED :{start1} \n ENDED HERE :{end1} \n ")
#     f23=open("memmory.txt","r")
#     obj=f23.read()
#     print(obj)


# memmory()

