from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import UnstructuredFileLoader,TextLoader,UnstructuredPDFLoader,UnstructuredWordDocumentLoader,CSVLoader,UnstructuredPowerPointLoader
import streamlit as st


def LoadDocumentsIntoChroma():

    for file in st.session_state.uploaded_files:

        file_extension_list= file.split('.')
        file_extension = file_extension_list[len(file_extension_list) - 1]
        lowercase_file_extension = file_extension.lower()
        data = None
        loader = None
        if lowercase_file_extension == "csv":

            # Load CSV file using CSV Loader
            loader = CSVLoader(file_path=file)

        elif lowercase_file_extension == "pptx":

            # Load ppt file using PPT loader
            loader = UnstructuredFileLoader(file_path= file)

        elif lowercase_file_extension == "docx":

            # Load word file using docx loader
            loader = UnstructuredWordDocumentLoader(file_path=file)

        elif lowercase_file_extension == "txt":

            # load txt file using TXT loader
            loader = TextLoader(file_path= file)

        elif lowercase_file_extension == "pdf":

            # load pdf file using pdf loader
            loader = UnstructuredFileLoader(file_path= file)

        data = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        docs = text_splitter.split_documents(data)
        st.session_state.db.add_documents(documents = docs)


