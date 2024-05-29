import pandas as pd
from datetime import datetime
from twilio.rest import Client

# Load the spreadsheet
df = pd.read_excel('birthdays.xlsx')

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Function to send WhatsApp message
def send_whatsapp_message(to, body):
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=body,
                              to=to
                          )
    print("Message sent to", to)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    name = row['Name']
    birthday = row['Birthday']

    # Calculate days until birthday
    today = datetime.today()
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)
    days_until_birthday = (next_birthday - today).days

    # Send reminder if birthday is within 7 days
    if 0 < days_until_birthday <= 7:
        message = f"Don't forget, {name}'s birthday is in {days_until_birthday} days!"
        send_whatsapp_message('whatsapp:+1234567890', message)  # Replace with your number

print("It worked")