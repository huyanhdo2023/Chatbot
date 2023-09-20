from src.model.model import HandleQA
from config.config import config
import os 

path = r'C:\Users\anh.do\Desktop\chatbot\data\drive-download-20230920T080751Z-001\Tăng_trưởng_GDP_Việt_Nam_năm_2023'
files = os.listdir(path)
files = [os.path.join(path,file) for file in files]
chat = HandleQA(config)

# chunks = chat.split_context(files)
# print(chunks)
# print(len(chunks))
# print(len(chunks))
# chat.store_db(chunks)
x = chat.ask_gpt('Tăng trưởng GDP Việt Nam năm 2023',files)
print(x)
# print(chat.chroma._collection.count())
# u,v= chat.get_query_and_chunk('Thông tin chứng khoán')
# print(u)
# print(v)