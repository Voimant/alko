import requests
import json
import argparse

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

def update_token():
    url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
    data ='{"yandexPassportOauthToken":"y0_AgAAAAB2FRVuAATuwQAAAAEWRJwRAACLbspsHf1FXYhkkQjdW1nsEbYu6g"}'

    response = requests.post(url, data=data)
    file = (response.json())
    with open('aim.json', 'w') as f:
        json.dump(file, f)



def neiro(question):
    with open('aim.json') as f:
        data = json.load(f)
        token = data['iamToken']
    # Собираем запрос
    data = {}
    # Указываем тип модели
    data["modelUri"] = "gpt://b1g91ecm1m52tvmskjp0/yandexgpt/rc"
    # Настраиваем опции
    data["completionOptions"] = {"temperature": 0.3, "maxTokens": 1000}
    # Указываем контекст для модели
    data["messages"] = [
        {"role": "system", "text": "напиши ответ"},
        {"role": "user", "text": f"{question}"},
    ]

    # Отправляем запрос
    response = requests.post(
        URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        },
        json=data,
    ).json()

    # Распечатываем результат
    return response['result']['alternatives'][0]['message']['text']




