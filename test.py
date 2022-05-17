import unittest
from SSN import SSN

class TestSSN(unittest.TestCase):
  def test_TC0(self):
    self.assertEqual('Invalid length input', SSN.ssnValidator(''))
  def test_TC1(self):
    self.assertEqual('valid SSN code', SSN.ssnValidator('856-45-6789'))
  def test_TC2(self):
    self.assertEqual('Invalid code. The third part should be from 0001 to 9999', SSN.ssnValidator('856-45-0000'))
  def test_TC3(self):
    self.assertEqual('Invalid code. The first part should not be 000, 666, or between 900 and 999', SSN.ssnValidator('000-45-6789'))
  
  



if __name__ == '__main__':
  unittest.main()
    