import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from CountDown import waitFor

def getSimilarDocuments(query):
    
    docs = st.session_state.db.similarity_search(query,3)
    return docs



for message in st.session_state.doc_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter the Query"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.doc_messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):

        list_relevant_docs = getSimilarDocuments(prompt)
        response = "["
        for doc_id in range(len(list_relevant_docs)):
            response += list_relevant_docs[doc_id].page_content
            response += "\n"
            
        response += "]"
        st.write(response)

    # Add assistant response to chat history
    st.session_state.doc_messages.append({"role": "assistant", "content": response})

test_button  = st.sidebar.button(label= "Test my Knowledge")
if test_button:
    waitFor(5)
    if st.session_state.embedding_function == "OpenAI":
        switch_page("QueryTabRAG")
    

    

