from tables import *

import pandas as pd

# h5file = open_file('data_base.h5', mode='w', title='test file')

index_name = 0
index_data_frame = 1


class Storage:
    def __init__(self):
        self.storage_table = []

    def add(self, new_name, new_df):
        if len(self.storage_table) > 0:
            for i in self.storage_table:
                if new_name == i[0].names:
                    new_input_name = ('Element with name ' + new_name + 'already exists. Please input new name: ')
                    return self.add(new_input_name, new_df)

        new_elem = list([])
        name = pd.DatetimeIndex(data=new_df, name=new_name)
        self.storage_table.append(name)


        '''
        new_elem.append(name)
        new_elem.append(new_df)
        '''
        self.storage_table.append(name)

    def get(self, name):
        for i in self.storage_table:
            if name == i[0]:
                return pd.DatetimeIndex.get_value(name)
            else:
                new_name = input('Name ' + name + ' not found. Please input other name: ')
                return self.get(new_name)


if __name__ == '__main__':
    storage = Storage()
    storage.add('new_record', [1, 2, 3, 4])

    print(storage.get('new_record'))
