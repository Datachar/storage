from unittest.case import TestCase
from storage import Storage
import numpy as np
import pandas as pd
from pandas.util.testing import assert_frame_equal


class TestStorage(TestCase):
    def setUp(self):
        self.first = pd.Series([1, 3, 5, 'Nan', 6, 8])
        self.second = pd.DataFrame({'A': 1.,
                                    'B': pd.Timestamp('20130102'),
                                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                                    'D': np.array([3] * 4, dtype='int32'),
                                    'E': pd.Categorical(["test", "train", "test", "train"]),
                                    'F': 'foo'})
        self.third = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])

    def test_get(self):
        storage = Storage()
        storage.add('first', self.first)
        print(storage.get('first') == self.first)

    def test2_get(self):
        storage = Storage()
        storage.add('second', self.second)
        print(storage.get('second') == self.second)


names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names, births))
