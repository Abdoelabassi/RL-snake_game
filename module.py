import torch

import torch.nn as nn

import torch.optim as optim

import torch.nn.functional as Func

import os


class Linear_QNet(nn.Module):

	def __init__(self, input_size, hidden_size, output_size):

		super().__init__()

		self.linear_1 = nn.Linear(input_size, hidden_size)

		self.linear_2 = nn.Linear(hidden_size, output_size)



	def forward(self, x):

		X = Func.rely(self.linear_1(x))

		X = self.linear_2(x)

		return X

	def save(self, file_name="model.pth")
