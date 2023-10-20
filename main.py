# main.py

import streamlit as st
import langchain as lc
from agents.openai_agent import OpenAIAgent
from utils.memory_manager import save_memory, load_memory

# Initialize LangChain and OpenAI Agent
chain = lc.Chain()
openai_agent = OpenAIAgent()
conversation_chain = lc.ConversationChain()
conversation_chain.add(openai_agent)
chain.add(conversation_chain)

# Load existing conversation memory if available
memory_file_path = 'memory.pkl'
memory_buffer = load_memory(memory_file_path) if os.path.exists(memory_file_path) else lc.ConversationBufferMemory()
conversation_chain.set_memory(memory_buffer)

# Streamlit Interface
st.title('ConvoMemory')

user_input = st.text_input("You: ")
if user_input:
    response = conversation_chain.process(lc.Message(text=user_input))
    st.write(f'AI: {response.text}')
    # Save conversation memory after each interaction
    save_memory(memory_buffer, memory_file_path)
