from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


from users.forms import UserLoginForm, UserRegisterForm
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

    # def form_valid(self, form):
    #     super().form_valid(form)
    #     user = form.save()
    #     if send_verify_email(user):
    #         print('Сообщение отправлено.')
    #         return HttpResponseRedirect(reverse('users:login'))
    #     else:
    #         print('Не удалось отправить сообщение.')
    #         return HttpResponseRedirect(reverse('users:login'))


# class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
#     model = User
#     template_name = 'users/profile.html'
#     form_class = UserProfileForm
#     success_message = 'Изменения сохранены!'
#
#     def get_success_url(self):
#         return reverse_lazy('users:profile', args =(self.object.id,))
#
#     def get_context_data(self, **kwargs):
#         context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
#         context['title'] = 'GeekShop - Профиль'
#         context['baskets'] = Basket.objects.filter(user=self.object)
#         return context
#
#
# class UserLogoutView(LogoutView):
#     template_name = 'users/login.html'