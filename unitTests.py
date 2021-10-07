from quantcastFunctions import *
import unittest

class test_increment_count(unittest.TestCase):
    def test_increment_count_nonexistent(self):
        counts = {}
        increment_count(counts, "hello")
        self.assertEqual(counts["hello"], 1)
        
    def test_increment_count_existent(self):
        counts = {"hello" : 3}
        increment_count(counts, "hello")
        self.assertEqual(counts["hello"], 4)
        
class test_correct_date(unittest.TestCase):
    def test_correct_date_correct(self):
        same_start = correct_date("2018-12-09T14:19:00+00:00", "2018-12-09")
        self.assertEqual(same_start, True)
        
    def test_correct_date_incorrect(self):
        same_start = correct_date("2018-12-04T14:19:00+00:00", "2018-12-09")
        self.assertEqual(same_start, False)
        
class test_find_max_cookie(unittest.TestCase):
    def test_find_max_cookie(self):
        counts = {"cookie1" : 3, "cookie2": 5, "cookie3": 1, "cookie4" : 10}
        max_cookie = find_max_cookie(counts)
        self.assertEqual(max_cookie, ["cookie4"])
        
    def test_find_max_cookie_multiple(self):
        counts = {"cookie1" : 3, "cookie2": 10, "cookie3": 1, "cookie4" : 10}
        max_cookie = find_max_cookie(counts)
        self.assertEqual(max_cookie, ["cookie2", "cookie4"])