from django.shortcuts import render
from .models import Article
from django.http import HttpResponseRedirect

# Create your views here. These are test views only for dev


def home(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # FIXME: loginAsAdmin is not working properly
        # loginAsAdmin = request.POST["login_as_admin"]

        # if loginAsAdmin == "on":
        #     loginAsAdmin = True
        # else:
        #     loginAsAdmin = False

        print(f"{email} {password} ")  # TODO: add loginAsAdmin, when it is implemented
        return HttpResponseRedirect("/MeinBereich/dashboard")
    else:
        pass
    # get all articles
    articles = Article.objects.all()
    return render(request, "content/home.html", {"articles": articles})
