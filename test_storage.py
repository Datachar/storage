from unittest.case import TestCase
from storage import Storage
import numpy as np
import pandas as pd


class TestStorage(TestCase):
    def setUp(self):
        self.first = pd.Series([1, 3, 5, 'Nan', 6, 8])
        self.second = pd.DataFrame({'A': 1.,
                                    'B': pd.Timestamp('20130102'),
                                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                                    'D': np.array([3] * 4, dtype='int32'),
                                    'E': pd.Categorical(["test", "train", "test", "train"]),
                                    'F': 'foo'})

    def test_1(self):
        test_storage = Storage()
        test_storage.add('first record', self.first)