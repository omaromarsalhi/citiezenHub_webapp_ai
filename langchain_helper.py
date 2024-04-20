from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def generate_produxt_description(title):
    llm = OpenAI(temperature=0.8)

    prompt_template_name = PromptTemplate(
        input_variables = ['title'],
        template = """
            I have a {title} witch is a product's title for sale.
            give me a descreption that i can put on that product to get peaple to buy it.
        """
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    ai_response = name_chain({'title': title})
    response = ai_response.get('text', '')

    return response
