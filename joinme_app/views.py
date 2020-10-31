from django.shortcuts import render, redirect
from .models import Activity, User, Comment
from .forms import ActivityForm, NewUserForm, CommentForm, LoginForm
from django.contrib import messages
import collections
import os

# Create your views here.
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: views.py

# reading key file and getting the key
workpath = os.path.dirname(os.path.abspath(__file__))
api_file_path = os.path.join(workpath, 'api-key.txt')
api_file = open(api_file_path, "r")
api_key = api_file.read()
api_file.close()

# getting file path for the  picture:
commenter_pic = os.path.join(workpath, 'commenter.png')


def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        print("----> User Login Page <-----")
        return render(request, "joinme_app/login_form.html", {'form': form})
    else:
        found_user = False
        form = LoginForm(request.POST or None)
        if form.is_valid():
            log_email = form.cleaned_data.get('u_email', None)
            log_pswd = form.cleaned_data.get('pswd', None)

            print("---Email entered is: {}\n ---Password entered is: {}".format(log_email, log_pswd))

        list_users = User.objects.all()

        for u in list_users:
            if u.u_email == log_email and u.pswd == log_pswd:
                found_user = True
                return redirect('/joinme/activity_list')

        if found_user == False:
            form = LoginForm()
            message = 'Wrong email and password, please try again or create a new account...'
            return render(request, "joinme_app/login_form.html", {'form': form, 'message': message})

    return redirect('/joinme/activity_list')


def signup_form(request):
    """ signup_form for creating an user account
    Keyword arguments:
    request -- as required
    """
    # If this is a getting request then just render the form
    if request.method == "GET":
        form = NewUserForm()
        print("----> Creating a new SIGN UP Form <-----")
        return render(request, "joinme_app/sign_up.html", {'form': form})
    # otherwise post method when calling in the form
    else:
        form = NewUserForm(request.POST)
        print(form)
        print("Submit to create a new user in POST request")

    # Validating the form
    if form.is_valid():
        result = form.save()
        print("1 row has been affected at inserting")
    else:
        print("form input error, it is not valid, nothing has been added")

    return redirect('/joinme/activity_list')


def activity_list(request):
    """Loading a list of records at startup.

    Keyword arguments:
    request -- as default and required
    """
    activities = Activity.objects.all()
    context = {'activity_list': activities}
    return render(request, "joinme_app/activity_list.html", context)


def activity_form(request):
    """ joinme_form for creating a activity for adding into a list
    Keyword arguments:
    request -- as required
    """

    # if this is coming from a get method, then return a empty form
    if request.method == "GET":
        form = ActivityForm()
        print("----> Creating a new EMPTY Activity Form <-----")
        return render(request, "joinme_app/activity_create_form.html", {'form': form})
    else:
        form = ActivityForm(request.POST)
        print("Submiting a new form")

    if form.is_valid():
        result = form.save()
        print(form)
        print("1 row has been affected at inserting")
    else:
        print("form input error, it is not valid, nothing has been added")
    return redirect('/joinme/activity_list')


def activity_details(request, id=0):
    """ activity_details for user to clarify the details more
        user will be placing into a comments and reviews page singleton
        User will see organizer details and contact
        This is like a discussion forum
    Keyword arguments:
    request -- as required
    """
    # google map url API
    url = "https://www.google.com/maps/embed/v1/place?key=" + api_key + "&q="

    # initializing current User and Activity
    activity = Activity.objects.get(pk=id)
    #  currently default to a user, but looking at the template the commenter name is the organizer name
    #  for testing purpose AUDIT
    cmt_user = User.objects.get(pk=1)

    # Preparing for google API address
    address_plus = activity.address.replace(" ", "+")

    comments = activity.comments.filter(active=True)

    # generating a new comments list
    # for index, item in enumerate(comments):
    #     comments[index].body = item.body.replace("\r", "<br>")
    #     print(comments[index].body)

    new_comment = None
    # Comment posted
    if request.method == 'POST':
        print("in the post and creating a new comment")
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            print("Form is valid")
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = activity
            new_comment.cmt_user_name = cmt_user
            # new_comment.body = comment_form.cleaned_data['body'].replace("\r", "<br>")
            # Save the comment to the database
            new_comment.save()

            comment_form = CommentForm()
        else:
            print("Form is not valid")

    else:
        comment_form = CommentForm()
    context = {'activity': activity,
               'api_address': url+address_plus,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form,
               'commenter_pic': commenter_pic
               }
    return render(request, "joinme_app/activity_details.html", context)
