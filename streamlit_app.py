import streamlit as st
import json
from typing import Sequence, List

from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import BaseTool, FunctionTool
from google.cloud import secretmanager

import os
import openai

import nest_asyncio

st.header("Experiment #0.1 💬 📚")




#client = secretmanager.SecretManagerServiceClient()
secret_name = st.secrets["API_KEY"]
#response = client.access_secret_version(request={"name": secret_name})
#secret_value = response.payload.data.decode('UTF-8')
#os.environ['OPENAI_API_KEY'] = secret_value


api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    print("Zmienna OPENAI_API_KEY jest ustawiona.")
else:
    print("Zmienna OPENAI_API_KEY nie jest ustawiona.")



st.write(secret_name)
