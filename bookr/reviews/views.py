from django.shortcuts import render


def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})
