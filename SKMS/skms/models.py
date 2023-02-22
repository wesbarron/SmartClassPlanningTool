from django.db import models

# Create your models here.

class UserAccount(models.Model):
    

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices= (('Active','Active'), ('Inactive','Inactive')), default='Active')
    type = models.CharField(max_length=255, choices= (('User','User'), ('Expert','Expert')), default='User')

    def __str__(self):
        return self.username

class Post(models.Model):
    #likes, comments, title, content, userUploaded, date, time, subject, subscriptions
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    subject = models.CharField(max_length=100)
    subscriptions = models.ManyToManyField('auth.User', related_name='subscribed_posts')
    comments = models.ManyToManyField('Comment', related_name='post_comments')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.content}'


class Assets(models.Model):
    assetid = models.AutoField(db_column='AssetID', primary_key=True)  # Field name made lowercase.
    assetname = models.TextField(db_column='AssetName', unique=True)  # Field name made lowercase.



class CountermeasureDescriptions(models.Model):
    countermeasureid = models.OneToOneField('Countermeasures', models.DO_NOTHING, db_column='CounterMeasureID', primary_key=True)  # Field name made lowercase.
    countermeasuredescription = models.TextField(db_column='CounterMeasureDescription')  # Field name made lowercase.




class Countermeasures(models.Model):
    countermeasureid = models.AutoField(db_column='CounterMeasureID', primary_key=True)  # Field name made lowercase.
    countermeasurename = models.TextField(db_column='CounterMeasureName', unique=True)  # Field name made lowercase.



class ThreatDescriptions(models.Model):
    threatid = models.OneToOneField('Threats', models.DO_NOTHING, db_column='ThreatID')  # Field name made lowercase.
    threatdescription = models.TextField(db_column='ThreatDescription')  # Field name made lowercase.



class Threats(models.Model):
    threatid = models.AutoField(db_column='ThreatID', primary_key=True)  # Field name made lowercase.
    threatname = models.TextField(db_column='ThreatName', unique=True)  # Field name made lowercase.
