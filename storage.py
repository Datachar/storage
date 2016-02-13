import pandas as pd

index_name = 0
index_size = 1
index_df = 2


class Storage:
    def __init__(self):
        self.storage = []

    def add(self, name, new_df):
        if len(self.storage) != 0:
            for i in self.storage:
                if i[index_name] == name:
                    new_input = input("\n DataFrame '" + name + "' is found. Enter new name - ")
                    return self.add(new_input, new_df)
        new_obj = list([])
        new_obj.append(name)
        new_obj.append(new_df.size)
        new_obj.append(dict(new_df))
        self.storage.append(new_obj)

    def get(self, name):
        for i in self.storage:
            if i[index_name] == name:
                if i[index_size] > len(i[index_df]):
                    return pd.DataFrame(i[index_df])
                else:
                    return pd.Series(i[index_df])
        new_input = input("\n DataFrame '" + name + "' not found. Enter new name - ")
        return self.get(new_input)