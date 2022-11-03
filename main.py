import smtplib

# SMTP

my_email = "my_email@gmail.com"
password = "passwordlkdfjbsdf"

reciepient_address = "recpt_email@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=reciepient_address,
                        msg="Ubject:Hello\n\nThis is the body of the email.")
    connection.close()

# DATE TIME

import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
dayofweek = now.weekday()
print(year)

date_of_birth = dt.datetime(year=2003, month=7, day=5, hour=10)
print(date_of_birth)