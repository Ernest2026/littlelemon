# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Create your views here.
@api_view()
def little(request):
    allBooks = Book.objects.all()
    bookSerializer = BookSerializer(allBooks, many=True)
    # return render(response, "index.html")
    # return HttpResponse("This is a little view")
    return Response({"name":bookSerializer.data})

@api_view()
def addBook(request):
    newBook = Book(title="The Great pig", author="F. Scott Fitzgerald", year=1925)
    newBook.save()
    return Response({"book": "Book added"})