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

client.chat_postMessage(channel='#bot-testing', text='Hello World!')

matty = Classifier('sample_table_sponsor.csv')
df = pd.read_csv('sample_table_student.csv')
student1 = df[1, 1:len(df.columns)]
matches = matty.classify_row(student1)
print(matches)
