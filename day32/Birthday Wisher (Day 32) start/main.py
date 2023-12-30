
import datetime as dt
import smtplib as smtp
import random
import pandas

SENDER_EMAIL = "test4python15@gmail.com"
SENDER_PASS = ""

# Read in the birthday csv
birthdays = pandas.read_csv("Birthdays.csv")

# Get today's date
time_now = dt.datetime.now()

# Get all birthdays that are today
birthdays_today = birthdays[(birthdays.Month == time_now.month) & (birthdays.Day == time_now.day)]

for idx, row in birthdays_today.iterrows():
    # Get the information for the specific person such as name, age, and what letter to use
    name = row.Name
    age = time_now.year - row.Year
    letter = f"letter{random.randint(1, 3)}.txt"
    replacements = {
        "[NAME]": name,
        "[AGE]": str(age),
    }

    # Open the corresponding letter, and replace the necessary portions with name and age
    with open(letter) as birthday_letter:

        msg = birthday_letter.read()

        for key, value in replacements.items():
            msg = msg.replace(key, value)

    # Open an email connection, and send the birthday email
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=row.Email,
            msg=f"Subject:Happy Birthday!\n\n{msg}"
        )
