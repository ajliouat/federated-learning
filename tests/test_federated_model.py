import unittest
from src.models.federated_model import FederatedModel

class TestFederatedModel(unittest.TestCase):
    def test_forward(self):
        model = FederatedModel()
        input = torch.randn(1, 784)
        output = model(input)
        self.assertEqual(output.shape, (1, 10))

if __name__ == "__main__":
    unittest.main()