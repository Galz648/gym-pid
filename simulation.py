from control_system import ControlSystem
import gymnasium as gym
from typing import List, Tuple, Optional
from statemachine import StateMachine, State

class SimulationMachine(StateMachine):
	start = State('Start', initial=True)
	in_progress = State('In Progress')
	end = State('End', final=True)

	sequence = start.to(in_progress) | in_progress.to(end)
	
	def on_start(self):
		print('Simulation started')

	def on_in_progress(self):
		print('Simulation in progress')

	def on_end(self):
		print('Simulation ended')


class Simulation:
	def __init__(self, env: gym.Env, control_system: ControlSystem):
		self.env = env
		self.control_system = control_system
		self.observation = Optional[List[float]]
		self.fsm = SimulationMachine()

	def setup(self):
		observation, info = self.env.reset()
		return observation, info

	def step(self, action): # Check if terminated or truncated, and if so, change fsm state
		observation, reward, terminated, truncated, info = self.env.step(action)
		if terminated or truncated:
			self.fsm.sequence() # end the simulation
		self.observation = observation
		return observation, reward, terminated, truncated



	def simulate(self):
		action: Optional[List[float]]= None # temporary
		observation, _ = self.setup()
		# some default action/ first action has to be defined
		while not self.fsm.end.is_active:
			action = self.control_system.step(observation)
			observation, reward, terminated, truncated = self.step(action)
			print(f"observation: {self.observation[4]}")
			

			

