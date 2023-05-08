from key1 import KEY 
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader


from llama_index import download_loader, StorageContext
import os
import openai

os.environ['OPENAI_API_KEY'] = KEY 

documents = SimpleDirectoryReader("docs").load_data()
index = GPTVectorStoreIndex.from_documents(documents)

storage_context = StorageContext.from_defaults()
index.storage_context.persist()
print ("Done")