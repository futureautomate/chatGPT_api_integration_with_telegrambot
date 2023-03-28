import openai
import apikeys

# load and set our key
openai.api_key = 'add your chat gpt api'

def getIntegrationContent():  
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "Write content on how quantum computing will change the world?"}]
  )

  reply_content = completion.choices[0].message.content
  return reply_content
  #print(reply_content) 
