from django.test import Client
from django.urls import reverse, resolve
import pytest
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Address, Letting


def test_letting_index_url():
    path = reverse('lettings_index', )
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_lettings_index_view():
    client = Client()
    response = client.get('/lettings/')
    content = response.content.decode()
    expected = "Lettings</h1>"

    assert response.status_code == 200
    assert expected in content
    assertTemplateUsed(response, "lettings/index.html")


def create_letting() -> Letting:
    address = Address.objects.create(number="7", street="rue de la vanille", city="Blablaland",
                                     state="Imaginaire", zip_code=12122, country_iso_code="BLA")
    return Letting.objects.create(title="Location test", address=address)


def init_letting() -> tuple:
    client = Client()
    letting = create_letting()
    path = reverse("letting", kwargs={"letting_id": letting.pk})

    return client, path, letting


@pytest.mark.django_db
def test_letting_url():
    client, path, letting = init_letting()
    assert path == f"/lettings/{letting.pk}/"
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_profile_view():
    client, path, letting = init_letting()
    response = client.get(path)
    content = response.content.decode()
    expected = f">{letting.title}</h1>"

    assert response.status_code == 200
    assert expected in content
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_profile_view():
    client = Client()
    unknown_pk = 2
    letting = Letting.objects.filter(pk=unknown_pk).first()

    assert letting is None

    path = reverse("letting", kwargs={"letting_id": unknown_pk})
    response = client.get(path)
    content = response.content.decode()
    expected = f"Aucune location ne correspond à votre recherche."

    assert response.status_code == 200
    assert expected in content
    assertTemplateUsed(response, "lettings/letting.html")
