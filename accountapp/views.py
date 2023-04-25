from django.http import HttpResponse
from django.shortcuts import render

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

                                                              #추가적인 Data 꾸러미 안에 'hello_world_output'이라는 이름을 가진 객체 'new_hello_world'를 넣어서 저장
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output':new_hello_world})
    #요청이 GET 방식일 경우
    else:
                                                              #추가적인 Data 꾸러미 안에 'text'라는 이름을 가진 'GET METHOD!!'라는 내용을 넣어서 저장
        return render(request, 'accountapp/hello_world.html', context={'text':'GET METHOD!!'})