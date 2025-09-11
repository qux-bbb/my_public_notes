# python调用本地Ollama

这里使用兼容OpenAI的api：
```python
import requests

url = "http://localhost:11434/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

data = {
    "temperature": 0,
    "model": "qwen3:8b",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

输出：
```json
{
    "id": "chatcmpl-440",
    "object": "chat.completion",
    "created": 1757548927,
    "model": "qwen3:8b",
    "system_fingerprint": "fp_ollama",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": '<think>\nOkay, the user said "Hello!" so I should respond in a friendly and welcoming manner. Let me make sure to acknowledge their greeting and offer assistance. I should keep it simple and positive. Maybe something like, "Hello! How can I assist you today?" That sounds good. It\'s polite and opens the door for them to ask for help. I don\'t need to add anything else unless they have a specific question. Let me check for any typos or errors. Nope, looks good. Alright, ready to respond.\n</think>\n\nHello! How can I assist you today? 😊',
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 10, "completion_tokens": 123, "total_tokens": 133},
}
```


2025/9/12
