from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from users.views import register_view, user_logout

admin.site.site_header  =  "JantaSeva"  
admin.site.site_title  =  "Admin"
admin.site.index_title  =  "JantaSeva"

urlpatterns = [
    path('jantaseva/admin/', admin.site.urls),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path("logout/", user_logout, name="logout"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path("register/", register_view, name="register"),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html', success_url='/dashboard'), name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password-reset/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password-reset/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
