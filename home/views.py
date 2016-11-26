from django.shortcuts import render

def home(request):
    string = '你好，我是张东昌啊'
    things = [x for x in range(1, 1000)]
    return render(request, 'my_home.html', {'string': string, 'things': things})
