from django.http import HttpResponse
from django.shortcuts import render


def helloworld(request):
    #요청이 POST 방식일 경우
    if request.method == "POST":
                                                              #추가적인 Data 꾸러미 안에 'text'라는 이름을 가진 'POST METHOD!!'라는 내용을 넣어서 저장
        return render(request, 'accountapp/hello_world.html', context={'text':'POST METHOD!!'})
    #요청이 GET 방식일 경우
    else:
                                                              #추가적인 Data 꾸러미 안에 'text'라는 이름을 가진 'GET METHOD!!'라는 내용을 넣어서 저장
        return render(request, 'accountapp/hello_world.html', context={'text':'GET METHOD!!'})