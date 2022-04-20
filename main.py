import requests

import os

class YaUploader:
    def __init__(self, token:str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path:str):
        href_json = self._get_upload_link(file=file_path)
        href = href_json['href']
        response = requests.put(href, data=open(file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу: ')
    path, file = os.path.split(path_to_file)
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(file)

