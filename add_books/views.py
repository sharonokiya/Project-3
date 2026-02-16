from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def book_list(request):
    return render(request, 'book_list.html')
def book_details(request, pk):
    return render(request, 'book_details.html')
