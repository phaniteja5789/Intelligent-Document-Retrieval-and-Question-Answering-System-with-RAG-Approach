import streamlit as st
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI

def getRetriever():
    
    retriever = st.session_state.db.as_retriever(search_type = "similarity", search_kwargs = {'k':3})
    return retriever

for message in st.session_state.rag_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter the Query"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.rag_messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):

        retriever = getRetriever()
        qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key = st.session_state.open_ai_key), chain_type="stuff", retriever=retriever, return_source_documents=False)
        response = qa({"query":prompt})
        st.session_state.rag_messages.append({"role": "assistant", "content": response})
        st.write(response)
        

        
        
