from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from user.models import User
from user.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()

        #     记录登录状态
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            request.session['avatar'] = user.icon.url
            return redirect('/user/info/')
        else:
            return render(request, 'register.html', {'error': form.errors})
    else:
        return render(request, 'register.html', )


def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'login.html', )


def logout(request):
    return render(request, 'logout.html', {})


def user_info(request):
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    return render(request, 'user_info.html', {'user': user})
