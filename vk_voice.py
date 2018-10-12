"""Vk API for send voices"""

import vk_requests
import json
import requests


def send(login, password, path, user_id, is_chat=False):
    api = vk_requests.create_api(app_id=5002187, login=login,
                                 password=password, scope=["messages", "docs"])
    voice = open(path, 'rb')
    upload_url = api.docs.getUploadServer(type='audio_message')['upload_url']

    response = requests.post(upload_url, files=dict(file=voice))
    response.raise_for_status()

    response_file = json.loads(response.text)['file']
    doc_response = api.docs.save(file=response_file)

    message = {'attachment': "doc{0}_{1}".format(doc_response[0]['owner_id'], doc_response[0]['id'])}
    if is_chat:
        message['chat_id'] = user_id
    else:
        message['user_id'] = user_id
    api.messages.send(**message)
