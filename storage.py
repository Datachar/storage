import pandas as pd


class Storage:
    def __init__(self,name_file):
        self.storage = pd.HDFStore(name_file + '.h5')

    def add(self, name, new_df):
        self.storage[name] = new_df

    def get(self, name):
        return self.storage[name]