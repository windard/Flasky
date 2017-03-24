# coding=utf-8

import unittest
from flask import current_app
from app import create_app, db
from tests import FlaskyTestCase


class BasicsTestCase(FlaskyTestCase):
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
