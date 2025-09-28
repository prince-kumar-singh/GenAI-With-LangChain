from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



prompt = PromptTemplate(
    template="write five intresting facts about {topic}.",
    input_variables=["topic"],
)
model= ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)

parser = StrOutputParser()

chain = prompt | model | parser   # | = pipe operator

result = chain.invoke({"topic": "space"})
print(result)

chain.get_graph().print_ascii()  # to visualize the chain steps