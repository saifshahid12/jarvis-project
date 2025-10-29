from openai import OpenAI
client=OpenAI(api_key="sk-""proj-EdcWpcabok_XVimKFlrbu1QdkYjACKEm5uNBXkcTMGvfIdtZVsTK3swbIcmFp1C8hx1WGz9JzxT3BlbkFJ3FA8ysxOFAfL6-vjpE-xcDy7TbnYlXdMYoZcvOlrXTjosXifhnONTVOvzEalBkirUS34CQO-MA")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a virtual assistant name jarvis skilled in general task like google_cloud and alaxa "},
        {"role":"user","content":"what is coding"}
    ]
)

print(completion.choices[0].message)