from django.db import models

class Image(models.Model):
    title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="home_images")


class Title(models.Model):
    title = title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100)


class MenuItem(models.Model):
    title = title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=25)
    link = models.TextField(blank=True)

class Button(models.Model):
    title = title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=25)
    link = models.TextField(blank=True)

class ShowcaseText(models.Model):
    title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class SectionAText(models.Model):
    title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class SectionBText(models.Model):
    title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class SectionCCard(models.Model):
    title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    cardName = models.CharField(max_length=100)
    pricing = models.CharField(max_length=25)
    paymentPlan = models.CharField(max_length=50)
    details = models.TextField()

class SectionDText(models.Model):
    title = models.CharField(db_index=True, unique=True, max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

