from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def helloworld(request):
    #요청이 POST 방식일 경우
    if request.method == "POST":
        # 변수 temp에 POST방식으로 받은 요청 중 'hello_world_input에 대한 정보를 저장
        temp = request.POST.get('hello_world_input')
        # 변수 new_hello_world에 accountapp.model에 있는 HelloWorld model을 저장 (DB 불러오기)
        new_hello_world = HelloWorld()
        # 변수 안에 들어있는 text에 변수 temp를 저장 (DB에 입력)
        new_hello_world.text = temp
        # 해당 정보를 저장 (DB에 저장)
        new_hello_world.save()

        # 작업이 완료 된 뒤에는 'account/helloworld/'으로 재접속. (새로고침 시 DB에 Data가 중복되어 쌓이는 것을 방지)
                                    # reverse 함수는 url을 즉시 생성하고, 반환한다. view를 실행할 때마다 호출.
        return HttpResponseRedirect(reverse('accountapp:helloworld'))

    #요청이 GET 방식일 경우
    else:
        # 변수 hello_world_list에 HelloWorld DB안에 있는 모든 객체를 저장
        hello_world_list = HelloWorld.objects.all()
                                                              # 추가적인 Data 꾸러미 안에 'text'라는 이름을 가진 'GET METHOD!!'라는 내용을 넣어서 저장
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})

# Django Generic에 있는 CreateView를 상속 받는 Class를 생성
class AccountCreateView(CreateView):
    # User는 Django에서 기본 제공 해주는 model 이다.
    model = User # 어느 Model을 사용할 것인가?
    form_class = UserCreationForm # 어는 Form을 사용할 것인가?
                  # revers_lazy 함수는 url이 필요한 시점에 url을 생성하고 반환한다. 현재 구문에서 success_url (성공 시) 이기 때문에 reverse_lazy를 사용.
    success_url = reverse_lazy('accountapp:helloworld') # 성공 시 어느 url로 전달할 것인가?
    template_name = 'accountapp/create.html' # 어떤 template를 보여줄 것인가?

