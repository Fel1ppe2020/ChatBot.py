api_key = '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'
import os
os.environ['GROQ_API_KEY'] = api_key
from langchain_groq import ChatGroq

chat = ChatGroq(model='llama-3.3-70b-versatile') 

print('Bem vindo ao ChatBot!')
print('Digite "sair" para encerrar o chat')
pergunta = input("Digite sua pergunta: ")
while True:
    if pergunta == 'sair':
        break
    else:
        resposta = chat.invoke(pergunta)
        print(resposta.content)
        pergunta = input("Digite sua pergunta: ")
print("Obrigado por usar o chatbot!")









    


