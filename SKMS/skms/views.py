from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from .signUpForm import username_clean, email_clean
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        username = request.POST['user_name'].lower() 
        password = request.POST['password'] 
        #print(username, password)
        userNameCheck = UserAccount.objects.filter(username = username).exists()
        userPasswordCheck = UserAccount.objects.filter(password=password, username=username).exists()
        #print(userNameCheck, userPasswordCheck)
        #context = {"current_user":username}
        #current_user = request.user
        posts = Post.objects.all()
        context = {"current_user":username, "posts":posts}
        if userNameCheck == True and userPasswordCheck == True:
            return render(request, 'discussion-home.html', context=context)
        else:
            messages.error(request, 'The username or password combination is incorrect.')
            return render(request, 'index.html')

    return render(request, 'index.html')
    

def createAccount(request):
    if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        username = request.POST['user_name'] 
        password = request.POST['password'] 
        userNameCheck = User.objects.filter(username = username).exists()
        if userNameCheck == True:
            print(userNameCheck)
            messages.error(request, 'The username '+username+' already exists.')
            return render(request, 'sign-up.html')
        else:
            ins = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
            ins.save()
            ins2 = UserAccount(firstname = first_name, lastname = last_name, email = email, username=username, password=password, status='Active', type='User')
            ins2.save()
            messages.success(request, 'The account was successfully created.')
            return render(request, 'sign-up.html')
              
    return render(request, 'sign-up.html')

def userProfile(request):
    current_user = request.user
    account_user = UserAccount.objects.filter(username__exact=current_user).values()
    fs = FileSystemStorage()
    uploaded_file_url = fs.url(account_user[0]['userimage'])
    context = {"current_user":current_user, "current_user_id":current_user.id, "firstname":current_user.first_name, "lastname":current_user.last_name, "email":current_user.email, "type":account_user[0]['type'], "uploaded_file_url":uploaded_file_url}

    return render(request, 'user-profile.html', context=context)

def forum(request):
    current_user = request.user
    posts = Post.objects.all()
    context = {"current_user":current_user, "current_user_id":current_user.id, "posts":posts}

    return render(request, 'discussion-home.html', context=context)

def editProfile(request):
    current_user = request.user
    account_user = UserAccount.objects.filter(username__exact=current_user).values()
    context = {"current_user":current_user, "current_user_id":current_user.id, "firstname":account_user[0]["firstname"], "lastname":account_user[0]["lastname"], "email":account_user[0]["email"], "username":account_user[0]["username"], "type":account_user[0]["type"]}
    if request.method == 'POST': 
        first_name = request.POST['firstname']
        last_name = request.POST['lastname'] 
        email = request.POST['email'] 
        username = request.POST['username']
        type = request.POST['type']
        userimage = request.FILES['userimage']
        fs = FileSystemStorage()
        filename = fs.save(userimage.name, userimage)
        uploaded_file_url = fs.url(filename)
        context = {"uploaded_file_url":uploaded_file_url,"firstname":first_name, "lastname":last_name, "email":email, "current_user":username, "type":type}
        ins2 = UserAccount.objects.filter(username__exact=username).update(firstname=first_name, lastname=last_name, email=email, username=username, userimage=userimage)
        
        return render(request, 'user-profile.html', context=context)

    return render(request, 'edit-profile.html', context=context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post.html", {'post':post})

def renderCreatePost(request):
    return render(request,"create-post.html")

def createTestPost():
    author = User.objects.get(username='katieavt')
    post1 = Post(title='This is a test post',
        content='This is test content.',
        author=author,
        datetime = timezone.now(),
        subject="TestSubject"
    )
    post1.save()
    return post1

def renderCreatePost(request):
    return render(request,"create-post.html")

@login_required
def createPost(request):
    if request.method == 'POST': 
        title = request.POST['title']
        content = request.POST['description'] 
        author = request.user
        datetime = timezone.now()
        subject = "Null Subject"
        
        newPost = Post(title=title, content=content, author=author, datetime=datetime, subject=subject)
        newPost.save()
        return redirect('forum')

def createComment(request, post_id):
     if request.method == 'POST': 
        post = Post.objects.get(id=post_id)
        author = request.user
        content = request.POST['content']
        datetime = timezone.now()
        
        newComment = Comment(post=post, content=content, author=author, datetime=datetime)
        newComment.save()
        return redirect('post', post_id=post_id)

