from pprint import pprint
import requests

# Домашнее задание №1
# url = 'https://akabab.github.io/superhero-api/api/all.json'
#
# def test_request(url):
#     response = requests.get(url)
#     hero_list = response.json()
#     for hero in hero_list:
#         if hero['name'] == 'Hulk':
#             hulk = hero['powerstats']['intelligence']
#         elif hero['name'] == 'Captain America':
#             cap_am = hero['powerstats']['intelligence']
#         elif hero['name'] == 'Thanos':
#             thanos = hero['powerstats']['intelligence']
#     print(max(thanos, cap_am, hulk))
#
#     pprint(f'Интеллект: Капитан Америка {cap_am}, Халк {hulk}, Танос {thanos}')
#     if hulk > thanos and hulk > cap_am:
#         print('Халк умнее всех!', hulk)
#     elif cap_am > hulk or cap_am > thanos:
#         print('Капитан Америка умнее всех!', cap_am)
#     elif thanos > hulk or thanos > cap_am:
#         print('Танос умнее всех!', thanos)
#
# if __name__ == '__main__':
#     test_request(url)

# Задание №2

import os

# current = os.getcwd()
# folder_name1 = 'new_dir'
# file_name = 'test_file.txt'
# full_path = os.path.join(current, folder_name1, file_name)
# current - определение папки в которой находится файл main.py;
# folder_name1 - директория, которая находится на одном уровне с файлом main.py;
# file_name - название файла, к которому мы строим путь;
# full_path - собираем путь по цепочке.

class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        result = self._get_upload_link(disk_file_path=disk_file_path)
        href = result.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    TOKEN = ""
    path_to_file = r'F:\new\test_file.txt'
    ya = YandexDisk(token=TOKEN)
    # pprint(ya.get_files_list())
    pprint(ya.upload_file_to_disk("Netology/test_file.txt", path_to_file))



