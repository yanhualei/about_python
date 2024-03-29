import unittest
from unittest import mock
from .payment import PayApi
#  单元测试解决有依赖关系的模块
# 假设有这样一个场景：我们要测试一个支付接口但是这个支付接口又依赖一个第三方支付接口，
# 那么第三方支付接口我们暂时没有权限使用，那么我们该如何测试我们自己这个接口呢？
class TestPayApi(unittest.TestCase):

    def setUp(self):
        self.pay = PayApi()

    def test_1_success(self):
        self.pay.auth = mock.Mock(return_value={'status_code':'200'})  # 模拟第三方支付返回状态码：{'status_code':'200'}
        status = self.pay.pay('12345','1000','10000')
        self.assertEqual(status, '支付成功')  #将pay函数返回结果与模拟结果对比

    def test_2_fail(self):
        self.pay.auth = mock.Mock(return_value={'status_code':'500'})
        status = self.pay.pay('12345','1000','10000')
        self.assertEqual(status, '支付失败')

    def test_3_error(self):
        self.pay.auth = mock.Mock(return_value={'status_code':'300'})
        status = self.pay.pay('12345','1000','10000')
        self.assertEqual(status, '未知错误')

    def test_4_exception(self):
        self.pay.auth = mock.Mock(return_value='503')
        status = self.pay.pay('12345','1000','10000')
        self.assertEqual(status, 'Error, 服务器异常!')

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestPayApi('test_success'),TestPayApi('test_fail'),
            TestPayApi('test_error'),TestPayApi('test_exception')]
    # runner = unittest.TestRunner()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)