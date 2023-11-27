from fsm import FSM, State, Transition
from typing import List
from controllers import Controller, OrientationController, LandingController

class ControlSystem:
    def __init__(self):
        self.fsm = FSM()
        self.controllers: List[Controller] = []
        self.states: List[State] = []
        self.setpoint = None # TODO: make this a function of the ControlSystem, this depends on the state, and how the state is defined
        self.state_controller_mapping = {
            State.FIX_ORIENTATION: OrientationController,
            State.LANDING: LandingController,
            
        }


    def observe(self, observation: float):
        self.observation = observation

    def step(self):
        self.fsm.step(self.observation)
def calculate_error(setpoint: float, observation: float) -> float: # TODO: make this a function of the ControlSystem
    """
    The error calculates the angle of the craft from the landing area
    """
    return observation - setpoint
