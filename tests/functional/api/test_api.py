# coding=utf-8

import base64
import pytest
from flask import url_for
from mock import patch, Mock
import unittest


class BasicPyTestCase(object):
    """docstring for BasicPyTestCase"""

    @property
    def headers(self):
        value = 'Basic ' + base64.b64encode('%s:%s'%(self.email, self.password))
        return {'Authorization': value,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        }
    
    def assert_status_code(self, response, status_code):
        assert response.status_code == status_code

    def assert_status_type(self, response, content_type):
        assert response.headers['Content-Type'] == content_type

    def assert_ok(self, response):
        self.assert_status_code(response, 200)

    def assert_no_found(self, response):
        self.assert_status_code(response, 404)

    def assert_json(self, response):
        self.assert_status_type(response, 'application/json')

    def assert_html(self, response):
        self.assert_status_type(response, 'text/html; charset=utf-8')


class TestAPI(BasicPyTestCase):
    """docstring for TestAPI"""
    
    def test_get(self, client):
        response = client.get(url_for('api.get_posts'))
        self.assert_ok(response)
        self.assert_json(response)

    def test_no_authericated(self, client):
        response = client.post(url_for('api.new_post'))
        self.assert_status_code(response, 403)

    def test_no_found(self, client):
        response = client.get('http://127.0.0.1:5000/wrong/path')
        self.assert_no_found(response)
        self.assert_html(response)

    # def test_token(self, client, user_generator):
    #     user = user_generator()
    #     self.email = user.email
    #     self.password = user.password
    #     response = client.get(url_for('api.get_token'), headers=self.headers)
    #     self.assert_ok(response)

    #     self.assert_json(response)