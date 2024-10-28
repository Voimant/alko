import requests
import argparse

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"


def neiro(question):
    # Собираем запрос
    token = 't1.9euelZqWmc6TzMuLzcyPlciZkciSlu3rnpWak52Jmp3InJ2NmMqey5GNjYzl8_ckcgFH-e9_WC4A_t3z92Qgf0b5739YLgD-zef1656Vmoybk8_HzpzLzJyayZSej4uX7_zF656Vmoybk8_HzpzLzJyayZSej4uX.HGPzD3_oIMZPvo8xQ7WWnheAiMfN9PUzr1WHjXuJg_3u5dHFPSu6pQmxMDTaL_vTq7IRZy95dgqEcQcmfO_tBw'

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




