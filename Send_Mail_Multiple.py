import smtplib as ch

ob=s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('example@gmail.com', 'Enter your Email password that you are want to use to send mail')
subject="Chaudhary Junead"
body="Comsats University Islamabad Sahiwal Campus, I am working as Penetration tester now"
massage="subject:{}\n\n{}".format(subject,body)
listmail=['Chaudharyjunead.449@gmail.com',
           "chjuneadyounas.449@gmail.com",
           "junead.449@gmail.com",
           "junaidamz786@gmail.com"]

ob.sendmail('example@gmail.com',listmail , massage)
print("Send Mail")
ob.quit()