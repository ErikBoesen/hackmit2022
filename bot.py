import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from pathlib import Path
from dotenv import load_dotenv
from classify import Classifier
import pandas as pd

load_dotenv()

client = WebClient(token=os.environ['SLACK_TOKEN'])

matty = Classifier('easy_sponsor.csv')
df = pd.read_csv('easy_student.csv')

temp = pd.read_csv('easy_sponsor_info.csv')
student1 = df.iloc[1, 1:len(df.columns)]
matches = matty.classify_row(student1)
result = '\n'.join(matches)

client.chat_postMessage(channel='#hackbot', text="Hey <@U044RSJTX6F>! *Check out your top 5 companies:*")

for i in matches: 
    client.chat_postMessage(channel='#hackbot', text=">" + i) 

client.chat_postMessage(channel='#hackbot', text="Based on your interests we have matched you with these 5 companies. Check out their opportunities and head over to their tables soon :smile:!")
