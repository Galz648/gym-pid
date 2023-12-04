from typing import List, Optional
from controllers import Controller, OrientationController, NavigationController

from statemachine import StateMachine, State

class ControlSystemMachine(StateMachine):
    start = State('START', initial=True)
    navigation = State('NAVIGATION')
    orientation = State('ORIENTATION')
    end = State('END', final=True)

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
        # self.navigation_controller = NavigationController()
        self.controller = Optional[Controller]
        self.state_controller_mapping = {
            # self.fsm.navigation: self.navigation_controller,
            self.fsm.orientation: self.orientation_controller
        }

    def choose_controller(self, observation: List[float]) -> Controller:
        return self.orientation_controller # TODO: make this applicable to all controllers

    def choose_action(self, controller: Controller, observation: List[float]) -> List[float]:
        return controller.choose_action(observation)

        # if too far away from target(center), use navigation controller
        # if orientation is too steep, while inside the range of the target, use orientation controller
    def step(self, observation: List[float]): # should return an action to be taken
        """
        The step function should be called every time the simulation is stepped
        """
        controller = self.choose_controller(observation)
		# let the controller choose action
        controller_action = self.choose_action(controller, observation[4]) # feed the observation to the control system
        # TODO: step the sub-components of the control system
        return controller_action
		 
        # self.fsm.step((observation, terminated, truncated))
        


# The individual controller should be calculating the error, and the setpoint
def calculate_error(setpoint: float, observation: float) -> float: # TODO: make this a function of the ControlSystem
    """
    The error calculates the angle of the craft from the LAND area
    """
    return observation - setpoint
