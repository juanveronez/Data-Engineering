from json import load
from csv import DictReader, writer

class Data:
    def __init__(self, data):
        self.data = data

    def __get_file_type(path) -> str:
        'Get last part of file path, this information is the file extension'
        return path.split('.')[-1]

    def __read_json(path):
        with open(path, 'r') as file:
            return load(file)

    def __read_csv(path):
        with open(path, 'r') as file:
            reader = DictReader(file, delimiter=',')
            return [row for row in reader]
    
    @classmethod
    def read_data(cls, path):
        match cls.__get_file_type(path):
            case 'csv':
                data = cls.__read_csv(path)
            case 'json':
                data = cls.__read_json(path)
            
        return Data(data)
            
    def get_size(self) -> int:
        return len(self.data)
    
    def get_columns(self) -> list[str]:
        return list(self.data[0].keys())
    
    def rename_columns(self, key_mapping: dict[str, str]):
        self.data = [
            { key_mapping.get(key): value for key, value in row.items() }
            for row in self.data
        ]

    def join(datas: list):
        combined_data = []
        for el in datas:
            combined_data.extend(el.data)

        return Data(combined_data)
    
    def __get_table(self, headers: list[str]) -> list[list]:
        transformed_data = [headers]
        transformed_data.extend([[row.get(header, 'Indisponível') for header in headers] for row in self.data])

        return transformed_data
    
    def save_csv(self, path: str, headers: list[str]):
        data_table = self.__get_table(headers)

        with open(path, 'w') as file:
            csv_writer = writer(file)
            csv_writer.writerows(data_table)

        return path