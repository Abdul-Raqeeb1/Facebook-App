from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FacebookPost,Comment_Box,Friend_List,Extra_User_Table
from django.core.mail import send_mail
from django.conf import settings
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import os


# Create your views here.

def send_simple_email_view(request):
    subject = "Welcome to My Awesome Site!"
    message = "Thanks for signing up. We're glad to have you!"
    from_email = settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'webmaster@example.com'
    recipient_list = ['expertinstitute85@gmail.com']

    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False, # Set to True to suppress exceptions
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {e}")

@login_required
def Facebook_App(request):
    friends = Friend_List.objects.filter(current_user=request.user.id).values_list("friend_user", flat=True)
    value_get = FacebookPost.objects.filter(user_id_post__in=friends).order_by('-post_data_at')
    comment_get = Comment_Box.objects.all()
    session_user = request.session.get('username')

    if request.method == 'POST':
        form_type = request.POST.get('form-type')

        # 🟢 Handle Post Creation (text and/or image)
        if form_type == 'post-form':
            text_value = request.POST.get('text-post')
            uploaded_file = request.FILES.get('myFiles')

            # Check if file exists (user uploaded something)
            if uploaded_file:
                # Get file extension (.jpg, .png, etc.)
                extension = os.path.splitext(uploaded_file.name)[1]

                # Generate unique filename → username_20251024_153045.jpg
                new_filename = f"{request.user.username}_{timezone.now().strftime('%Y%m%d_%H%M%S')}{extension}"

                # Save file with new name
                fs = FileSystemStorage()
                filename = fs.save(new_filename, uploaded_file)
                file_url = fs.url(filename)

                # Save post with text and/or image
                FacebookPost.objects.create(
                    user_id_post=request.user,
                    text_area=text_value if text_value else "",
                    image=filename
                )
            else:
                # Only text post
                if text_value:
                    FacebookPost.objects.create(
                        user_id_post=request.user,
                        text_area=text_value
                    )

            return redirect('FaceBook')

        # 🟢 Handle Comment Creation
        elif form_type == 'comment-form':
            comment_text = request.POST.get('comment-message')
            post_id = request.POST.get('post-id')

            if comment_text and post_id:
                related_post = get_object_or_404(FacebookPost, id=post_id)
                Comment_Box.objects.create(
                    Comment_Post_id=related_post,
                    Comment_User_id=request.user,
                    Comment_Text=comment_text
                )
            return redirect('FaceBook')

    return render(request, 'Facebook_Page.html', {
        'get_value': value_get,
        'context': comment_get,
        'users': session_user
    })

    # value_get = FacebookPost.objects.all()
    # session_user = request.session.get('username')

    # if request.method == 'POST':
    #      FacebookPost.objects.create(
    #         user_id_post=request.user,
    #         text_area=request.POST.get('text-post')
    #      )
    #      return redirect('FaceBook')
    #     #  return render(request,'FaceBook_Page.html',{'view_post':publish_post,'get_value':value_get})

    # else:
    #     return render(request,'Facebook_Page.html',{'get_value':value_get,'users':session_user})


# Login Function

def Login_Page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        print(username)
        print(password)

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            request.session["username"] = user.username
            messages.success(request,"Logged in successfully!")
            return redirect('FaceBook')
        else:
            messages.error(request,"Invalid credentials")
    return render(request,'Login_Page.html')


# Logout Function

