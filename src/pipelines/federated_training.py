import torch
from src.models.federated_model import FederatedModel
from src.utils.secure_aggregation import secure_aggregation

def federated_training(clients_data, num_rounds=10):
    global_model = FederatedModel()
    for round in range(num_rounds):
        client_models = []
        for data in clients_data:
            model = FederatedModel()
            optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
            # Train model on client data
            client_models.append(model)
        global_model = secure_aggregation(client_models)
    return global_model