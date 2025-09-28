from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Set up model
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)
parser = StrOutputParser()

# First prompt: detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# Second prompt: summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text:\n{text}',
    input_variables=['text'] 
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
