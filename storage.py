from tables import *
import pandas as pd

# h5file = open_file('data_base.h5', mode='w', title='test file')

index_name = None
index_data_frame = 0


class Storage:
    def __init__(self):
        self.storage_table = []

    def add(self, name, new_df):
        if len(self.storage_table) > 0:
            for i in self.storage_table:
                if name == i[index_name]:
                    input_elem = ('Element ' + name + 'already exists. Please input new name: ')
                    return self.add(index_name, new_df)
        new_elem = list([])
        new_elem.append(name)
        new_elem.append(dict(new_df))
        self.storage_table.append(new_elem)

    def get(self, name):
        for i in self.storage_table:
            if name == i[index_name]:
                return pd.DataFrame(i[index_name])
            else:
                return pd.Series(i[index_name])


if __name__ == '__main__':
    storage = Storage()
    storage.add('new_record', pd.Series([1, 2, 'f', 4, 5]))
    print(storage.get('new_record'))