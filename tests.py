#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# unit testing
import unittest

from main import score_calculator,Love_score,Kid_score,Mood_score,length_and_complexity_score_calculator,unique_word_count

# class TestFunctions(unittest.TestCase):

def test_score_calculator(self):
    self.assertEqual(list(score_calculator([0,1,2,3,4,5,6,7,8,9])),[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])

def test_Love_score(self):
    self.assertEqual(Love_score('my sweet sweet darling, i love you so much'),4)
    self.assertEqual(Love_score('my sweet sweet darling, i do not hate you'),2)

def test_Kid_score(self):
    self.assertEqual(Kid_score('you are my angel, you are my star'),2)
    self.assertEqual(Kid_score('go to hell, jerk'),-2)

def test_Mood_score(self):
    self.assertEqual(Mood_score('i feel sad, i wanna cry, there is nothing cheerful in my life'),-1)
    self.assertEqual(Mood_score('i feel lucky and blessed everyday'),2)

def test_length_and_complexity_score_calculator(self):
    self.assertEqual(list(length_and_complexity_score_calculator([0,1,2])),[0.25, 0.75, 1.  ])

def test_unique_word_count(self):
    self.assertEqual(unique_word_count('baby baby baby oh yeah'),3)
    self.assertEqual(unique_word_count('you are my star, you are my sunshine'),5)


# # if __name__ == '__main__':
# #     unittest.main()

# suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestFunctions)
# unittest.TextTestRunner().run(suite)


# In[ ]:




