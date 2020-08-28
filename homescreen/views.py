from django.shortcuts import render
from djangocustom_user import settings


# Create your views here.

def home_view(request):
    username = request.user.username
    display_name = request.user.display_name
    data = getattr(settings, 'AUTH_USER_MODEL', None)
    return render(request, 'index.html', {'username': username, 'display_name': display_name, 'data': data})
