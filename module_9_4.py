first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first,second)))

def get_advanced_writer(file_name):
    

    def writer_everything(*data_set):
        with