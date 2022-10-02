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

client.chat_postMessage(channel='#hackbot', text='What industry are you interested in? Select all that apply')
client.chat_postMessage(channel='#hackbot', text='Fintech')
client.chat_postMessage(channel='#hackbot', text='Edtech')
client.chat_postMessage(channel='#hackbot', text='Gametech')
client.chat_postMessage(channel='#hackbot', text='Healthtech')
client.chat_postMessage(channel='#hackbot', text='Food/Agriculture')
client.chat_postMessage(channel='#hackbot', text='Social/Entertainment')
client.chat_postMessage(channel='#hackbot', text='Security')
client.chat_postMessage(channel='#hackbot', text='What are you interested in learning more about? Select all that apply')
client.chat_postMessage(channel='#hackbot', text='Machine Learning')
client.chat_postMessage(channel='#hackbot', text='Crypto')
client.chat_postMessage(channel='#hackbot', text='Quant')
client.chat_postMessage(channel='#hackbot', text='Blockchain')
client.chat_postMessage(channel='#hackbot', text='Artifical Intelligence')
client.chat_postMessage(channel='#hackbot', text='What are you interested in learning more about? Select all that apply')
client.chat_postMessage(channel='#hackbot', text='Frontend')
client.chat_postMessage(channel='#hackbot', text='Backenv')
client.chat_postMessage(channel='#hackbot', text='Full Stack')
client.chat_postMessage(channel='#hackbot', text='Design')
client.chat_postMessage(channel='#hackbot', text='Product Management')
client.chat_postMessage(channel='#hackbot', text='Data')
client.chat_postMessage(channel='#hackbot', text='What languages/frameworks do you have experience in? Select all that apply')
client.chat_postMessage(channel='#hackbot', text='Python')
client.chat_postMessage(channel='#hackbot', text='C')
client.chat_postMessage(channel='#hackbot', text='C++')
client.chat_postMessage(channel='#hackbot', text='Java')
client.chat_postMessage(channel='#hackbot', text='HTML/CSS')
client.chat_postMessage(channel='#hackbot', text='JavaScript')
client.chat_postMessage(channel='#hackbot', text='React')
client.chat_postMessage(channel='#hackbot', text='Flutter / Dart')
client.chat_postMessage(channel='#hackbot', text='Ruby on Rails')

matty = Classifier('easy_sponsor.csv')

df = pd.read_csv('easy_student.csv')
student1 = df.iloc[1, 1:len(df.columns)]
matches = matty.classify_row(student1)
