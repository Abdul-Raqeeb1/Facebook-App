from django.urls import path
# from django.shortcuts import redirect
from .views import Facebook_App,Login_Page,upload_file_view,Create_Account,User_Friend,Logout_Page,register,Post_Like,Friend_Lists,send_request,accept_friend,reject_friend,katti_friend,cancel_request,User_Profile,update_profile,user_profile_pic,delete_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    # path('', lambda request: redirect('/loginpage')),
    path('loginpage',Login_Page,name='Login'),
    path('logoutpage',Logout_Page,name='Logout'),
    path('Log-register',register,name='register'),
    path('facebookpage',Facebook_App,name='FaceBook'),
    path('Create_Account',Create_Account),
    path('likePost/<int:id>',Post_Like),
    path('friendlist',Friend_Lists,name='friendlist'),
    path('search-friend',User_Friend,name='global_friends'),
    path('send-request/<int:id>',send_request),
    path('loadfile',upload_file_view),
    path('accept-friend/<int:id>',accept_friend),
    path('reject-friend/<int:id>',reject_friend),
    path('katti-friend/<int:id>',katti_friend),
    path('cancel-request/<int:id>',cancel_request),
    path('user-profile',User_Profile,name="user-profile"),
    path('update-profile/<str:up_field_name>',update_profile,name='update-profile'),
    path('user-profile-pic',user_profile_pic,name='user-profile-pic'),
    path('delete-user',delete_user),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
