from processamento_dados import Data

path_json = 'pipeline_dados/data_raw/dados_empresaA.json'
dados_empresaA = Data.read_data(path_json)

path_csv = 'pipeline_dados/data_raw/dados_empresaB.csv'
dados_empresaB = Data.read_data(path_csv)


print('-'*30)
print('LEITURA DE DADOS')

print('Registro Empresa A:', dados_empresaA.data[0])
print('Colunas Empresa A:', dados_empresaA.get_columns())
print('Tamanho Empresa A:', dados_empresaA.get_size())
print()

print('Registro Empresa B:', dados_empresaB.data[0])
print('Colunas Empresa B:', dados_empresaB.get_columns())
print('Tamanho Empresa B:', dados_empresaB.get_size())
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

dados_empresaB.rename_columns(key_mapping)

print('Registro renomeado:', dados_empresaB.data[0])
print('Colunas renomeadas', dados_empresaB.get_columns())

fusao = Data.join([dados_empresaA, dados_empresaB])
print('Tamanho Fusao:', fusao.get_size())

print('-'*30)
print('SALVANDO OS DADOS')

path_dados_combinados = 'pipeline_dados/data_processed/dados_combinados.csv'
headers = list(key_mapping.values())

target_path = fusao.save_csv(path_dados_combinados, headers)
print(target_path)