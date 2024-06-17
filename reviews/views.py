from django.shortcuts import render
from django.views import generic
from .models import Review
from .forms import ReviewForm

# Create your views here.
def review_list(request):

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.review_name = request.user
            review.save()

    review_form = ReviewForm()
    reviews = Review.objects.all()
    review_count = reviews.count()

    return render(
        request,
        "reviews/reviews.html",
        {
            "review_form": review_form,
            "reviews": reviews,
            "review_count": review_count
        }
    )