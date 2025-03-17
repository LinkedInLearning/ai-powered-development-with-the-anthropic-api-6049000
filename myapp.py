import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="",
)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=8192,
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": "Tell me what the days of the week are"
        }
    ]
)
print(message.content[0].text)