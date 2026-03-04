import unittest
from app import mutiply

class TestApp(unittest.Testcase):


  def test_mutiply(self):
          self.assertequal(mutiply(3,4),12)

if name = "main":
unittest.main()