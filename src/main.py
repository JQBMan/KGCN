import argparse
import numpy as np
from data_loader import load_data
from train import train

np.random.seed(555)


parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='movie', help='which dataset to use, must be in [movie]')
parser.add_argument('--aggregator', type=str, default='sum', help='which aggregator to use, must be in [sum]')
parser.add_argument('--n_epochs', type=int, default=10, help='the number of epochs')
parser.add_argument('--neighbor_sample_size', type=int, default=8, help='the number of neighbors to be sampled')
parser.add_argument('--dim', type=int, default=16, help='dimension of user and entity embeddings')
parser.add_argument('--n_iter', type=int, default=0, help='number of iterations when computing entity representation')
parser.add_argument('--batch_size', type=int, default=65536, help='batch size')
parser.add_argument('--l2_weight', type=float, default=0., help='weight of l2 regularization')
parser.add_argument('--lr', type=float, default=0.1, help='learning rate')
parser.add_argument('--ratio', type=float, default=10., help='size of training dataset')
args = parser.parse_args()

show_loss = False
data = load_data(args)
train(args, data, show_loss)
