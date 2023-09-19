from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name = 'keepitreal/vietnamese-sbert',cache_folder='cache')
text = "This is a test document."
query_result = embeddings.embed_query(text)
print(query_result)