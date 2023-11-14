import gymnasium as gym
import time
import enum
env = gym.make("CartPole-v1",render_mode='human')
"""
I need to add visualization for the cart thingy
I want this controller to be flexible, where I could attach and remove any of the three components (proportional/integral,derivative)
at each time step the error needs to be calculated

at first, ill take the error as the angle of the pole from the upright position.

"""
from abc import ABC, abstractmethod



class Action(enum.Enum):
    RIGHT = 1,
    LEFT = 0


class ControllerComponent(ABC):
    """
    This is the base class for all controller components
    """     
    pass
    error = 0.0


    @abstractmethod
    def step(self):
        """
        This is called at each time step
        """
        pass


    @abstractmethod

    def choose_action(self, error: float) -> Action:
        """
        The error represents the angle of the pole from its upright position 
        """
        pass


class ProportionalController(ControllerComponent):
    def step(self):

        pass
    
    def choose_action(self, error: float) -> Action:
        chosen_action = Action.RIGHT


        return chosen_action


class Controller:
    
    def __init__(self, components: list[ControllerComponent]):
        self.components = components


    def choose_action(self, error: float) -> Action:
        """
        takes error as input and returns the action to perform
        """
        pass
    
    def step(self):
        """
        This is called at each time step

        updates each of the controller components.
        """
        for component in self.controller:
            component.step()




observation, info = env.reset(seed=42)

for time_step in range(1000):    
    env.render()
    # action = env.action_space.sample()
    p_component = ProportionalController()
    controller = Controller([p_component])
    action = controller.choose_action(observation)
    # action = 1
    # action = 0
    observation, reward, terminated, truncated, info = env.step(action)
    controller.step()
    
    print(f"angle: {observation[2]} | iteration: {time_step} | action: {action} | info: {info}")
    # unpack observation
    cart_position, cart_velocity, pole_angle, pole_velocity = observation
    if terminated or truncated:
        print("terminated or truncated")
        observation, info = env.reset()
    # time.sleep(0.2)
env.close()
