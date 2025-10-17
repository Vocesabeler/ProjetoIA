import openai #

chave_api = "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"

openai.api_key = chave_api

def enviar_mensagem(mensagem):
    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-16k",
        messages = [
            {"role": "user", "content": mensagem}
        ],
    )

    return resposta["choices"][0]["message"]

