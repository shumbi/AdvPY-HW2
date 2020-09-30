from iterator import RESULT_FILE
import hashlib

file = input('Пожалуйста, введите путь и имя файла для генерации md5 hash (при пустом вводе будет использованы значения по умолчанию - country_url.json): ')
file = file or RESULT_FILE




class MD5Generator:
    """
    MD5Generator is a class that gets the file and generates md5 hash line by line
    """

    def __init__(self, file):
        self.file = file

    def __iter__(self):
        pass
        return self

    def md5_gen(self):
        with open(self.file) as f:
            for line in f:
                yield print('Хэшируемая строка:', line, 'md5 хэш: ', hashlib.md5(line.encode()).hexdigest())
                print()



