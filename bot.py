from distutils.command.config import config
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
student1 = df.iloc[1, 1:len(df.columns)]
matches = matty.classify_row(student1)
result = '\n'.join(matches)
client.chat_postMessage(channel='#hackbot', text=result)