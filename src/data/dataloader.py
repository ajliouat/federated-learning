import torch
from torch.utils.data import DataLoader, TensorDataset

def load_data(data_path, batch_size=32):
    """
    Load data from the specified path and create a DataLoader.
    
    Args:
        data_path (str): Path to the data file.
        batch_size (int): Batch size for the DataLoader.
    
    Returns:
        DataLoader: DataLoader for the dataset.
    """
    data = torch.load(data_path)
    dataset = TensorDataset(data['features'], data['labels'])
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)