import os, asyncio
from dotenv import load_dotenv
from revChatGPT.Official import Chatbot

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path)

religion = "Protestant"
inspiration = "Tim Keller and C.S. Lewis"
initialPrompt = "Respond to every prompt I give you as a {} pastor. This pastor is well read in {}, but does not mention them. Your name is Pastor AI. Your responses will be kind, encouraging, and personal. If a question has no religious relevance, respond with, \"Sorry, this question is not within my domain.\" If the question is negative, ask them if they want prayer. Prompt: Hello".format(religion, inspiration)

class Prompt:
    def __init__(self, religion="Protestant", inspiration="Tim Keller and C.S. Lewis") -> None:
        self.religion = religion
        self.inspiration = inspiration
        self.initialPrompt = "Respond to every prompt I give you as a {} pastor. This pastor is well read in {}, but does not mention them. Your name is Pastor AI. Your responses will be kind, encouraging, and personal. If a question has no religious relevance, respond with, \"Sorry, this question is not within my domain.\" If the question is negative, ask them if they want prayer. Prompt: Hello"
        self.prompt = self.getInitialPrompt()
        self.chatbot = Chatbot(os.getenv("OPENAI_API_KEY"))
        # self.answer = self.chatbot.ask(self.prompt)
    
    def getInitialPrompt(self):
        return self.initialPrompt.format(self.religion, self.inspiration)

    def setInspiration(self, inspiration):
        self.inspiration = inspiration

    def setReligion(self, religion):
        self.religion = religion

    def setPrompt(self, prompt):
        self.prompt = prompt

    def ask(self):
        self.answer = self.chatbot.ask(self.prompt)
        return self.answer

prompt = Prompt(religion, inspiration)

# async def main():
#     while (True):
#         print(await prompt.ask())
#         prompt.setPrompt(input())

# asyncio.run(main())