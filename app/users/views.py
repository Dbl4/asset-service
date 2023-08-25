from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from assets.models import Asset
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_message = 'Изменения сохранены!'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        context['password_change_form'] = PasswordChangeForm(self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        password_change_form = PasswordChangeForm(self.request.user, request.POST)

        if form.is_valid() and password_change_form.is_valid():
            new_password = password_change_form.cleaned_data['new_password1']
            self.request.user.set_password(new_password)
            self.request.user.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserLogoutView(LogoutView):
    template_name = 'users/login.html'


class UserAssetsView(LoginRequiredMixin, TemplateView):
    template_name = 'users/assets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        assets = Asset.objects.filter(owner=user)
        context['assets'] = assets
        return context