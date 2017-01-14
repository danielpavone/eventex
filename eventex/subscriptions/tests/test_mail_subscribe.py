from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Daniel Ferreira Pavone', cpf='12345678901',
                    email='danielpavone@gmail.com', phone='12-99999-9999')

        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'danielpavone@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Daniel Ferreira Pavone',
            '12345678901',
            'danielpavone@gmail.com',
            '12-99999-9999'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)