import unittest
from unittest.mock import Mock
from .add_multify import Method


# 注意：单元测试文件夹的名字不能含有汉字，否则每次就回弹出Edit Configration
class test_add_multify(unittest.TestCase):
    def test_add_and_multify(self):
        x,y=5,5
        method = Method()
        method.multify =Mock(return_value=25) # method.multify被模拟返回值25
        add_result,multify_result = method.add_and_multify(5,5)  # multify_result将不会从真正的函数中计算值，也就是说屏蔽了method.multify方法，目的是只测试add_and_multify这个方法是否有错误
        self.assertEqual(add_result,10)
        self.assertEqual(multify_result,25)

    def test_multify(self):
        method = Method()
        result=method.multify(2,3)
        assert result==6
        # self.assertEqual(result,6)

if __name__ == '__main__':
    unittest.main()