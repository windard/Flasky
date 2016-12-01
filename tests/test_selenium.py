# coding=utf-8

import re
import unittest
import threading
from app import create_app, db
from selenium import webdriver
from app.models import Role, User, Post, Comment, Follow

class SeleniumTestCase(unittest.TestCase):
	"""docstring for SeleniumTestCase"""
	client = None

	@classmethod
	def setUpClass(cls):
		try:
			cls.client = webdriver.Chrome()
		except:
			pass

		if cls.client:
			cls.app = create_app('testing')
			cls.app_context = cls.app.app_context()
			cls.app_context.push()

			import logging

			logger = logging.getLogger('werkzeug')
			logger.setLevel('ERROR')

			db.create_all()
			Role.insert_roles()
			User.generate_fake(10)
			Post.generate_fake(10)

			admin_role = Role.query.filter_by(permission=0xff).first()
			admin = User(email='john@example.com', username=unicode('john'), password='cat', role=admin_role, confirmed=True)
			db.session.add(admin)
			db.session.commit()

			threading.Thread(target=cls.app.run).start()

	@classmethod
	def tearDownClass(cls):
		if cls.client:
			cls.client.get('http://localhost:5000/shutdown')
			cls.client.close()

			db.drop_all()
			db.session.remove()

			cls.app_context.pop()

	def setUp(self):
		if not self.client:
			self.skipTest('web browser not available')

	def tearDown(self):
		pass	

	def test_admin_home_page(self):
		self.client.get('http://localhost:5000/')
		self.assertTrue(re.search(u'hello,\s+Stranger!', self.client.page_source))

		self.client.find_element_by_link_text('Log In').click()
		self.assertTrue('<h1>Login</h1>' in self.client.page_source)

		self.client.find_element_by_name('email').send_keys('john@example.com')
		self.client.find_element_by_name('password').send_keys('cat')
		self.client.find_element_by_name('submit').click()
		self.assertTrue(re.search(u'hello,\s+john!', self.client.page_source))

		self.client.find_element_by_link_text('Profile').click()
		self.assertTrue('<h1>john</h1>' in self.client.page_source)