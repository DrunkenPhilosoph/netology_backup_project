import requests
import pprint

class VK:

   def __init__(self, access_token, version='5.131'):
       self.token = access_token
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       print(self.params)
       return response.json()
   def get_photo(self, owner_id):
       url = f'https://api.vk.com/method/photos.get?owner_id={owner_id}&album_id=profile&photo_sizes=o&&access_token={self.token}&v={self.version}'
       response = requests.get(url)
       # pprint.pprint(response.json())

class Disk:
    sess = requests.Session()
    def __init__(self, access_token):
        self.access_token = access_token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.connect = requests.Session()
        self.connect.headers.update({"Content-Type": "application/json",
                                     "Accept": "application/json",
                                     "Authorization": self.access_token})


    def upload_for_link(self, name_folder, photo_url):
        data = {
            "path":name_folder,
            "url": photo_url
        }
        request = self.sess.post(f"{self.url}/upload", data=data)
        print(request.json())


access_token = 'vk1.a.QY5W0U2hK6wrFcPsVeLI7SjwAub_-xhx6oLSaqUn_AmpPfD_5wekBhbRu02Lmvub7XePbSl2mR5c1ee5F2JRJc4ZVj9RUXc1KQkq6jFyrF1OFxdeDKLJL9NNIv5c7MLp8YU_lnDunjnF6UJj8_AEb7iee8IZ9onkROFrjwgaI4b4C5pFk7XV5mh9JR6amcrY_EhIFVpd7o1FOylpzDHe7Q'
vk = VK(access_token)
disk = Disk(access_token='OAuth y0_AgAAAAAQZZiXAADLWwAAAADvX0H79qDDqCAIRJe4UmswPfJhaRoufBw')
disk.upload_for_link('https://sun1-28.userapi.com/impg/mGEyIFnkDp_BdiXMgxHQypwcePuwMJcYLn5I5g/jTdRpDUC_Us.jpg?size=510x765&quality=95&sign=e823dfe6c730863692710938c4c8c745&c_uniq_tag=Lfpwij154NQPNnpOdspvV5IqWXK4frPKrxCkSmXK4CQ&type=album','/data/evi1.jpeg')
vk.get_photo(62864744)
