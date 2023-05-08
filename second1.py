from llama_index import StorageContext, load_index_from_storage
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
import os
import openai

from key1 import KEY 
import os
import openai

os.environ['OPENAI_API_KEY'] = KEY 

storage_context = StorageContext.from_defaults(persist_dir='./storage')

index = load_index_from_storage(storage_context)
query_engin = index.as_query_engine() 

question = input("Enter the question ")
response = query_engin.query(question)
print ("\n", response)

