from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from ..models import (
    Article,
    CompanyInfo,
    Term,
    Contact,
    Vacancy,
    Review,
    PromoCode,
    Favor,
)
import logging
from ..decorator import role_required

logger = logging.getLogger(__name__)

def home_page_view(request):
    """
    View function for the home page.

    Retrieves the latest published article and passes it to the template.
    Logs an informational message about this view being accessed.
    """
    try:
        latest_article = Article.objects.latest("published_date")
    except Article.DoesNotExist:
        latest_article = None
    context = {"latest_article": latest_article}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: home_page_view")
    return render(request, "pages/home_page.html", context)


def about_page_view(request):
    """
    View function for the about page.

    Retrieves the first company information object and passes it to the template.
    Logs an informational message about this view being accessed.
    """
    company_info = CompanyInfo.objects.first()
    context = {"company_info": company_info}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: about_page_view")
    return render(request, "pages/about_page.html", context)


def news_page_view(request):
    """
    View function for the news page.

    Retrieves all published articles and passes them to the template.
    Logs an informational message about this view being accessed.
    """
    news = Article.objects.all()
    context = {"news": news}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: news_page_view")
    return render(request, "pages/news_page.html", context)


def terms_page_view(request):
    """
    View function for the terms page.

    Retrieves all terms and passes them to the template.
    Logs an informational message about this view being accessed.
    """
    terms = Term.objects.all()
    context = {"terms": terms}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: terms_page_view")
    return render(request, "pages/terms_page.html", context)


def contacts_page_view(request):
    """
    View function for the contacts page.

    Retrieves all contacts and passes them to the template.
    Logs an informational message about this view being accessed.
    """
    contacts = Contact.objects.all()
    context = {"contacts": contacts}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: contacts_page_view")
    return render(request, "pages/contacts_page.html", context)


def privacy_policy_page_view(request):
    """
    View function for the privacy policy page.

    Logs an informational message about this view being accessed.
    Renders the privacy policy page template.
    """
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: privacy_policy_page_view")
    return render(request, "pages/privacy_policy_page.html")


def vacancies_page_view(request):
    """
    View function for the vacancies page.

    Retrieves all vacancies and passes them to the template.
    Logs an informational message about this view being accessed.
    """
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: vacancies_page_view")
    return render(request, "pages/vacancies_page.html", context)


def reviews_page_view(request):
    """
    View function for the reviews page.

    Retrieves all reviews ordered by the date added and passes them to the template.
    Logs an informational message about this view being accessed.
    """
    reviews = Review.objects.all().order_by("-date_added")
    context = {"reviews": reviews}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: reviews_page_view")
    return render(request, "pages/reviews_page.html", context)


@login_required
def add_review_page_view(request, pk):
    """
    View function for the add review page.

    Retrieves the favor object with the given pk and passes it to the template.
    Logs a warning message about this view being accessed.

    If the request method is POST, creates a new review object with the user, favor, rating, and text, and saves it.
    Then redirects to the favor detail page.

    Renders the add review page template.
    """
    favor = get_object_or_404(Favor, pk=pk)
    context = {"favor": favor}
    logger.log(settings.LOGGING_LEVELS["warning"], "VIEW: add_review_page_view")

    if request.method == "POST":
        rating = request.POST.get("rating")
        text = request.POST.get("text")

        review = Review.objects.create(
            user=request.user, favor=favor, rating=rating, text=text
        )
        review.save()
        return redirect("favor_detail", pk=favor.id)

    return render(request, "pages/add_review_page.html", context)


@role_required("client")
def promocodes_page_view(request):
    """
    View function for the promocodes page.

    Retrieves all promocodes and passes them to the template.
    Logs an informational message about this view being accessed.

    This view is only accessible to users with the "client" role.
    """
    promocodes = PromoCode.objects.all()
    context = {"promocodes": promocodes}
    logger.log(settings.LOGGING_LEVELS["info"], "VIEW: promocodes_page_view")
    return render(request, "pages/promocodes_page.html", context)