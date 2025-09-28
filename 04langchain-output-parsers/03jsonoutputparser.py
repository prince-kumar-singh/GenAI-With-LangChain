from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me five fatcs about {topic}.\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Prompt = template.format()
# result = model.invoke(Prompt)
# final_result = parser.parse(result.content)
# print(final_result['name'])
# print(type(final_result))

chain = template | model | parser
result = chain.invoke({'topic':'space exploration'})
print(result)