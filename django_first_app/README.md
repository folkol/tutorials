# Writing your first Django app

Doing https://docs.djangoproject.com/en/2.0/intro/tutorial01/.

## Part 1

	$ django-admin startproject django_first_app .
	$ python manage.py runserver
	$ python manage.py startapp polls

Add index to polls/views.py
Add urlpatterns to polls/urls.py

## Part 2

Add models for Question and Choice
Add polls to installed apps

	$ python manage.py makemigrations
	$ python manage.py migrate

// Models are classes that inherit from django.dn.models.Model.
// Class variables represent columns in the database.

// Apps are decoupled from the site, they can be reused for other sites

	$ python manage.py shell
	>>> from polls.models import Question, Choice
	>>> Question.objects.all()
	<QuerySet []>
	>>> from django.utils import timezone
	>>> q = Question(question_text="What's new?", pub_date=timezone.now())
	>>> q.save()  # store in database
	>>> q.id
	1
	>>> q.question_text
	"What's new?"
	>>> q.pub_date
	datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)
	>>> q.question_text = "What's up?"
	>>> q.save()
	>>> Question.objects.all()
	<QuerySet [<Question: Question object (1)>]>

You might want to add __str__ to your models...

	$ python manage.py createsuperuser  # Might want to comment out AUTH_PASSWORD_VALIDATORS

Add models to polls/admin.py to be able to edit them in the admin GUI.

## Part 3

Load items from the database in the index view.
Create ./polls/templates/polls
// Populate the template index.html, and update the index view

## Part 4

...

## Part 5

...

## Part 6

Add static file, and refer to these in the templates.

## Part 7

...


## Switch to Postgresql

https://medium.com/agatha-codes/painless-postgresql-django-d4f03364989

	$ brew install postgresql
	$


## Deploy

https://medium.com/agatha-codes/9-straightforward-steps-for-deploying-your-django-app-with-heroku-82b952652fb4

	$ heroku login
