import streamlit as st
import json
from typing import Sequence, List
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import BaseTool, FunctionTool
from llama_index.core.agent import AgentRunner
from llama_index.agent.openai import OpenAIAgentWorker, OpenAIAgent

import os
import openai
import nest_asyncio

################################
########### CONFIG #############
################################

os.environ['OPENAI_API_KEY'] = st.secrets["API_KEY"]
api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI(model="gpt-3.5-turbo")

###################################
########### FUNCTIONS #############
###################################
    
def click_button():
    st.session_state.clicked = not st.session_state.clicked

def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b

def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


multiply_tool = FunctionTool.from_defaults(fn=multiply)
add_tool = FunctionTool.from_defaults(fn=add)
tools = [multiply_tool, add_tool]



######## Bootstraping agent
agent = OpenAIAgent.from_tools(tools, llm=llm, verbose=True)


#############################
########### GUI #############
#############################

if api_key:
    st.write("Zmienna OPENAI_API_KEY jest ustawiona.")
else:
    st.write("Zmienna OPENAI_API_KEY nie jest ustawiona.")


st.header("Experiment #0.1 💬 📚")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


######## Sidebar
st.sidebar.header("About")
st.sidebar.markdown(
    "LllamaIndex eperiment"
)

st.sidebar.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.sidebar.write('Button is on!')
else:
    st.sidebar.write('Button is off!')


###### Main content
# TESTS 
with st.expander("Moreinfo"):
    st.write('lorem ipsum')




st.write(">>> Response from agent:", str(agent.chat("Hi")))

st.write(">>> Do math: ", str(agent.chat("What is (121 * 3) + 42?")))
