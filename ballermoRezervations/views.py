from django.shortcuts import redirect, render


def redirect_home(request):
    return redirect("/")


def handler500(request, *args, **argv):
    response = render(request, "errors/500.html")
    response.status_code = 500
    return response
