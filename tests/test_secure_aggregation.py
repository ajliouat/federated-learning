import unittest
from src.utils.secure_aggregation import secure_aggregation
from src.models.federated_model import FederatedModel

class TestSecureAggregation(unittest.TestCase):
    def test_secure_aggregation(self):
        models = [FederatedModel() for _ in range(3)]
        aggregated_model = secure_aggregation(models)
        self.assertIsNotNone(aggregated_model)

if __name__ == "__main__":
    unittest.main()