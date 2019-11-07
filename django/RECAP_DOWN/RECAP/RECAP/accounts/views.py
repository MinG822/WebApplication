from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
from IPython import embed
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


# Create your views here.
def signup(request):
    # embed()
    if request.method == 'POST':
        # 보내온 정보 저장
        # embed()

        """
        # 검증 먼저
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aritcles:index')
        """

        # 검증 먼저
        form = CustomUserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # embed()
        """logic 흐름
        username이 username인 것을 찾고
            if form.is_valid():
                username = request.POST.get('username')
                user = User.objects.get(username=username)
                if user:
                    if user.password == request.POST.get('password'):
                        # 로그인 시킨다: 세선 생성한다.
                else:
                    # 사용자가 없다.
        """
        
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

def logout(request):
    # 세선에서 유저 정보 지우기 / 세션 지우기
    auth_logout(request)

    return redirect('articles:index')

@require_POST
def delete(request):
    request.user.delete()
    return redirect('accounts:signup')
    # pass

@login_required
def update(request):
    if request.method == 'POST':
        # 변경사항 업데이트
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 폼 보여주기
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        # 비밀번호 변경
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # session auth hash를 변경
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # 폼 보여주기
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    context = {
        'person': person, 
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    user = request.user
    
    user.followers.add(person)


    return redirect('profile', username=person.username)