from django.urls import path
from labeler.views import HomeView, RegisterView, LoginView, UserView

app_name = "labeler"
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('login/', LoginView.as_view(), name="login-page"),
    path('user/<str:username>/', UserView.as_view(), name="user-page")
]