import os, warnings
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory, ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq

warnings.filterwarnings("ignore")

def main():
    load_dotenv()
    
    if os.getenv("GROQ_API_KEY") is None or os.getenv("GROQ_API_KEY") == "":
        print('Your Groq API key is not set. Please set it in the .env file.')
        exit(1) 
    else:
        print('Groq API key is set.')
    
    llm = ChatGroq(model='llama-3.3-70b-versatile', api_key=os.getenv("GROQ_API_KEY"))
    conversation = ConversationChain(
        llm=llm,
        verbose=False,
        memory=ConversationEntityMemory(llm=llm),
        prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE
    )
    
    print('Hello, I am ChatGroq CLI!')
    
    while True:
        user_input = input("> ")
        ai_response = conversation.predict(input=user_input)
        
        print("\nAssistant\n", ai_response)


if __name__ == "__main__":
    main()