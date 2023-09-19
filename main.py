from src.model.model import HandleQA
from config.config import config
import os 

files = os.listdir('data')
files = [os.path.join('data',file) for file in files]
chat = HandleQA(config)

print(chat.split_context(files))