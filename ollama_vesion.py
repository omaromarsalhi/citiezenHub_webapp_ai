import json
import requests
import subprocess


# GITIGNORE
# url='https://ab7e-104-155-185-76.ngrok-free.app'


def execute_cmd(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    except Exception as e:
        print(f"Error executing command: {e}")

def generateBasedOnText(prompt,prompt2,url):
    r = requests.post(url+'/api/generate',
                    json={
                        'model': 'mistral',
                        'prompt': 'is this paragraph "'+prompt+'" speaks about "'+prompt2+'" , please answer with yes or no',
                    },
                    stream=True)
    r.raise_for_status()
    return r.content.decode('utf-8');


def generateBasedOnCategory(prompt,prompt2,url):
    r = requests.post(url+'/api/generate',
                    json={
                        'model': 'mistral',
                        'prompt': 'is the main objext in this paragraph "'+prompt+'" falls under this category "'+prompt2+'" , please answer with yes or no ',
                    },
                    stream=True)
    r.raise_for_status()
    return r.content.decode('utf-8');



# image_url="E:\\usersImg\\0e4525b5-2aa0-469f-9aa6-a36ea7765481.png"
# commands=f"set OLLAMA_HOST={url}&ollama run llava only describe the image content  {image_url}"
# response=execute_cmd(commands)


def finetune_text(text):
    tuned_response=''
    for string in text.split('\n'):
        if string.find("failed")==-1:
            tuned_response+=string
    return tuned_response


def finetune_resp(text):
    newResp=text.split('\n')
    del newResp[-1]
    final_response=''
    for i in newResp:
        body = json.loads(i)
        final_response+=body.get('response', '')
    return final_response

# print(tuned_response)
# generateBasedOnText(tuned_response,"Golf")
