import requests
import pprint
import time


class VK:

    def __init__(self, access_token, version='5.131'):
        self.token = access_token
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        # print(self.params)
        return response.json()

    def get_photo(self, owner_id, album_id='profile'):
        photo_list = []
        url = f'https://api.vk.com/method/photos.get?owner_id={owner_id}&album_id={album_id}&photo_sizes=1&&access_token={self.token}&v={self.version}'
        response = requests.get(url).json()
        photos = response['response']['items']
        for photo in photos:
            target_photo = None
            TYPES = 'smxopqryzw'
            for photo in photo['sizes']:
                if not target_photo or TYPES.find(photo['type']) > TYPES.find(
                    target_photo['type']): target_photo = photo
            photo_list.append(target_photo['url'])
        return photo_list


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
        params_dir = {
            "path": f"{self.path}{folder_path}"
        }
        self.connect.put(self.url, params=params_dir).json()
        count_photo = len(photo_urls)
        for photo in photo_urls:
            data = {
                "path": f"{self.path}{folder_path}{count_photo}.jpg",
                "url": photo
            }
            request = self.connect.post(f"{self.url}/upload/", params=data)
            count_photo += 1


access_token = 'vk1.a.QY5W0U2hK6wrFcPsVeLI7SjwAub_-xhx6oLSaqUn_AmpPfD_5wekBhbRu02Lmvub7XePbSl2mR5c1ee5F2JRJc4ZVj9RUXc1KQkq6jFyrF1OFxdeDKLJL9NNIv5c7MLp8YU_lnDunjnF6UJj8_AEb7iee8IZ9onkROFrjwgaI4b4C5pFk7XV5mh9JR6amcrY_EhIFVpd7o1FOylpzDHe7Q'
vk = VK(access_token)

# по умолчнию стоит выгрузка profile, можно заменить на wall, saved
photo_album = vk.get_photo(208804302)

disk = Disk(access_token='OAuth y0_AgAAAAAQZZiXAADLWwAAAADvX0H79qDDqCAIRJe4UmswPfJhaRoufBw')
disk.upload_for_link('/result/', photo_album)
