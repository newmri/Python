import datetime as dt
import pandas
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthdays[today_tuple])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("ID", "Password")
            connection.sendmail(
                "ID",
                birthdays[today_tuple]["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
