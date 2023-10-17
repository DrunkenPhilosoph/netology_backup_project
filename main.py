import requests

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()
   def get_photo(self, photo_size, album_id, ):
       url = f'https://api.vk.com/method/{}?owner_id={}&offset={}&count=200&v=5.131&access_token={}&v=5.131'


access_token = ''
user_id = '596289942'
vk = VK(access_token, user_id)
print(vk.users_info())