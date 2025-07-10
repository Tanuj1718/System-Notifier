import psutil
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Thresholds
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 80

load_dotenv()

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_FROM, EMAIL_PASS)
        smtp.send_message(msg)

def check_system_usage():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print(cpu, ram, disk)
    print(f"🔥 CPU usage: {cpu}% \n 🥵It's getting hotter than you!")
    print((f"RAM usage: ({ram}%) \n 🧠 RAM is getting out of memory — just like me forgetting what I wrote!"))
    print((f"Disk usage: {disk}% \n 💾 Disk is filling, remove unwanted files before it starts billing"))
    alert_msgs = []

    if cpu > CPU_THRESHOLD:
        alert_msgs.append(f"🔥 CPU usage: {cpu}% \n 🥵It's getting hotter than you!\n")

    if ram > RAM_THRESHOLD:
        alert_msgs.append(f"RAM usage: {ram}% \n 🧠 RAM is getting out of memory — just like me forgetting what I wrote!\n")

    if disk > DISK_THRESHOLD:
        alert_msgs.append(f"Disk usage: {disk}% \n 💾 Disk is filling, remove unwanted files before it starts billing.\n")



    if alert_msgs:
        subject = "System Resource Alert 🚨"
        body = "\n".join(alert_msgs)
        send_email(subject, body)

check_system_usage()
