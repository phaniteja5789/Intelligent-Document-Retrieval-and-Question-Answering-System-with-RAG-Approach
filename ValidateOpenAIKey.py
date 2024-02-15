import openai

def ValidateOpenAIKEY(api_key):
    
    openai.api_key = api_key

    try:
        openai.models.list()

    except openai.AuthenticationError as e:
        return False
    else:
        return True
