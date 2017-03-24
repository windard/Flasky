# coding=utf-8

import unittest
from app import create_app, db
from app.models import Role


class FlaskyTestCase(unittest.TestCase):

    # 在每一条测试用例前执行
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    # 在每一条测试用例后执行
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    # def Testfunc(self):
    #     a = 1
    #     b = 1
    #     assert a == b

    # 在整个类的测试用例前执行
    # @classmethod
    # def setUpClass(cls):
    #     cls.app = create_app('testing')
    #     cls.app_context = cls.app.app_context()
    #     cls.app_context.push()
    #     db.create_all()
    #     Role.insert_roles()
    #     cls.client = cls.app.test_client(use_cookies=True)

    # 在整个类的测试用例之后执行 
    # @classmethod
    # def tearDownClass(cls):
    #     db.session.remove()
    #     db.drop_all()
    #     cls.app_context.pop()
