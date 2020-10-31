from django.db import models

# Create your models here.


class Activity(models.Model):
    # creating class model for Activity entity
    activity_name = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    zip = models.CharField(max_length=20, null=True)
    province = models.CharField(max_length=20, null=True)
    fees = models.CharField(max_length=20)
    organizer = models.CharField(max_length=20)
    email = models.CharField(max_length=30, null=True)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    num_people = models.IntegerField(default=0, blank=False, null=False)
    # description = models.TextField()


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    u_email = models.CharField(max_length=30)
    pswd = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)


class Comment(models.Model):
    post = models.ForeignKey(Activity, related_name='comments', on_delete=models.CASCADE)
    cmt_user_name = models.ForeignKey(User, related_name='cmt_users', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
