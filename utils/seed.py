import random
import torch

def set_seed(seed):
    """
    Fixe le seed pour rendre la génération reproductible.
    """
    random.seed(seed)
    torch.manual_seed(seed)
