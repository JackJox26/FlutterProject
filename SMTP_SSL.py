import smtplib,ssl
port = 465
password = input("Entre ton mot de passe et entrer")

#Create a secure SSL context
context = ssl.create_default_context()
with smtplib.S