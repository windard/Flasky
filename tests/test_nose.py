# coding=utf-8

import re
import json
import unittest
from flask import url_for
from app import create_app, db
from app.models import User, Role, Post, Comment
from base64 import b64encode
from tests import FlaskyTestCase


class NoseTestCase(unittest.TestCase):
    app_context = None

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def setUp(self):
        # self._ctx = self.app.test_request_context()
        # self._ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.response = None


class TictalkTestCase(unittest.TestCase):
    app_context = None

    client_header = ''
    token = ''
    response = None

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        # cache.clear()
        self.clean_token()
        self.response = None

    def clean_token(self):
        self.token = ''
        

class NoseExampleTestCase(FlaskyTestCase):
    """docstring for APITestCase"""

    def test_nose(self):
        assert type(1) == int

    def test_url_for(self):
        print url_for('main.index')
        assert url_for('main.index') == '/'

    def test_client(self):
        # response = self.client.get('/')
        response = self.client.get(url_for('auth.index'))
        # print response.status_code
        self.assertEquals(response.status_code, 302)
        # assert response.status_code == 200

    def test_api(self):
        response = self.client.get(url_for('main.index'))
        assert response.status_code == 200
