from django.shortcuts import render

# Create your views here.
def page(request):
  context = None
  return render(request, "page/contact.html", context)