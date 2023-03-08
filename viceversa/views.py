from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def reverse(request):
    test_get_text = request.GET['message']
    i = test_get_text[::-1]
    print(i)
    return render(request, 'reverse.html', {'message': i})