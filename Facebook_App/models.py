from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class RegisterFrom(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )


class FacebookPost(models.Model):
    
    user_id_post = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text_area = models.CharField(max_length=9999)
    image = models.ImageField(upload_to='post_images/',null=True)
    n_like = models.DecimalField(max_digits=9999,max_length=9,decimal_places=0,default=0,null=True)
    post_data_at = models.DateTimeField(auto_created=True,auto_now_add=True)

# Post Like Option

class Post_Likes(models.Model):
    Post_id = models.ForeignKey(
        FacebookPost,
        on_delete=models.CASCADE
    )
    User_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    like_date = models.DateTimeField(auto_created=True,auto_now_add=True)

# Comment Option

class Comment_Box(models.Model):
    def __str__(self):
        return self.Comment_Text+ self.Comment_User_id.username + str(self.Comment_Post_id.text_area)
    
    Comment_Post_id = models.ForeignKey(
        FacebookPost,
        on_delete=models.CASCADE
    )

    Comment_User_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    Comment_Text = models.CharField(max_length=9999)

    Comment_Date = models.DateTimeField(auto_created=True,auto_now_add=True)

# Firend list
class Friend_List(models.Model):

    def __str__(self):
        return str(self.current_user,)+str(self.friend_user)

    current_user = models.ForeignKey(
        User,related_name="current_user",
        on_delete=models.CASCADE
    )

    friend_user = models.ForeignKey(
        User,related_name="friend_user",
        on_delete=models.CASCADE
    )

    status_choice = [
        ('PN' , "Pending"),
        ('AP' , "Accept"),
        ('RJ' , "Reject"),
    ]
    status = models.CharField(max_length=20, choices=status_choice, default='PN')

    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)


# Extra User Table
class Extra_User_Table(models.Model):

    def __str__(self):
        return self.id.username
    

    id = models.OneToOneField(
        primary_key=True,
        to= User,
        on_delete=models.CASCADE
    )

    locations = models.CharField(max_length=500,null=True)

    current_school = models.CharField(max_length=500,null=True)

    education = models.CharField(max_length=500,null=True)

    gender_options = [
        ("MA","Male"),
        ("FE","Female"),
    ]

    gender = models.CharField(max_length=2,choices=gender_options)

    phone_number = models.CharField(max_length=20, null=True)

    
    profile_pic = models.ImageField(upload_to='media/profile/',null=True)