from django.shortcuts import render


# Create your views here.
def contact_page(request):
  context = None
  return render(request, "pages/contact.html", context)