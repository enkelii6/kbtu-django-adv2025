from django.contrib.auth import logout
from django.shortcuts import redirect, render


def chat_page(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context = {}
    return render(request, 'chat/chatPage.html', context)


def custom_logout(request):
    logout(request)
    return redirect('login-user')
