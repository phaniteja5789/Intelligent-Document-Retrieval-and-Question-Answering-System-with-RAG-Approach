import streamlit as st

def initialization():
    
    if "is_validate_key" not in st.session_state:
        st.session_state.is_validate_key = False

    if "folder_path" not in st.session_state:
        st.session_state.folder_path = None

    if "embedding_function" not in st.session_state:
        st.session_state.embedding_function = None

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []

    if "db" not in st.session_state:
        st.session_state.db = None

    if "doc_messages" not in st.session_state:
        st.session_state.doc_messages = []

    if "rag_messages" not in st.session_state:
        st.session_state.rag_messages = []

    if "api_key" not in st.session_state:
        st.session_state.open_ai_key = None