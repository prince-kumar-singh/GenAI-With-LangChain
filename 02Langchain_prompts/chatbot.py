from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model =ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# We can use ChatPromptTemplate for dynamic messages as well
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit', 'q']:
        print("Exiting the chatbot. Goodbye!")
        break
    model_response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=model_response.content))
    print("AI: ", model_response.content)
print("Chat history:", chat_history)