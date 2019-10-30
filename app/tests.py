from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


# Create your tests here.

class LocationTestClass(TestCase):
    
    def setUp(self):
        self.location = Location(id=1, name='Test')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
        
        
class ProfileTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='Test', password='12345')
        self.location = Location(id=1, name='Test')
        self.neighbourhood = Neighbourhood(id=1,name='Test',location=self.location,occupants=100)
        self.profile = Profile(id=1, name=self.user.username, neighbourhood = self.neighbourhood, bio = 'Testing', email = 'testing@gmail.com',user = self.user)

   
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))



class PostTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='Test', password='12345')
        self.location = Location(id=1, name='Test')
        self.neighbourhood = Neighbourhood(id=1,name='Test',location=self.location,occupants=100)
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user, neighbourhood = self.neighbourhood, pub_date = '2019-10-10')

   
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))



class NeighbourhoodTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='Test', password='12345')
        self.location = Location(id=1, name='Test')
        self.neighbourhood = Neighbourhood(id=1,name='Test',location=self.location,occupants=100)

    
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_create_neighbourhood(self):
        self.location.save()
        self.neighbourhood.create_neighbourhood()
        self.assertTrue(len(Neighbourhood.objects.all()) > 0)

    def test_delete_neighbourhood(self):
        self.location.save()
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood = Neighbourhood.objects.get(id=1)
        self.neighbourhood.delete_neighbourhood()
        self.assertTrue(len(Neighbourhood.objects.all()) == 0)

    def test_find_neighbourhood(self):
        self.location.save()
        self.neighbourhood.create_neighbourhood()
        self.searched_neighbourhood = Neighbourhood.find_neighbourhood(1)
        self.assertTrue(self.searched_neighbourhood == self.neighbourhood)

        
        
class BusinessTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='Test', password='12345')
        self.location = Location(id=1, name='Test')
        self.neighbourhood = Neighbourhood(id=1,name='Test',location=self.location,occupants=100)
        self.profile = Profile(id=1, name=self.user.username, neighbourhood = self.neighbourhood, bio = 'Testing', email = 'testing@gmail.com',user = self.user)
        self.profile.save()
        self.location = Location(id=1, name='Test')
        self.location.save()
        self.neighbourhood = Neighbourhood(id=1,name='Test',location=self.location,occupants=100)
        self.neighbourhood.save()
        self.business = Business(id=1,name='Test',email='testing@gmail.com',description='Test description',neighbourhood=self.neighbourhood,user=self.profile)
        self.business.save()

    
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        self.business.create_business()
        self.assertTrue(len(Business.objects.all()) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_find_business(self):
        self.business = Business.find_business(1)
        self.assertEqual(self.business.id, 1)

    