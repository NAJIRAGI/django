from django.urls import path

from accountapp.views import helloworld, AccountCreateView

app_name = "accountapp"

urlpatterns = [
                    # FBV에선 함수 이름을 바로 사용해서 불러올 수 있다.
    path('helloworld/', helloworld, name='helloworld'),
                    # CBV에선 Class이름 뒤에 .as_view()를 붙인다.
    path('create/', AccountCreateView.as_view(), name='create'),
]