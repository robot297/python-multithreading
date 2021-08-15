def dictionary_writer(key, item : str):
    dictionary = {key: item}
    return dictionary


def file_writer(key, item):
    with open(file='sample.txt', mode='a') as file:
        file.write(f'{key}: {item}\n')


def dictionary_file_writer(item):
    with open(file='dictionary_writer.txt', mode='a') as file:
        for k, v in item.items():
            file.writelines(f'{k}: {v}\n')
