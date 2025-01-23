from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_document_embedder():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-l6-v2")

def initialize_llm():
    return ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

def generate_prompt(chat_history, user_input, context):
    history_context = "\n".join(f"User: {msg['user']}\nAI: {msg['ai']}" for msg in chat_history)
    return (
        f"Previous Chat History:\n{history_context}\n\n"
        f"Relevant Context:\n{context}\n\n"
        f"User Question: {user_input}"
    )

def get_ai_response(prompt):
    chain = (
        ChatPromptTemplate.from_messages([("system", "You are a helpful AI assistant."), ("user", "{input}")])
        | initialize_llm()
        | StrOutputParser()
    )
    return chain.invoke({"input": prompt})