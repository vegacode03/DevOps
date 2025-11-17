import unittest
from app import app
import werkzeug

# Correção para evitar erro no werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "0.0"


class SimpleAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    # 1️⃣ Teste do endpoint /
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # 2️⃣ Teste do endpoint /items
    def test_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

    # 3️⃣ Teste do endpoint protegido sem token
    def test_protected_without_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
