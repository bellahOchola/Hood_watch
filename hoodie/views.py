from django.shortcuts import render
from .forms import RegistrationForm,UploadProfile,CreatePost, BusinessForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Hood, Post, Profile, Business
from django.contrib.auth.decorators import login_required


# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form':form})


@login_required(login_url='login')
def profile(request, username):
    users = get_object_or_404(User, username=username)
    form = UploadProfile(request.POST,request.FILES, instance=request.user.profile)
    
    if form.is_valid():
        form.save()
        messages.success(request, f'You have successfully updated your profile')
        return redirect('profile')
    else:
        form = UploadProfile(instance=request.user.profile)
   

    return render(request, 'profile.html', {'form': form}, {'users':users})


def index(request):
    return render(request, 'index.html')
    


@login_required(login_url='login')
def hood(request):
    hoods = Hood.objects.all()
    # hood = Hood.objects.get()
    # import pdb; pdb.set_trace()

    return render(request, 'hood.html', {'hoods':hoods})


@login_required(login_url='login')
def single_hood(request,id):
    hood = Hood.objects.get(id=id)
    posts = Post.objects.filter(hood=hood)
    business = Business.objects.filter(hoodie=hood)
    posts = posts[::-1]
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood=hood
            post.user = request.user.profile
            post.save()
            return redirect('single_hood', hood.id)
    else:
        form = CreatePost()

    return render(request, 'single_hood.html', {'form':form,'hood':hood, 'posts':posts, 'business':business})


@login_required(login_url='login')
def create_business(request, id):
    hood = Hood.objects.get(id=id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hoodie=hood
            post.user = request.user.profile
            post.save()
            return redirect('single_hood', hood.id)
    else:
        form = BusinessForm()

    return render(request, 'business.html', {'form':form})


@login_required(login_url='login')
def search_business(request):
    if request.method == 'GET':
        name = request.GET.get('title')
        results = Business.objects.filter(name__icontains=name).all()
        message = f'name'

        return render(request, 'search.html', {'results':results, 'message':message} )
    else:
        message = "You haven't searched for any Business"

    return render(request, 'search.html', {'results':results, 'message':message} )

    

