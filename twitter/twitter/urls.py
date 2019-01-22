"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tweet.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='tweet/login.html')),
    path("", LoginUserView.as_view(), name="login_user"),
    path("logout/", LogoutUserView.as_view(), name="logout_user"),
    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("add_message/", AddMessageView.as_view(), name="add_message"),
    path("mark/<int:id>/", MarkMessageView.as_view(), name="mark"),
    path("like/<int:msg_id>/", LikeMessageView.as_view(), name="like"),
    path("create/<int:message_id>/", AddCommentView.as_view(), name="add_comment"),
    path("user_info/<int:user_id>/", GetUserInfoView.as_view(), name="user_info"),
    path("user_profile/<int:user_id>", GetUserProfileView.as_view(), name="user_profile"),
    path("password/", ChangeUserPasswordView.as_view(), name="change_password"),
    path("edit_profile/<int:user_id>/", EditUserProfileView.as_view(), name="edit_profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
