# from src.model.model import HandleQA
# from config.config import config
# import os 
# from src.get_data.user_query import get_data
# path = r'C:\Users\anh.do\Desktop\chatbot\data\drive-download-20230920T080751Z-001\data'
# query = 'số người tử vong trong vụ cháy chung cư mini'
# get_data(query,query_folder = path)
# files = os.listdir(path)
# files = [os.path.join(path,file) for file in files]
# chat = HandleQA(config)

# x = chat.ask_gpt('quốc gia nào vô địch chung kết bóng đá nam',files)
# print(x)
# from fastapi import FastAPI
# from pydantic import BaseModel
# from src.database import engine
# from src.schemas import Chat
# from src.model.model import HandleQA
# from config.config import config
# from dotenv import load_dotenv,find_dotenv
# from src.get_data.user_query import get_data
# _ = load_dotenv(find_dotenv())
# import os 
# app = FastAPI()

# bot = HandleQA(config)

# @app.get('/')
# def hello_world():
#     return {
#         'res':'hello world'
#     }


# @app.post("/chat")
# def chat(req:Chat):
#     path = r'C:\Users\anh.do\Desktop\chatbot\data\drive-download-20230920T080751Z-001\data'
#     get_data(req.question,query_folder = path)

#     files = os.listdir(path)
#     files = [os.path.join(path,file) for file in files]

#     answer = bot.ask_gpt(req.question,files)
#     return {'answer':answer}