def Logout_Page(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('Login')


# Registration Form
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created!")
            return redirect('Login')
        else:
            form = UserRegisterForm()
        return render(request,'Login_Page.html',{"form":form})


# Create Account 
def Create_Account(request):
        if request.method == 'POST':
            gender = request.POST.get('gender')
    
            user = User()

            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password'))

            user.save()

            Extra_User_Table.objects.create(id=user,gender=gender)


            return redirect('Login')
        
def Post_Like(request,id):
    post = FacebookPost.objects.get(id=id)

    post.n_like += 1


    post.save()
    return redirect('FaceBook')

# Comment Options
def Comments_Option(request):

    comment_get = Comment_Box.objects.all()

    if request.method == 'POST':
        context = Comment_Box.objects.create(
            Comment_Text = request.POST.get('comment-message')
        )
        return render(request,'Facebook_Page.html',{'context':comment_get})
    

# New Fucntion
# def Call(request):
#     return redirect('loginpage')

def Friend_Lists(request):

    user_id = request.user.id
    friend_list = Friend_List.objects.filter(friend_user=user_id)

    friends = []
    waiting = []

    # print(friend_list[0].status)
    for  friend in friend_list:
        if friend.status == "PN":
            waiting.append(friend)
        elif friend.status == "AP":
            friends.append(friend)

    useres = User.objects.all()
    return render(request,'friend_list.html',{'Accept':friends,'request':useres,'waiting':waiting})


# upload image

def upload_file_view(request):
    # This block handles the submission of the form
    fs = FileSystemStorage()
    My_File = request.FILES['myFiles']
    filename = fs.save(My_File.name, My_File)
    file_url = fs.url(filename)

    print(file_url)
    


def User_Friend(request):

    context_Facebook = list( User.objects.exclude(id=request.user.id) )

    marked_users = []

    for user in context_Facebook:
        us = dict(user.__dict__)

        fr = Friend_List.objects.filter(current_user=request.user.id, friend_user= us.get("id"))
        us['waiting']=0

        if(fr):
            us['waiting']=1
        
        marked_users.append(us)

    return render(request,"Search-User.html",{'context_Facebook':marked_users})

def send_request(req,id):

    current = User.objects.get(id=req.user.id)
    friend_user = User.objects.get(id=id)
    
    Friend_List.objects.create(current_user=current,friend_user=friend_user)

    # return render(req,"Search-User.html",{'context_Facebook':context_Facebook})
    return redirect('global_friends')

    


def accept_friend(request,id):
    
    friend_request = Friend_List.objects.get(id=id)

    friend_request.status = 'AP'
    friend_request.save()
    return_request = Friend_List.objects.create(current_user=friend_request.friend_user,friend_user=friend_request.current_user,status='AP')

    return redirect('friendlist')

def reject_friend(request,id):

    f1 = Friend_List.objects.get(id=id)

    f1.delete()

    return redirect("friendlist")

def katti_friend(request,id):
    
    friend_katti = Friend_List.objects.get(id=id)

    f1 = Friend_List.objects.filter(current_user=friend_katti.friend_user,friend_user=friend_katti.current_user)
    f2= Friend_List.objects.filter(current_user=friend_katti.current_user,friend_user=friend_katti.friend_user)

    f1.delete()
    f2.delete()

    return redirect('friendlist')

def cancel_request(request,id):
    
    request_cencel = Friend_List.objects.get(friend_user=id,current_user=request.user.id)

    request_cencel.delete()

    return redirect('global_friends')


def User_Profile(request):
    current_id = request.user.id
    extra_info = Extra_User_Table.objects.filter(id_id=current_id).get()
    return render(request,"User-Profile.html",{"extra":extra_info})

def update_profile(request,up_field_name):
    current_id =request.user.id

    cur_extra_user = Extra_User_Table.objects.filter(id_id=current_id)

    dct = {up_field_name: request.POST.get(up_field_name)}

    cur_extra_user.update(**dct)


    return redirect("user-profile")

def user_profile_pic(request):
    if request.method == 'POST':
        print("request")

        # 🟢 Handle Post Creation (text and/or image)
        if True:
            uploaded_file = request.FILES.get('myProfile')
            print("uploaded")

            # Check if file exists (user uploaded something)
            if uploaded_file:
                # Get file extension (.jpg, .png, etc.)
                extension = os.path.splitext(uploaded_file.name)[1]

                # Generate unique filename → username_20251024_153045.jpg
                new_filename = f"{request.user.username}_{timezone.now().strftime('%Y%m%d_%H%M%S')}{extension}"

                # Save file with new name
                fs = FileSystemStorage()
                filename = fs.save(new_filename, uploaded_file)
                file_url = fs.url(filename)
                print("pic save")

                # Save post with text and/or image
                profile, created = Extra_User_Table.objects.get_or_create(id_id=request.user)
                
                if profile.profile_pic:
                    old_pic_path = profile.profile_pic.path

                    if os.path.exists(old_pic_path):
                        os.remove(old_pic_path)

                profile.profile_pic = filename
                profile.save()
                
                print("end")
                return redirect("user-profile")

def delete_user(request):
    
    user_delete = User.objects.get(id=request.user.id)

    user_delete.delete()

    return redirect('Login')