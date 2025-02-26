import unittest
from src.models.differential_privacy import apply_differential_privacy
from src.models.federated_model import FederatedModel

class TestDifferentialPrivacy(unittest.TestCase):
    def test_apply_differential_privacy(self):
        model = FederatedModel()
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        model, optimizer = apply_differential_privacy(model, optimizer, sample_rate=0.1, noise_multiplier=1.0, max_grad_norm=1.0)
        self.assertIsNotNone(model)
        self.assertIsNotNone(optimizer)

if __name__ == "__main__":
    unittest.main()