import pytest
from app.routes import app


@pytest.fixture
def client():
    return app.test_client()
