import torch

def save_pytorch_model(model, path):
    torch.save(model, path)

def load_pytorch_model(path):
    model = torch.load(path).eval()
    return model