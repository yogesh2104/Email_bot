import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    with sr.Microphone() as source:
        print("listening......")
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
        return info.lower()

def sendemail(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your email id','your email_id password')
    email = EmailMessage()
    email['From'] = "your email id"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)
    print("Email send Successfully....")

email_list = {
    "kumar" : "iamyogesh2104@gmail.com",
    "sandeep" : "sk9366026@gmail.com",
    "saurabh" : "saurabhsharma29520@gmail.com"
}

def get_email_info():
    talk("To whom you want to send email ?")
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject of your email ?")
    subject = get_info()
    talk("Tell me the text inyour email ?")
    message = get_info()
    sendemail(receiver,subject,message)
    talk("Email send Successfully....")
    talk("Do You want to send More Email..")
    answer = get_info()
    if "yes" in answer:
        get_email_info()
    talk("Thank You For this service.")

print("Start....")
get_email_info()
