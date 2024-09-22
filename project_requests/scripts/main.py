from owner_repositories import RepositoriesData
from repository_loader import RepositoryLoader

amzn_repos = RepositoriesData('amzn').create_df_lenguages()
amzn_repos.to_csv('../data_processed/amzn_repos.csv', index=False)

netflix_repos = RepositoriesData('netflix').create_df_lenguages()
netflix_repos.to_csv('../data_processed/netflix_repos.csv', index=False)

spotfy_repos = RepositoriesData('spotify').create_df_lenguages()
spotfy_repos.to_csv('../data_processed/spotify_repos.csv', index=False)

apple_repos = RepositoriesData('apple').create_df_lenguages()
spotfy_repos.to_csv('../data_processed/apple_repos.csv', index=False)

languages_repo = RepositoryLoader('juanveronez', 'companies-languages')
languages_repo.create()

languages_repo.add_file('amzn_repos.csv', '../data_processed/amzn_repos.csv')
languages_repo.add_file('netflix_repos.csv', '../data_processed/netflix_repos.csv')
languages_repo.add_file('spotify_repos.csv', '../data_processed/spotify_repos.csv')
languages_repo.add_file('apple_repos.csv', '../data_processed/apple_repos.csv')

