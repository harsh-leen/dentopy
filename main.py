import json
import os

input_directory = './input'

def process_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    
    data = json.loads(data)
    if not isinstance(data, list):
        raise ValueError('Data is not a list')  
    print(f'File contains {len(data)} items')

    pydantic_model_name = ''.join(part.capitalize() for part in file_path.split('/')[-1].split('.')[0].rstrip('s').split('_'))
    print(f'Pydantic model name: {pydantic_model_name}')

    keys = set()
    for item in data:
        keys.update(item.keys())
    
    keys_frequency = {}
    for item in data:
        for key in item.keys():
            if key not in keys_frequency:
                keys_frequency[key] = 0
            keys_frequency[key] += 1
    
    key_info_dict = {}
    for key, frequency in keys_frequency.items():
        type_str = 'None' if data[0].get(key) is None else type(data[0].get(key)).__name__
        key_info_dict[key] = {
            'frequency': frequency,
            'type': type_str
        }
    
    print(key_info_dict)





if __name__ == '__main__':
    files = os.listdir(input_directory)
    
    print(f'Found {len(files)} files in the input directory')
    for file_name in files:
        file_path = os.path.join(input_directory, file_name)
        if not file_path.endswith('.json'):
            print(f'Skipping a non-json file: {file_path}')
            continue
        print(f'Processing file: {file_path}')
        process_file(file_path)
        print(f'File processed: {file_path}')
        print("\n\n")
