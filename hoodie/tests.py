from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='bellah', password='bee@1972')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class HoodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='bellah')
        self.hood = Hood.objects.create(id=1, name='matata', hood_pic='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e',
         description='desc',user=self.user, police_line='+254 accra street',hospital_info='mama-ngina hospital accra road' )

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Hood))

    def test_save_hood(self):
        self.hood.save_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_hood(self):
        self.hood.delete_hood()
        hood = Hood.search_project('test')
        self.assertTrue(len(hood) < 1)

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='bellah')
        self.post = Post.objects.create(id=1, title='poster', content='life sucks',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)


    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)

class BusinessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='bellah')
        self.business = Business.objects.create(id=1, name='marina techs', description='life sucks',user=self.user, email='bellahkenya@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)


    def test_delete_business(self):
        self.business.delete_business()
        business = Business.search_project('test')
        self.assertTrue(len(business) < 1)
