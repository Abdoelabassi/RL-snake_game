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

		X = Func.relu(self.linear_1(x))

		X = self.linear_2(x)

		return X

	def save(self, file_name="model.pth"):

		model_folder_path = "./model"

		if not os.path.exists(model_folder_path):

			os.makedirs(model_folder_path)

		file_name = os.path.join(model_folder_path)
		torch.save(self.state_dict(), final_move)


class QTrainer:

	def __init__(self, model, lr, gamma):

		self.lr = lr 
		self.gamma = gamma

		self.model =  model

		self.optimizer = optim.Adam(model.parameters(), lr=self.lr)

		self.criterion = nn.MSELoss()


	def train_step(self, state, action, reward, next_state, done):

		pass
