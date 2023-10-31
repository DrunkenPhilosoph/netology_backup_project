import requests
import json

class VK:

    def __init__(self, access_token, version='5.131'):
        self.token = access_token
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def get_photo(self, owner_id, album_id='profile', count=5):
        """Метод загружает список ссылок из профиля VK, параметр count отвечает за количество возвращаемых ссылок
        фотографий. Параметр album_id=profile возвращает ссылки на аватарки, параметр album_id=wall возвращает ссылки
        со стены"""
        photo_dict = []
        url = f'https://api.vk.com/method/photos.get?owner_id={owner_id}&album_id={album_id}&photo_sizes=0' \
              f'&extended=1&access_token={self.token}&v={self.version}'
        response = requests.get(url).json()
        photos = response['response']['items']
        for photo in photos:
            target_photo = None
            TYPES = 'smxopqryzw'
            for photo_size in photo['sizes']:
                if not target_photo or TYPES.find(photo_size['type']) > TYPES.find(
                        target_photo['type']): target_photo = photo_size
            photo_dict.append({'url': target_photo['url'],
                               'type': target_photo["type"],
                               'width': target_photo["width"],
                               'height': target_photo["height"],
                               'likes': photo['likes']['count'],
                               })
        sorted_photo_dict = sorted(photo_dict, key=lambda x: x['height'])
        return_count_items = sorted_photo_dict[-count:]
        return return_count_items


class Disk:
    def __init__(self, access_token):
        self.access_token = access_token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.path = 'disk:'
        self.connect = requests.Session()
        self.connect.params.update({"Authorization": self.access_token})
        self.connect.headers.update({"Content-Type": "application/json",
                                     "Accept": "application/json",
                                     "Authorization": self.access_token})

    def upload_for_link(self, folder_path, photo_urls):
        log_create = []
        params_dir = {
            "path": f"{self.path}{folder_path}"
        }
        self.connect.put(self.url, params=params_dir).json()
        status_photo = 1
        count_name = 0
        names_list = []
        for photo in photo_urls:
            name = photo['likes']
            if name not in names_list:
                names_list.append(name)
            else:
                count_name += 1
            data = {
                "path": f"{self.path}{folder_path}{name}_{count_name}.jpg",
                "url": photo['url']
            }

            log_create.append({'file_name':f"{name}_{count_name}.jpg",
                                "size": photo['type']})
            request = self.connect.post(f"{self.url}/upload/", params=data)
            print(f'Загружена фотография {status_photo} из {len(photo_urls)}')
            status_photo += 1
        log_file = open('log_result.json', encoding='utf-8', mode='w')
        json.dump(log_create, log_file)
        log_file.close()


# Нужно ввести токен VK
access_token = ''
vk = VK(access_token)

# по умолчнию стоит выгрузка profile, можно заменить на wall
vk_id = int()
photo_album = vk.get_photo(vk_id, count=5, album_id='wall')

# Нужно ввести токен Яндекс диска
yandex_disk_token = ''
disk = Disk(access_token=yandex_disk_token)
disk.upload_for_link('/result/', photo_album)