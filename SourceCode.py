# Importing Required Packages
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from KeysValidation import ValidateKeyBasedOnSelection
from RetrievalOfFullPath import retrieveFullPath
from InitializationOfSessionVariables import initialization
from LoadDocumentsIntoVectorDB import LoadDocumentsIntoChroma
from CountDown import waitFor
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings,OpenAIEmbeddings

# Persisting the Vector DataBase Directories
# Chroma_directory_1 ==> This is used when user selects the OpenAI LLM
# Chroma_directory_2 ==> This is used when user selects the Hugging Face LLM
# The reason for using 2 directories because, both the LLM's will return the vectors of different dimensions
chroma_directory_1 = 'db1/'
chroma_directory_2 = 'db2/'


# Initialization of Session Variables for the StreamLit
initialization()


api_key_selection = st.sidebar.radio("Choose from where the model needs to be used",["OPENAI","HuggingFACE"])

def CreateMainUI():
    uploaded_files = st.file_uploader("Choose a required files", accept_multiple_files=True, disabled= not st.session_state.is_validate_key)
    retrieveFullPath(uploaded_files)

def retrieveSimilarityDocuments():
    st.write("Documents has been loaded into the Vector DataBase")
    # waiting for 5 secs to navigate to next page
    waitFor(5)
    switch_page("RetrieveSimilarityDocuments")  
    
# Validation of Key based on provided Key
if api_key_selection:
    
    api_key = st.sidebar.text_input(label = f"Provide the {api_key_selection} API KEY", type="password")

    validate_api_button = st.sidebar.button(label=f"Validate {api_key_selection} key")

    ValidateKeyBasedOnSelection(validate_api_button,api_key_selection,api_key)

    
CreateMainUI()
embed_button = st.button(label= "embed the files", disabled = not st.session_state.is_validate_key)        
if embed_button:
    
    # create the open-source embedding function
    embedding_function = None

    if st.session_state.embedding_function == "OpenAI":
        embedding_function = OpenAIEmbeddings(openai_api_key = api_key, model = "text-embedding-ada-002")
        st.session_state.db = Chroma(persist_directory=chroma_directory_1, embedding_function=embedding_function)
        st.session_state.open_ai_key = api_key
    else:
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        st.session_state.db = Chroma(persist_directory=chroma_directory_2, embedding_function=embedding_function)

    LoadDocumentsIntoChroma()
    retrieveSimilarityDocuments()

