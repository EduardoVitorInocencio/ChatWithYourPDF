import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from openai import embeddings
from langchain import hub

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

load_dotenv(find_dotenv('.env'))

if __name__ =='__main__':
    print('Hi!')

    file_path = 'C:\\Users\\edinocencio\\ChatWithYourPDF\\2210.03629v3.pdf'
    loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(separator="\n") 
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local("faiss_index_react")

    new_vectorstore = FAISS.load_local(
        "faiss_index_react", embeddings, allow_dangerous_deserialization=True
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain   = create_stuff_documents_chain(
        OpenAI(), retrieval_qa_chat_prompt
    )
    retrieval_chain = create_retrieval_chain(
        new_vectorstore.as_retriever(), combine_docs_chain
    )

    res = retrieval_chain.invoke({"input":"What is ReAct in 3 sentences"})
    print(res['answer'])

