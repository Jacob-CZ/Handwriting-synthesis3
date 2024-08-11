import torch
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, '..')
from utils import plot_stroke

from utils.constants import Global
from utils.dataset import HandwritingDataset
from utils.data_utils import data_denormalization, data_normalization, valid_offset_normalization
from models.models import HandWritingPredictionNet, HandWritingSynthesisNet
from generate import generate_unconditional_seq, generate_conditional_sequence
data_path = 'data/'
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# seed = 128
# if seed:
# print("seed:",seed)
#     torch.manual_seed(seed)
#     np.random.seed(seed)
model_path = 'results/synthesis/best_model_synthesis_4.pt'

train_dataset = HandwritingDataset(data_path, split='train', text_req=True)
print(train_dataset.char_to_id)
# print(train_dataset.id_to_char)
# print(train_dataset.idx_to_char(np.arange(26,32)))
char_seq = "Dear valued shoppers"
bias = 1
is_map = True
ytext = char_seq + "           "


gen_seq, phi = generate_conditional_sequence(
        model_path, char_seq, device, train_dataset.char_to_id,
        train_dataset.idx_to_char, bias, prime=False, prime_seq=None, real_text=None, is_map=is_map)

gen_seq = data_denormalization(Global.train_mean, Global.train_std, gen_seq)