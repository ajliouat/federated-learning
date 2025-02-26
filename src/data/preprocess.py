import torch

def preprocess_data(raw_data_path, processed_data_path):
    """
    Preprocess raw data and save it in the processed data directory.
    
    Args:
        raw_data_path (str): Path to the raw data.
        processed_data_path (str): Path to save the processed data.
    """
    # Example: Load raw data (e.g., CSV, images) and preprocess it
    raw_data = torch.randn(1000, 784)  # Example: Random data
    labels = torch.randint(0, 10, (1000,))  # Example: Random labels
    
    # Save processed data
    torch.save({'features': raw_data, 'labels': labels}, processed_data_path)
    print(f"Processed data saved to {processed_data_path}")