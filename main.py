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

class ControllerComponent(ABC):
    """
    This is the base class for all controller components
    """     
    pass

    @abstractmethod
    def step(self):
        """
        This is called at each time step
        """
        pass
class Action(enum.Enum):
    RIGHT = 1,
    LEFT = 0

class ProportionalController(ControllerComponent):
    
    pass

class Controller:
    
    def __init__(self, components: list[ControllerComponent]):
        self.components = components


    def choose_action(self, error: float) -> Action:
        """
        takes error as input and returns the action to perform
        """
        return Action.RIGHT
    
    def step(self):
        """
        This is called at each time step

        updates each of the controller components.
        """
        for component in self.controller:
            component.step()




observation, info = env.reset(seed=42)

for _ in range(1000):    
    env.render()
    # action = env.action_space.sample()
    p_controller = ProportionalController()
    controller = Controller([p_controller])
    action = controller.choose_action(observation)
    # action = 1
    # action = 0
    observation, reward, terminated, truncated, info = env.step(action)
    controller.step()
    
    print(f"angle: {observation[2]} | iteration: {_} | action: {action} | info: {info}")
    # unpack observation
    cart_position, cart_velocity, pole_angle, pole_velocity = observation
    if terminated or truncated:
        print("terminated or truncated")
        observation, info = env.reset()
    # time.sleep(0.2)
env.close()
