from django.shortcuts import render
from ..utils.api_utils import get_random_joke, get_random_cat_fact


def jokes_and_facts_view(request):
    random_joke = get_random_joke()
    cat_fact = get_random_cat_fact()
    context = {"random_joke": random_joke, "cat_fact": cat_fact}
    return render(request, "jokes_and_facts.html", context)
