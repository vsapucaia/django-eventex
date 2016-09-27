from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_is_digit(self):
        """CPF must accept only digits"""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_capitalized(self):
        """Name must be capitalized"""
        # VITOR fortunato -> Vitor Fortunato
        form = self.make_validated_form(name='VITOR fortunato')
        self.assertEqual('Vitor Fortunato', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """E-mail is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """E-mail or phone must be informed"""
        form = self.make_validated_form(phone='', email='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Vitor Fortunato',
                     cpf='12345678901',
                     email='vsfortunato@gmail.com',
                     phone='27-981176970')
        data = dict(valid, **kwargs)

        form = SubscriptionForm(data)
        form.is_valid()
        return form
