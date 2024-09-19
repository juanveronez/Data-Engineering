from json import load
from csv import DictReader, writer

def leitura_json(path):
    with open(path, 'r') as file:
        return load(file)

def leitura_csv(path):
    with open(path, 'r') as file:
        reader = DictReader(file, delimiter=',')
        return [row for row in reader]
    
def leitura_dados(path, file_type):
    match file_type:
        case 'csv':
            return leitura_csv(path)
        case 'json':
            return leitura_json(path)


def get_columns(data: list[dict]) -> list[str]:
    return list(data[0].keys())

def rename_columns(data: list[dict], key_mapping: dict[str, str]):
    return [
        { key_mapping.get(key): value for key, value in row.items() }
        for row in data
    ]

def data_size(data: list) -> int:
    return len(data)

def join(dataA: list, dataB: list) -> list:
    combined_data = []
    combined_data.extend(dataA)
    combined_data.extend(dataB)
    
    return combined_data

def transform_data_to_table(data: list[dict], key_mapping: dict[str, str]) -> list[list]:
    headers = list(key_mapping.values())

    transformed_data = [headers]
    transformed_data.extend([[row.get(header, 'Indisponível') for header in headers] for row in data])

    return transformed_data

def save_csv(path: str, data: list[list]):
    with open(path, 'w') as file:
        csv_writer = writer(file)
        csv_writer.writerows(data)


path_json = 'pipeline_dados/data_raw/dados_empresaA.json'
path_csv = 'pipeline_dados/data_raw/dados_empresaB.csv'

print('-'*30)
print('LEITURA DE DADOS')

dados_empresaA = leitura_dados(path_json, 'json')
colunas_empresaA = get_columns(dados_empresaA)
tamanho_empresaA = get_columns(dados_empresaA)

print('Registro Empresa A:', dados_empresaA[0])
print('Colunas Empresa A:', colunas_empresaA)
print('Tamanho Empresa A:', tamanho_empresaA)
print()

dados_empresaB = leitura_dados(path_csv, 'csv')
colunas_empresaB = get_columns(dados_empresaB)
tamanho_empresaB = get_columns(dados_empresaB)


print('Registro Empresa B:', dados_empresaB[0])
print('Colunas Empresa B:', colunas_empresaB)
print('Tamanho Empresa B', tamanho_empresaB)
print()

print('-'*30)
print('TRANSFORMACAO DE DADOS')

key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB = rename_columns(dados_empresaB, key_mapping)

print('Registro renomeado:', dados_empresaB[0])
print('Colunas renomeadas', get_columns(dados_empresaB))

fusao = join(dados_empresaA, dados_empresaB)
print('Tamanho Fusao:', data_size(fusao))

print('-'*30)
print('SALVANDO OS DADOS')


tabela_fusao = transform_data_to_table(fusao, key_mapping) #transformacao puramente para salvamento dos dados
print('Headers:', tabela_fusao[0])
print('Registro:', tabela_fusao[1])


path_dados_combinados = '../data_processed/dados_combinados.csv'
save_csv(path_dados_combinados, tabela_fusao)
print(path_dados_combinados)