from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
    Baduza was born in East London, Eastern Cape, South Africa.[2] 
    She's the youngest of five children; her father worked as a 
    journalist and her mother as a government employee.[3] 
    After high school, Baduza moved to the United States to study
    at the New York Film Academy in the Los Angeles campus, 
    graduating in 2016 with an Associate of Fine Arts in Acting 
    for Film.[4][5] After graduation, she returned to South 
    Africa, where she worked primarily in theatre.[2] Baduza is 
    bilingual in Xhosa and English.[5]

    Baduza began her career primarily in theatre in South Africa, 
    including an all-female production of The Taming of the Shrew 
    at the Maynardville Open-Air Theatre.[2] She later appeared in 
    the South African crime thriller Trackers, which was M-Net's top 
    performing show for 2019.[6][7] In 2019, she was named a rising 
    star and one to watch by the Royal Television Society.[8] In 2020 
    she landed her first work outside of South Africa, playing the 
    character Sephy Hadley in the BBC One drama Noughts + Crosses.

    Her film work includes Slumber Party Massacre (2021) and The Woman 
    King (2022).

    In 2024, she guest-starred in the third season of Bridgerton as 
    Michaela Stirling, a genderflipped version of the book character 
    Michael Stirling.[9] She appeared as a regular cast member in the 
    fourth season[10] and was later confirmed as one of the leads for 
    the fifth season playing the love interest of Francesca Bridgerton, 
    portrayed by Hannah Dodd, making them the first same-gender central 
    romance of the series.[11]
    """

    summary_template = """
    Given the information {information} about a person I want
    you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables = ['information'], template = summary_template
    )

    llm = ChatOpenAI(temperature=0, model='gpt-4o-mini')
    chain = summary_prompt_template | llm
    response = chain.invoke(input={'information': information})
    print(response.content)


if __name__ == "__main__":
    main()
