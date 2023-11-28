from fsm import FSM, Transition
from typing import List
from controllers import Controller, OrientationController, LandingController
from enum import Enum, auto

class ControlSystemState(Enum):
    LANDING = auto(),


class ControlSystemFSM:
    
    def __init__(self):
        self.transitions: List[Transition] = [
        ]
        self.states: List[ControlSystemState] = [s for s in ControlSystemState]
        self.state_controller_mapping = {}
        self.current_state = ControlSystemState.LANDING
        self.fsm = FSM(transitions=self.transitions, states=self.states, initial_state=self.current_state)

class ControlSystem:
    """
    TODO:
        * Handle transitions between states
        * Handle the chaning of controllers, and the setpoint
    """
    def __init__(self):
        self.fsm = ControlSystemFSM()
        self.orientation_controller = OrientationController()
        self.controllers = {ControlSystemState.LANDING: self.orientation_controller}
        self.states: List[ControlSystemState] = [s for s in ControlSystemState]
        self.setpoint = None # TODO: make this a function of the ControlSystem, this depends on the state, and how the state is defined
        self.state_controller_mapping = {}

    def choose_controller(self) -> Controller:
        return self.controllers[self.fsm.current_state]

    def choose_action(self, observation) -> List[float]:
        if self.fsm.current_state == ControlSystemState.LANDING:
            chosen_controller: Controller = self.choose_controller()
            return chosen_controller.choose_action(observation)
        return [0,0]
        # WHAT IS THIS SUPPOSED TO DO? ANSWER: this is supposed to choose an action based on the current state of the fsm
    def step(self):
        # self.fsm.step(self.observation)
        pass


def calculate_error(setpoint: float, observation: float) -> float: # TODO: make this a function of the ControlSystem
    """
    The error calculates the angle of the craft from the landing area
    """
    return observation - setpoint
