from django.shortcuts import render


def posts_list(request):
    names = ['Igor Kolodiazhnyi', 'I', 'Me']
    return render(request, 'blog/index.html', context={'author': names})
