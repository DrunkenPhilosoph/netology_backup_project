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
       pprint.pprint(response.json())


access_token = 'vk1.a.QY5W0U2hK6wrFcPsVeLI7SjwAub_-xhx6oLSaqUn_AmpPfD_5wekBhbRu02Lmvub7XePbSl2mR5c1ee5F2JRJc4ZVj9RUXc1KQkq6jFyrF1OFxdeDKLJL9NNIv5c7MLp8YU_lnDunjnF6UJj8_AEb7iee8IZ9onkROFrjwgaI4b4C5pFk7XV5mh9JR6amcrY_EhIFVpd7o1FOylpzDHe7Q'
vk = VK(access_token)
vk.get_photo(62864744)