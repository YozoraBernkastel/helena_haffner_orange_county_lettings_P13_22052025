from django.shortcuts import render
from profiles.models import Profile


# Create your views here.
# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat
# libero pulvinar eget. Fusc# faucibus, urna quis auctor pharetra, massa dolor cursus
# neque, quis dictum lacus d
def profiles_index(request):
    """
    Display the home of the profile application with a list of all the profiles in an HTML page.
    :param request: The user's request
    :return: The render of the profiles/index.html with all the Profile's objects
    from the database.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,# it.
# Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Display an HTML page with the detail of the requested profile.
    :param request: The user's request.
    :param username: username of the selected profile.
    :return: The render of the detailed profile of the requested profile.
    """
    profile = Profile.objects.filter(user__username=username).first()

    context = {'profile': profile} if profile is not None else \
        {"unknown": f"Aucun profil ne correspond à votre recherche \"{username}\"."}
    return render(request, 'profiles/profile.html', context)
