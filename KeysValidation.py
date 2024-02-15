import streamlit as st
from ValidateOpenAIKey import ValidateOpenAIKEY
from ValidateHuggingFaceKey import ValidateHuggingFaceKEY

def ValidateKeyBasedOnSelection(validate_api_button,api_key_selection,api_key):

    if validate_api_button:
            if api_key_selection == "OPENAI":
                
                # validate OpenAI key
                st.session_state.is_validate_key = ValidateOpenAIKEY(api_key)
                st.session_state.embedding_function = "OpenAI"

            else:

                # Validate HuggingFace Key

                if ValidateHuggingFaceKEY(api_key) != 200:
                    st.session_state.is_validate_key = False
                else:
                    st.session_state.is_validate_key = True
                    st.session_state.embedding_function = "HuggingFace"
        
            if not st.session_state.is_validate_key:
                    st.sidebar.error(f'Entered {api_key_selection} key is wrong', icon="🚨")
