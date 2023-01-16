from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from gallery.models import Photography


def index(request):
    photographs = Photography.objects.order_by(
        "-photo_date").filter(published=True)
    return render(request, 'gallery/index.html', {"cards": photographs})


def image(request, photography_id):
    photography = get_object_or_404(Photography, pk=photography_id)
    return render(request, 'gallery/imagem.html', {"photography": photography})


def search(request):
    photographs = Photography.objects.filter(published=True)
    name_to_search = request.GET['search']

    search = Q(
        Q(name__icontains=name_to_search) |
        Q(caption__icontains=name_to_search)
    )

    photographs = photographs.filter(search)
    return render(request, 'gallery/buscar.html', {"cards": photographs})


def search_by_tag(request):
    photographs = Photography.objects.filter(published=True)
    return render(request, 'gallery/buscar.html', {"cards": photographs})
