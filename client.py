from openai import OpenAI
client=OpenAI(api_key="OPEN_AI_API")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a virtual assistant name jarvis skilled in general task like google_cloud and alaxa "},
        {"role":"user","content":"what is coding"}
    ]
)

print(completion.choices[0].message)