from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def reverse(request):
    test_get_text = request.GET['message']
    i = test_get_text[::-1]
    return render(request, 'reverse.html', {'123': test_get_text, 'message': i})