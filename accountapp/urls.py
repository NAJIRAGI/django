from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import helloworld, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = "accountapp"

urlpatterns = [
                    # FBV에선 함수 이름을 바로 사용해서 불러올 수 있다.
    path('helloworld/', helloworld, name='helloworld'),
                    # CBV에선 Class이름 뒤에 .as_view()를 붙인다.
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
          # 해당 유저 정보를 골라오기 위해 Primary Key를 인자값으로 가져온다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
]