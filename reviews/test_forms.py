from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        """
        Test form is valid.
        """
        form = ReviewForm({
            'star_rating': 2,
            'review_body': 'Test review',
        })
        self.assertTrue(form.is_valid(), msg='Form is not valid')

    def test_star_rating_is_valid(self):
        """
        Test star_rating field is valid.
        """
        form = ReviewForm({
            'star_rating': 10,
            'review_body': 'Test review',
        })
        self.assertFalse(
                form.is_valid(),
                msg='Star rating field is not valid',
            )

    def test_star_rating_is_required(self):
        """
        Test for the star_rating field.
        """
        form = ReviewForm({
            'star_rating': '',
            'review_body': 'Test review',
        })
        self.assertFalse(form.is_valid(), msg='No star rating was provided')

    def test_review_body_is_required(self):
        """
        Test for the review_body field.
        """
        form = ReviewForm({
            'star_rating': 2,
            'review_body': '',
        })
        self.assertFalse(form.is_valid(), msg='No review body was provided')
