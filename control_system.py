from fsm import FSM, Transition
from typing import List
from controllers import Controller, OrientationController
from enum import Enum, auto
from math import sqrt

from statemachine import StateMachine, State

class ControlSystemMachine(StateMachine):
    start = State('START', initial=True)
    navigation = State('NAVIGATION')
    orientation = State('ORIENTATION')
    end = State('END')

    navigate = start.to(navigation) | orientation.to(navigation)
    orient = navigation.to(orientation)
    end = navigation.to(end) | orientation.to(end)

class ControlSystem:
    """
    TODO:
        * Handle transitions between states
        * Handle the chaning of controllers, and the setpoint
    """
    def __init__(self):
        self.fsm = ControlSystemMachine()
        self.orientation_controller = OrientationController()
        # self.current_controller = self.choose_controller()
        self.setpoint = self.choose_controller().setpoint

    def choose_controller(self, observation: List[float]) -> Controller:
        return self.state_controller_mapping[self.fsm.current_state]

    def choose_action(self, observation: List[float]) -> List[float]:
        # return self.choose_controller().choose_action(observation)
        pass

        # if too far away from target(center), use navigation controller
        # if orientation is too steep, while inside the range of the target, use orientation controller
    def step(self, observation: List[float]):
        self.controller = self.choose_controller(observation)
        self.setpoint = self.controller.setpoint
            

        # change the setpoint (whether or not the controller is changed)
        pass


# The individual controller should be calculating the error, and the setpoint
def calculate_error(setpoint: float, observation: float) -> float: # TODO: make this a function of the ControlSystem
    """
    The error calculates the angle of the craft from the LAND area
    """
    return observation - setpoint
