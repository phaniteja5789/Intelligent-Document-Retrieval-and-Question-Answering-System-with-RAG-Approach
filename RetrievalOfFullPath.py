import streamlit as st
import tempfile
import os

def retrieveFullPath(uploaded_files):
    temp_dir = tempfile.mkdtemp()
    uploaded_files_path = []
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        path = os.path.join(temp_dir, uploaded_file.name)
        with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())

        uploaded_files_path.append(path)
        
    for uploaded_file_path in uploaded_files_path:

        if uploaded_file_path not in st.session_state.uploaded_files:

            st.session_state.uploaded_files.append(uploaded_file_path) 
    
    for file in st.session_state.uploaded_files:
        if file not in uploaded_files_path:
            st.session_state.uploaded_files.remove(file)
