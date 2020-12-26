import unittest
from unittest.mock import Mock
from .add_multify import Method


# 注意：单元测试文件夹的名字不能含有汉字，否则每次就回弹出Edit Configration
class test_add_multify(unittest.TestCase):
    def test_add_and_multify(self):
        x,y=5,5
        method = Method()
        method.multify =Mock(return_value=25) # multify功能还未开发，我们给一个预定值
        add_result,multify_result = method.add_and_multify(5,5)
        self.assertEqual(add_result,10)  # 测试x+y的功能是否正确
        self.assertEqual(multify_result,25)  # 测试x*y是否正确，此时的multify函数已经被Mock掉，也就是说，multify_result并不是被测试函数返回的结果，而是我们mock给的结果

    # def test_multify(self):
    #     method = Method()
    #     result=method.multify(2,3)
    #     assert result==6
    #     # self.assertEqual(result,6)

if __name__ == '__main__':
    unittest.main()