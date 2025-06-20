from django.test import Client
from django.urls import reverse, resolve


def test_dummy():
    assert 1


def test_index_url():
    path = reverse('index', )
    assert path == "/"
    assert resolve(path).view_name == "index"


def test_index_view():
    client = Client()
    response = client.get('')
    content = response.content.decode()
    expected = "Welcome to Holiday Homes</h1>"

    assert response.status_code == 200
    assert expected in content
