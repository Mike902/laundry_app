from django.shortcuts import render


# Create your views here.
def contact_page(request):
  user = {
    "firstName": "Mike"
  }
  context = {
    "title": "Contact",
    "user": user
  }
  return render(request, "pages/contact.html", context)