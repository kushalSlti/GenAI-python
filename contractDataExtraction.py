from openai import OpenAI

OPENAI_API_KEY="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"
client = OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)