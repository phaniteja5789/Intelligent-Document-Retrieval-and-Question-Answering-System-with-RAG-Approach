This project is Document Search using Vector Embeddings and Vector Data Base using LLM.

**Framework Used**
1.) LangChain ==> To Connect to LLM
2.) Stream-lit ==> For developing UI



**Models Used**

  **OpenAI
  HuggingFace**

  **Embeddings Model**

    **text-embedding-ada-002
    all-MiniLM-L6-v2**

  **OpenAI**

    **gpt-turbo-3.5**

**Vector DataBase**

  **Chroma**


This project mainly deals with 4 stages
1.) Stage-1 ==> Validation of API Key ==> Here we are providing leverage to the user to either use OpenSource Models from Hugging Face or OpenAI models using OpenAI API Key
2.) Stage-2 ==> Based on the User Selection of Model, He needs to select the documents of any type for which the embeddings need to be performed and the embeddings will be stored in the vector database
3.) Stage-3 ==> Once the vectors have been stored, the user needs to query the keywords on which the similar documents will be fetched from the database
4.) Stage-4 ==> We also provide, the feasibility to the user, to test the knowledge by using RAG(pattern) (**Retrieval Augmented Generation**)


**Stage-1**

<img width="960" alt="image" src="https://github.com/phaniteja5789/VectorDocumentSearch/assets/36558484/be2132a8-aca1-4b34-a8e3-5d3b0ba9a182">

In the Left side Pane, we are providing the user either to select the OpenAI or Hugging Face.
Based on the selection, the text box below and the button will vary, either to provide an OpenAI API key or the HuggingFace API key
If an OpenAI key is provided, then the OpenAI key will be validated, if the API key is valid then the Right Pane Controls will be enabled
If the Hugging Face key is provided, then the Hugging Face will be validated, if the Hugging Face key is valid then the Right Pane Controls will be enabled
The below screenshot is for reference

<img width="959" alt="image" src="https://github.com/phaniteja5789/VectorDocumentSearch/assets/36558484/31e9c78a-c6c9-4990-a307-99a946052291">

**Stage-2**
In the Right side Pane, we allow the user to browse the files of different file types like (pptx,pdf,csv,txt)
Once the files are selected, the respective file names will be populated below the control, 
Once the documents have been uploaded, then we need to embed the documents and store the embeddings in the database
<img width="959" alt="image" src="https://github.com/phaniteja5789/VectorDocumentSearch/assets/36558484/db569375-0b6c-4870-949b-dac499bb0cfb">

We allow the user to embed the documents.
Once the documents have been embedded the below message will be shown
<img width="602" alt="image" src="https://github.com/phaniteja5789/VectorDocumentSearch/assets/36558484/f67ad572-f8ac-4e29-b2f8-617b6f62c10e">


    
  
