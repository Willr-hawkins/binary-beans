from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

    for review in reviews:
        review.total_likes = review.total_likes()

    review_count = reviews.count()

    return render(
        request,
        "reviews/reviews.html",
        {
            "review_form": review_form,
            "reviews": reviews,
            "review_count": review_count,
        }
    )

def likeView(request, pk):
    review = get_object_or_404(Review, id=request.POST.get('review_id'))
    review.likes.add(request.user)
    
    return redirect('reviews')

def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, review_name=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully!")
            return redirect('reviews')

    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, review_name=request.user)

    if request.method == "POST":
        review.delete()
        messages.success(request, "Booking request deleted successfully!")
        return redirect('reviews')

    return render(request, 'reviews/delete_review.html', {'review': review})