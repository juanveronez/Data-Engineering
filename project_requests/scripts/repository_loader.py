import requests as req
import base64

from os import getenv
from dotenv import load_dotenv

class RepositoryLoader:
    def __init__(self, owner: str, repo_name: str):
        self.owner = owner
        self.repo_name = repo_name
        self.base_url = 'https://api.github.com'
        self.access_key = self.__get_access_key()
        self.headers = {'X-GitHub-Api-Version': '2022-11-28',
                        'Authorization': self.access_key}

    def __get_access_key(self):
        load_dotenv()

        access_token = getenv('GITHUB_ACCESS_TOKEN')
        return f'Bearer {access_token}'
    
    def create(self):
        data = {
            'name': self.repo_name,
            'description': 'Repositorio com as linguagens de prog. de algumas empresas.',
            'private': True
        }

        request = req.post(f'{self.base_url}/user/repos',
                           json=data, headers=self.headers)
        
        print('Status code:', request.status_code)

    def add_file(self, file_name, file_path):
        encoded_file = self.__encode_file(file_path)
        url = f'{self.base_url}/repos/{self.owner}/{self.repo_name}/contents/{file_name}'

        data = {
            'message': 'Adicionando um novo arquivo',
            'content': encoded_file.decode('utf-8')
        }

        response = req.put(url, json=data, headers=self.headers)
        print('Update status:', response.status_code)

    
    def __encode_file(self, file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()

        return base64.b64encode(file_content)
    
    def delete(self):
        url = f'https://api.github.com/repos/{self.owner}/{self.repo_name}'
        response = req.delete(url, headers=self.headers)
        print(f"Delete repo status: {response.status_code}")