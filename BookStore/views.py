from django.http import HttpResponse
from django.shortcuts import render, redirect

from BookStore.models import City, Author


# Create your views here.
def home(request):
    pass


def add_author(request):
    if request.method == 'GET':
        cities = City.objects.all()
        data = {'cities':cities}
        return render(request,"addauthor.html",data)
    else:
        a = Author()
        a.AuthorName = request.POST["tbaname"]
        a.AuthorDob = request.POST["tbadob"]
        a.AuthorGender = request.POST["ddlgender"]
        a.AuthorEmail = request.POST["tbemail"]
        a.AuthorPhone = request.POST["tbphone"]
        a.AuthorCity = City.objects.get(CityName=request.POST["ddlcity"])
        a.save()
        return  redirect("displayauthor")


def display_author(request):
    authors = Author.objects.all()
    data = {'authors' : authors}
    return render(request,"displayauthors.html",data)


def delete_author(request,id):
    a = Author.objects.get(id=id)
    a.delete()
    return redirect("displayauthor")


def edit_author(request,id):
    author = Author.objects.get(id=id)
    cities = City.objects.all()

    if request.method == "GET":
        data = {"author":author,'cities': cities}
        return  render(request,"editauthor.html",data)

    else:
        author.AuthorName = request.POST["tbaname"]
        author.AuthorDob = request.POST["tbadob"]
        author.AuthorGender = request.POST["ddlgender"]
        author.AuthorEmail = request.POST["tbemail"]
        author.AuthorPhone = request.POST["tbphone"]
        author.AuthorCity = City.objects.get(CityName=request.POST["ddlcity"])
        author.save()
        return redirect("displayauthor")
