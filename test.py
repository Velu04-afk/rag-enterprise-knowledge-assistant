import cohere

co = cohere.ClientV2("wJjhtebfQ08cRFOoMNJFqW1jyZZbH1LyWTy51acu")
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "hello world!"}]
)

print(response)
