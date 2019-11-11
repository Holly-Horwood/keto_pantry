from django.test import TestCase, Client
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User

class TestAccountsForm(TestCase):

    def test_login_username_and_password_required(self):
        form = UserLoginForm({'username': 'admin',
                              'password': 'password123'})
        self.assertTrue(form.is_valid())

    def test_can_create_user_with_required_fields(self):
        form = UserRegistrationForm({'username': 'admin',
                                     'email': 'admnin@example.com',
                                     'password1': 'password123',
                                     'password2': 'password123'})
        self.assertTrue(form.is_valid())    

    def test_registration_passwords_match(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertTrue(form.is_valid())    

    def test_cant_create_user_unless_password_match(self):
        form = UserRegistrationForm({'username': 'admin',
                                     'email': 'admin@example.com',
                                     'password1': 'password123',
                                     'password2': 'password456'})
        self.assertFalse(form.is_valid())  

    def test_cant_register_user_unless_required_field_filled(self):
        form = UserLoginForm({'username': 'admin'})
        self.assertFalse(form.is_valid())     

    def test_missing_username_throws_correct_error(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_missing_password_throws_correct_error(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])



