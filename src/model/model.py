from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings

class HandleQA():
    def __init__(self,config):
        self.config = config
        self.embedding = HuggingFaceEmbeddings(model_name = config.embedding,cache_folder='cache')
        self.chroma = None  
        self.memory = None


    def split_context(self, files:list[str]) -> list[str]:
        """
        Split documents into chunks
        Args: 
            files(list[str]:None): list of documentations' local paths
        Return:
            list of chunks (list[str])
        """
        chunk_size = self.config.chunk_size
        chunk_overlap = self.config.chunk_overlap

        r_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )   
        chunks = []

        for file in files:
            with open(file,'r',encoding='utf8') as f:
                content = f.read()
                x = r_splitter.split_text(content)
                chunks += x 
                
        return chunks


    def store_db(self,chunks:list[str])->None:
        """
        add content
        """
        self.chroma = Chroma.from_texts(chunks,embedding = self.embedding)
    
    def get_query_and_chunk(self,query:str,similarity_function:str)->tuple[str,list[str]]:
        if similarity_function == 'max_marginal_relevance_search':
            similar_chunks = self.chroma.max_marginal_relevance_search(query,k = self.config.number_of_chunk)
    
        elif similarity_function == 'similarity':
            similar_chunks = self.chroma.similarity(query,k = self.config.number_of_chunk)
        
        contents = [content.page_content for content in similar_chunks]

        return query,contents
    
    def ask_gpt(self):
        pass
