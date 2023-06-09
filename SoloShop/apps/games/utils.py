from django.core.paginator import Paginator


def pages(request, objects, OBJECTS_LIMIT):
    paginator = Paginator(objects, OBJECTS_LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
