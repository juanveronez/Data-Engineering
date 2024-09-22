import requests as req
from os import getenv
from dotenv import load_dotenv
import pandas as pd
from math import ceil

class RepositoriesData:
    def __init__(self, owner: str):
        self.owner = owner
        self.base_url = 'https://api.github.com'
        self.access_key = self.__get_access_key()
        self.headers = {'X-GitHub-Api-Version': '2022-11-28',
                        'Authorization': self.access_key}

    def __get_access_key(self):
        load_dotenv()

        access_token = getenv('GITHUB_ACCESS_TOKEN')
        return f'Bearer {access_token}'
    
    def __count_repositories(self) -> int:
        url = f'{self.base_url}/users/{self.owner}'
        owner_data = req.get(url, headers=self.headers).json()
        
        return owner_data['public_repos']
    
    def __list_repositories(self):
        url = f'{self.base_url}/users/{self.owner}/repos'
        repos_list = []
        
        count_repos = self.__count_repositories()
        total_pages = ceil(count_repos / 100)
        
        for page_index in range(1, total_pages + 1):
            try:
                url_page = f'{url}?per_page=100&page={page_index}'
                repos = req.get(url_page, headers=self.headers).json()
                
                repos_list.append(repos)
            except:
                repos_list.append(None)

        return repos_list
    
    def __repos_names(self, repos_list: list) -> list[str]:
        return [repo['name'] for repos in repos_list for repo in repos]
    
    def __repos_languages(self, repos_list: list) -> list[str]:
        return [repo['language'] for repos in repos_list for repo in repos]
    
    def create_df_lenguages(self):
        repos_list = self.__list_repositories()
        repos_names = self.__repos_names(repos_list)
        repos_languages = self.__repos_languages(repos_list)

        df = pd.DataFrame()
        df['repository_name'] = repos_names
        df['language'] = repos_languages

        return df