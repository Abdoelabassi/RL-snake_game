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

		state = torch.tensor(state, dtype=torch.float)
		next_state = torch.tensor(next_state, dtype=torch.float)
		action = torch.tensor(action, dtype=torch.long)
		reward = torch.tensor(reward, dtype=torch.float)

		if len(state.shape) == 1:

			#format : (1,x)

			state = torch.unsqueeze(state, 0)

			next_state = torch.unsqueeze(next_state,0)

			action = torch.unsqueeze(action,0)

			reward = torch.unsqueeze(reward,0)

			done = (done,)

		#Bellman equation: implementation
		#1:predict Q value of the current state

		pred = self.model(state)

		#2: Q_new = reward + gamma*max(current Q value with the new state) -> only if done
		#pred[argmax(action)] = Q_new

		tar = pred.clone()

		for i in range(len(done)):

			Q_new = reward[i]

			if not done[i]:

				Q_new = reward[i] + self.gamma* torch.max(self.model(next_state[i]))

		    tar[i][torch.argmax(action).item()] = Q_new


		self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()



