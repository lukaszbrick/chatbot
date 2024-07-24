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


def click_button():
    st.session_state.button = not st.session_state.button


# Sidebar
st.sidebar.header(_("About"))
st.sidebar.markdown(_(
    "LllamaIndex eperiment"
))

st.sidebar.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.sidebar.write('Button is on!')
   
else:
    st.sidebar.write('Button is off!')


# Main content
with st.expander(_("Moreinfo")):
    st.write(secret_name)

