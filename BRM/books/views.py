from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NewBookForm
from . import models

def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'books/view_books.html',{'books':books})
    return res

def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/books/view/')

def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'books/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('http://localhost:8000/books/view/')
def searchBook(request):
    pass
def insertBook(request):
    form=NewBookForm()
    res=render(request,'books/insert_book.html',{'form':form})
    return res
def insert(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record Inserted Successfully <a href='http://localhost:8000/books/view'>View Books</a>"
    return HttpResponse(s)
