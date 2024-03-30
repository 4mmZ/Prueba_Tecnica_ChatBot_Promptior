from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

file_path= "app/docs/about_us.txt"

""" Obtiene la información que sera consultada por el LLM """
read_file_chain = RunnableLambda(lambda _: {
    "context": open(file_path, "r").read()
})

""" Prompt del chatbot """
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

""" Modelo de OpenAI """
llm = ChatOpenAI()

""" Generación de respuesta basada en el contenido recuperado """
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
