# Binary Beans

Binary Beans is a charming boutique café. This website is designed for those curious about the cafe experience and seeking more information.

Users of the website can leave reviews directly on our site, sharing their thoughts and experiences. Additionally, users have the option to book a private event tailored to their preferences, ensuring a personalized and memorable occasion.

[The live link for the website is here](https://binary-beans-23fbf9ec9fe1.herokuapp.com/)

![Responsive mockup](https://github.com/Willr-hawkins/binary-beans/assets/148203271/8cb9a0af-99c3-4b57-bf5a-afcfbc42329f)

## Technologies Used

- HTML
- CSS
- Boostrap Framework CSS
- Django Framework

## Tools used

- GitHub - App repository
- GitPod - Cloud-based development enviroment
- ElefantSQL - Postgres database

## User stories

- As a Site Admin I can create and edit the about content of the website so that the content is up to date for the site users.
- As a Site User I can click the review link so that I can read the reviews on the coffee shop.
- As a Site User I can leave a review of the shop so that I can give my opinion.
- As a Site User I can edit and delete reviews so that I can update my opinion of the shop.
- As a Site User I can send a request for a private event booking so that I can use the shops facilities.
- As a Site Admin I can store private event requests in the database so that I can review them.
- As a Site Admin I can approve users request for a private booking so that the user will be notified of a successful booking.
- As a Site Admin I can create and edit the menu content so that users can see up to date menu items.
- As a Site Admin I can create and update the event information so that I can keep site users up to date with up and coming events.
- As a Site user I can Sign up and login so that I can leave reviews on the store.
- As a site User I can edit and cancel my bookings so that I can update the cafe about my booking.
- As a site user I can thumbs up review so that I can show if i agree with the users opinion.

## Pages 

### Binary Beans/Home page

This is the website's homepage, featuring a brief section about Café Binary Beans, providing users with an overview of the café's essence and opening hours.

![Homepage](https://github.com/Willr-hawkins/binary-beans/assets/148203271/8c3c9638-5497-4737-b0d6-c8f85fdbaa91)

### Menu Page

The menu page contains information about the café's main menu as well as event menus, allowing site users to browse the café's offerings before visiting.

![Menu Page](https://github.com/Willr-hawkins/binary-beans/assets/148203271/b1c8b021-70dc-4292-a94f-29325e881a5f)

![Menu Page](https://github.com/Willr-hawkins/binary-beans/assets/148203271/4a1069de-867e-4231-9a86-b4508668df87)

### Events Page

On the events page, users will be able to find up and coming events that will be held at the cafe, alongside for logged in users there will be a form to allow the user to request a private event of their choice at the cafe.

If a user has made a booking request their event will appear on the events page with all its information.

![Events Page](https://github.com/Willr-hawkins/binary-beans/assets/148203271/028769ed-19e5-4024-a9c6-dca316c34f4b)

![Booking Form](https://github.com/Willr-hawkins/binary-beans/assets/148203271/0eefc90d-623a-496f-8a3d-6ef59757def7)

![User Events](https://github.com/Willr-hawkins/binary-beans/assets/148203271/f3c96b7f-908b-4e38-a90d-102a468966cf)

Once a booking request has been sbumitted the event will appear with a message saying 'Booking Unapproved'

![unapproved message](https://github.com/Willr-hawkins/binary-beans/assets/148203271/72a61216-f0f6-47f9-aa52-c81605e40e46)

It will remain unapproved unitill the site admin approves the booking from the admin panel, this ensures that users are up to date with the status of their booking.

![approved message](https://github.com/Willr-hawkins/binary-beans/assets/148203271/795ae485-d546-4af6-a814-2c750400c4ca)


### Reviews Page

The reviews page will hold all reviews that users have made with their opinion on the cafe, alongside this logged in users will have a form to leave there own review.

![Reviews Page](https://github.com/Willr-hawkins/binary-beans/assets/148203271/73d8e786-5ddc-41d8-85e6-e5bb5f5531b4)

### Sign Up and Log In page

When the users click on sign up or log in they will be taken to a page with a form for either logging in as an exsiting user or for creating an account.

![Sign up](https://github.com/Willr-hawkins/binary-beans/assets/148203271/bd4496bd-66a9-4e6d-8024-b61388257249)

![Log in](https://github.com/Willr-hawkins/binary-beans/assets/148203271/40e99416-fb7e-485c-9650-4d2e31c45e0f)

### Custom 404 and 500 pages 

The website has it's own unique 404 error and 500 error pages, making it easier for users to navigate back to the working webiste.

![404 page](https://github.com/Willr-hawkins/binary-beans/assets/148203271/7772dcf0-3a93-4c9e-a034-0d208ff9af3b)

![500 page](https://github.com/Willr-hawkins/binary-beans/assets/148203271/b5a6cc8c-db4c-473b-a6dc-8be58b464f70)

## Features & Functionalities

### Account Managment

Users can register for an account, log in and log out. Majority of the sites content is available to all users wether logged in or not, however forms and liking review functionlaity is only available to logged in users.

### Admin Managment

As a superuser you gain access to the admin panel allowing you to access the app from the backend. The superuser can do the following:

- Add and delete users, About content, Menus, Events, Private events, and Reviews.
- Approve Booking requests. 

### Naviagtion Bar 

From the naviagtion bar users can access the About/Home, Menus, Events, and Reviews pages. The navigation bar also hold links for users to Sign up, Log in, and Log out.

### Events 

Events is an app within the project. Logged in users can view up and coming events as well as request their own private event using the booking form, in this form the user can add a menu from the events menu section on the menu page to thier event. 

Once a user had request an event they can edit or delete their event using the buttons beneath each event they've made.

![Edit and delete](https://github.com/Willr-hawkins/binary-beans/assets/148203271/7b4e4b1d-0b0e-4258-a502-2ddbf040163b)

### Reviews

Reviews is an app within the project. Logged in users can view other users reviews, as well as leave their own review using the review form.

Users will also be able to edit and delete their own reviews.

### Likes

When a logged in user goes to the reviews page they will see a thumbs up icon on each review that is not their own. 

Users can click on this icon to leave a like on that particular review, they can then click it again to remove their like.

![Like section](https://github.com/Willr-hawkins/binary-beans/assets/148203271/4a8d8d87-c3ad-49b1-b0cf-1a7fc314323b)

## Deployment to Heroku

- Create a Heroku app.
- Set up of necessary configuration variables in settings for the application.
- In the deploy tab connect the app to the relevant GitHub repository.
- Then Ensure that the branch the app is begin deployed by is main and click deploy.
- Heroku will then build the application using the specified buildpack and dependencies.
- Once the build process is complete, the URL can be used to access the deployed application.

## Testing

### Manual Testing

#### Testing links:

- Binary Beans logo - Takes the user to the About/Home page.
- About - Takes the user to the About/Home page.
- Menu - Takes the user to the Menu page.
- Events - Takes the user to the Events page.
- Reviews - Takes the user to the reviews page.
- Sign Up - Takes the user to the registration page, and registering works.
- Log in - Takes the user to the log in page, and logging in works.
- Log out - Takes the user to the confirmation page for logging out, when approved the user is successfully logged out.

#### Functionality Testing:

- Adding a Private event - Ensure that when the form is valid and submitted that the users request is added to the list of there events on the events page.
- Edit or deleting event - Ensure that when a user edits or deletes an event either the correct changes are displayed or the event is removed from their events list.
- Adding a review -  Ensure that when the review form is valid and submitted that the users review is added to the list of reviews on the review page.
- Edit or deleting review -  Ensure that when a user edits or deletes a review either the correct change are displayed or the review is removed from the reviews list.
- Liking/Unliking review - Ensure that when a user likes a review the thumbs up icon change color and when the user unlikes a review the thumbs up icon change back to normal.

#### Responive Testing:

Multiple devices have been used to test how responsive the site is:

- PC: Mac Mini, M2 chip, Runnning Chrome, Safari or FireFox, 27" monitor (1920x1080).
- Tablet: Ipad Air, M1 chip, Running Safari, 10.9" display (2360x1640).
- Phone: Iphone 13 pro, Running Safari, 6.1" display (2532x1170).

### Automatic testing

Automatic testing has been carried out for testing each apps forms.

#### Events Form:

    from django.test import TestCase
    from .forms import BookingForm
    from menu.models import EventMenus

    class TestBookingForm(TestCase):

        def setUp(self):
            # Create an instance of EventMenus
            self.event_menu = EventMenus.objects.create(title='Test menu', content='This is a test menu')

        def test_form_is_valid(self):
            """
            Test the form is valid.
            """

            booking_form = BookingForm({
                'customer_email': 'test@gmail.com',
                'booking_date': '2024-06-08',
                'event_title': 'Test Event',
                'event_description': 'This is a test event',
                'menu': self.event_menu.id,
            })
            self.assertTrue(booking_form.is_valid(), msg='Form is not valid')

        def test_customer_email_is_required(self):
            """
            Test for the cutomer_email field.
            """
            booking_form = BookingForm({
                'customer_email': '',
                'booking_date': '2024-06-08',
                'event_title': 'Test Event',
                'event_description': 'This is a test event',
                'menu': self.event_menu.id,
            })
            self.assertFalse(booking_form.is_valid(), msg='No customer email was provided')

        def test_booking_date_is_required(self):
            """
            Test for the booking_date field.
            """
            booking_form = BookingForm({
                'customer_email': 'test@gmail.com',
                'booking_date': ' ',
                'event_title': 'Test Event',
                'event_description': 'This is a test event',
                'menu': self.event_menu.id,
            })
            self.assertFalse(booking_form.is_valid(), msg='No booking date was provided')

        def test_event_title_is_required(self):
            """
            Test for the event_title field.
            """
            booking_form = BookingForm({
                'customer_email': 'test@gmail.com',
                'booking_date': '2024-06-08',
                'event_title': ' ',
                'event_description': 'This is a test event',
                'menu': self.event_menu.id,
            })
            self.assertFalse(booking_form.is_valid(), msg='No event title was provided')

        def test_event_description_is_required(self):
            """
            Test for the event_description field.
            """
            booking_form = BookingForm({
                'customer_email': 'test@gmail.com',
                'booking_date': '2024-06-08',
                'event_title': 'Test Event',
                'event_description': '',
                'menu': self.event_menu.id,
            })
            self.assertFalse(booking_form.is_valid(), msg='No event description was provided')

        def test_menu_is_required(self):
            """
            Test for the menu field.
            """
            booking_form = BookingForm({
                'customer_email': 'test@gmail.com',
                'booking_date': '2024-06-08',
                'event_title': 'Test Event',
                'event_description': 'This is a test event',
                'menu': '',
            })
            self.assertFalse(booking_form.is_valid(), msg='No menu was provided')

#### Reviews Form: 

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
            self.assertFalse(form.is_valid(), msg='Star rating field is not valid, must be within the range 1 to 5')

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

All automatic tests passed.

![Tests](https://github.com/Willr-hawkins/binary-beans/assets/148203271/eb369dda-52ac-4675-bf7e-ae50397767b0)

## Validation

### The W3C Markup validation service
![W3C HTML validation](https://github.com/Willr-hawkins/binary-beans/assets/148203271/b2f334df-f55b-4210-854e-0ad454f40f71)

### The W3C CSS validation service
![W3C CSS validation](https://github.com/Willr-hawkins/binary-beans/assets/148203271/037433b6-c7fc-4a45-ae1f-c2ce7b5cb661)

### CI Python Linter
![CI python linter](https://github.com/Willr-hawkins/django-blog-project/assets/148203271/911e69df-f608-41c5-86bd-1306fd14c28d)

## Credits

I have used the knowledge I learnt from the I Think Before I Blog course content, and I have taken inspiration from the code written in the walktrough project.

For the liking functionality and unliking functionality I took inspiration from the following youtube videos:
- [Codemy.com Channel](https://www.youtube.com/@Codemycom)

- [Liking Functionality](https://www.youtube.com/watch?v=PXqRPqDjDgc)

- [Unliking Functionality](https://www.youtube.com/watch?v=dwgIi8dspa4)

## Acknowledgment

I would like to express my gratitude to Spencer Barriball for guiding me during this project and offering me support to overcome challenges I faced during completing this project.