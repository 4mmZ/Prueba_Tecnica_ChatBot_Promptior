from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
file_path= "docs/about_us.txt"

read_file_chain = RunnableLambda(lambda _: {
    "context": open(file_path, "r").read()
})


generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            f"Eres un asistente que se encarga de responder preguntas acerca de promptior.",
        ),
        (
            "human",
            """
Please answer the following query based on the provided context:
     
Query: {query}
---
<context>
{context}
</context>
""",
        ),
    ]
)

llm = ChatOpenAI()

chain = (
    RunnableParallel(
        {
            "query": RunnablePassthrough(),
            "context": read_file_chain,
        }
    )
    | generation_prompt
    | llm
).with_types(input_type=str)