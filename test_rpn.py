import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)

	def test_sub(self):
		result = rpn.calculate("1 2 -")
		self.assertEqual(-1, result)

	def test_mult(self):
		result = rpn.calculate("7 2 *")
		self.assertEqual(14, result)

	def test_div(self):
		result = rpn.calculate("7.0 2.0 /")
		self.assertEqual(3.5, result)
	
	def test_badstring(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +")
	def test_exponent(self):
		result = rpn.calculate("7 2 ^")
		self.assertEqual(49)
