import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
import requests

class Models:
    def __init__(self):
        pass

    def initialize_models(self, api_key):
        try:
            embeddings_model = OpenAIEmbeddings()
            chat = ChatOpenAI(model='gpt-4o-mini')
            
            diretorio = 'arquivos/chat_retrieval_db'
            vectordb = Chroma(
                embedding_function=embeddings_model,
                persist_directory=diretorio
            )
            
            return chat, vectordb
        except Exception as e:
            st.error(f"Erro ao inicializar modelos: {str(e)}")
            return None, None
        
    def generate_image(self, prompt, api_key):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "model": "dall-e-3",
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024",
            "quality": "standard",
            "response_format": "url"
        }
        
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            return response.json()['data'][0]['url']
        else:
            raise Exception(f"Error: {response.text}")


        