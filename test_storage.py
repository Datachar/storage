from unittest.case import TestCase
from storage import Storage
import numpy as np
import pandas as pd


class TestStorage(TestCase):
    def setUp(self):
        self.first = pd.Series([1, 3, 5, 'Nan', 6, 8])
        self.second = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
        self.third = pd.DataFrame(np.random.randn(6,1), index=pd.date_range('2013-08-01', periods=6, freq='B'), columns=list('A'))

    def test_get_first_when_none(self):
        s = Storage('test')
        print('After')
        with self.assertRaises(KeyError):
            s.get('test')

    def test_get_first(self):
        s = Storage('test2')
        s.add('first', self.first)
        self.assertTrue(s.get('first').equals(self.first))

    def test_get_two(self):
        s = Storage('test2')
        s.add('first', self.first)
        s.add('first', self.second)
        self.assertTrue(s.get('first').equals(self.second))

    def test_get_third(self):
        s = Storage('test3')
        s.add('third', self.third)
        s.add('third2', self.third)
        self.assertTrue(s.get('third').equals(s.get('third2')))