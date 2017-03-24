# coding=utf-8

import pytest
from app import create_app, db
from app.models import User


@pytest.fixture
def app(request):
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()
    request.addfinalizer(lambda :ctx.pop())
    return app


@pytest.fixture
def client(app):
    db.create_all()
    with app.test_client() as client:
        yield client
    db.session.remove()
    db.drop_all()


@pytest.fixture
def user_generator():
    def create(**kwargs):
        u = User(
            email = 'john@example.com',
            password = 'cat',
            )
        for attr, value in kwargs.items():
            setattr(u, attr, value)
        db.session.add(u)
        db.session.commit()
        return u
    return create
