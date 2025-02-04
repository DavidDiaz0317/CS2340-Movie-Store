from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def admin_home(request):
    return render(request, 'adminPage/adminHome.html', {'users':  User.objects.all()})

def admin_users(request):
    user_type = request.GET.get('type', 'user')

    if user_type == 'admin':
        users = User.objects.filter(is_staff=True)
    else:
        users = User.objects.filter(is_staff=False)
    return render(request, 'adminPage/adminUser.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = CustomUserCreationForm()

    return render(request, 'adminPage/create_user.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_type = request.GET.get('type', 'user')

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("admin_users")}?type={user.user_type}')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'adminPage/edit_user.html', {'form': form, 'user': user,
                                                        'user_type': user_type})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('admin_users')

def admin_movies(request):
    user_type = request.GET.get('type', 'user')

    if user_type == 'admin':
        users = User.objects.filter(is_staff=True)
    else:
        users = User.objects.filter(is_staff=False)
    return redirect(reverse('admin:index'))

def admin_reviews(request):
    user_type = request.GET.get('type', 'user')

    if user_type == 'admin':
        users = User.objects.filter(is_staff=True)
    else:
        users = User.objects.filter(is_staff=False)
    return redirect(reverse('admin:index'))

def admin_orders(request):
    user_type = request.GET.get('type', 'user')

    if user_type == 'admin':
        users = User.objects.filter(is_staff=True)
    else:
        users = User.objects.filter(is_staff=False)
    return redirect(reverse('admin:index'))