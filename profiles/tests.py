from django.test import Client
from django.urls import reverse, resolve
import pytest
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User
from profiles.models import Profile


def test_profile_index_url():
    path = reverse('profiles_index', )
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    response = client.get('/profiles/')
    content = response.content.decode()
    expected = "Profiles</h1>"

    assert response.status_code == 200
    assert expected in content
    assertTemplateUsed(response, "profiles/index.html")


def create_profile() -> Profile:
    user = User.objects.create(username="Username", first_name="Prénom",
                               last_name="Nom de Famille", email="test@mail.test")
    return Profile.objects.create(user=user, favorite_city="TestCity")


def init_profile() -> tuple:
    client = Client()
    profile = create_profile()
    path = reverse("profile", kwargs={"username": profile.user.username})

    return client, path, profile


@pytest.mark.django_db
def test_profile_url():
    client, path, profile = init_profile()
    assert path == f"/profiles/{profile.user.username}/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_profile_view():
    client, path, profile = init_profile()
    response = client.get(path)
    content = response.content.decode()
    expected = f"<p><strong>First name :</strong> {profile.user.first_name}</p>"

    assert response.status_code == 200
    assert expected in content
    assertTemplateUsed(response, "profiles/profile.html")
