from django.urls import path, reverse_lazy
from users.apps import UsersConfig
from users.views import SignUp
from django.contrib.auth import views as auth_views

app_name = UsersConfig.name

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path('signup/', SignUp.as_view(success_url=reverse_lazy('users:login')), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('pass/change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('pass/reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('pass/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('pass/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('pass/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]
