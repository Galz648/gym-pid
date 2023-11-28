from fsm import FSM, State, Transition
from control_system import ControlSystem
import gymnasium as gym
from typing import List, Tuple
from enum import Enum, auto

class SimulationState(Enum):
	START = auto(),
	IN_PROGRESS= auto(),	
	END = auto()

	def __eq__(self, other: object) -> bool: # TODO: is this the correct way to do this?
		if self.value == other.value:
			return True
        
		return False

class SimulationFSM:
	def __init__(self, intial_state: SimulationState):
		self.transitions: List[Transition] = [
		Transition(from_state=SimulationState.START, to_state=SimulationState.END)
		]
		self.states: List[SimulationState] = [s for s in SimulationState]
		self.state_controller_mapping = {}
		self.fsm = FSM(transitions=self.transitions, states=self.states, initial_state=intial_state)

	#@property.setter
	def set_state(self, state: SimulationState):
		self.fsm.current_state = state


	def end_state(self):
		return self.fsm.current_state == SimulationState.END
	def add_transition(self, t: Transition):
		# add error handle for if the tranisition already exists and such
		self.transitions.append(t)
		
	def transition(self, t:Transition):
		valid_transition = self.is_transition_valid(t) # Should this be checked here ? What are the responsabillities of this function

		if valid_transition: 
			self.set_state(t.to_state)
		else:
			raise Exception("Invalid transition")

	def is_transition_valid(self, t: Transition) -> bool:
        # TODO: add error handling for invalid transition
		return t in self.transitions and t.from_state in self.states and t.to_state in self.states

	@property
	def current_state(self):
		return self.fsm.current_state
	
	def step(self, step_info: Tuple[List[float], bool, bool]):
		"""
		Should change the internal state of the fsm, in according to the given environment information.
		The state might not change on every state
		"""
		observation, terminated, truncated = step_info

		if terminated or truncated:
			self.transition(Transition(self.current_state, SimulationState.END)) # TODO: only require to_state?, more clean

		elif self.current_state == SimulationState.START:
			self.transition(Transition(self.current_state, SimulationState.IN_PROGRESS))

class Simulation:
	def __init__(self, env: gym.Env, control_system: ControlSystem):
		self.env = env
		self.control_system = control_system
		self.observation = None
		self.fsm = SimulationFSM(SimulationState.START)

	def setup(self):
		self.observation, info = self.env.reset()

	def step(self, action): # Check if terminated or truncated, and if so, change fsm state
		observation, reward, terminated, truncated, info = self.env.step(action)
		self.observation = observation
		return observation, terminated, truncated



	def simulate(self):
		self.setup()
		# some default action/ first action has to be defined
		while not self.fsm.end_state():
			# feed the observation to the control system
			controller_action = self.control_system.choose_action(self.observation[4])
			self.observation, terminated, truncated = self.step(controller_action)
			self.fsm.step((self.observation, terminated, truncated))
			

