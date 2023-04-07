from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ImageUploadForm
from .models import Image

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def profile_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
            form = ImageUploadForm()
            data = Image.objects.all()
            # print(data,"--------------------------")
    # return render(request, 'upload.html', {'form': form, 'data': data})
    return render(request, 'user/profile.html', {'form': form, 'data': data})


def update_image(request,id):
    if  request.method=="POST":
        image_name = request.POST['image_name']
        # print(image_name,"..............................")
        new_file = request.FILES.get('new_images')
        print(new_file,",,,,,,,,,,,,,,,,,,,,,,,,,,")
        # print("id=======================================",id)
        # retrieve the image record by ID
        image = Image.objects.get(id=id)

# def like_image(request, id):
#     print(".......................")
#     # image = Image.objects.all(Image, pk=id)
#     image = get_object_or_404(Image, pk=id)
#     print(image,"****************")
#     image.likes += 1
#     image.save()
#     return redirect('upload_image')

# def dislike_image(request, id):
#     if request.method == 'POST':
#     # image = Image.objects.all(Image, pk=id)
#         image = Image.objects.get(pk=id)
#         image.likes -= 1
#         image.dislikes += 1
#         image.save()
#         return redirect('upload_image')

