import gymnasium as gym
import time
import enum
import gymnasium as gym
from typing import List

"""
This is an attempt at creating a flight controller for the lunar lander project.
This is a continuous action space problem. The action space is a vector of 3 floats.
The first float is the main thruster power, the second float is the left thruster power, and the third float is the right thruster power.
lets start with something simple, only thrusting the main engine at some constant speed.

my strategy would be to try and stabilize the moon lander, using a proportional reaction to the angle  of the lander.
starting with the discrete action would be simpler since I wouldnt have to understand or manage the power at which the thrusters are acting.
"""
class ActionType(enum.Enum):
    MOVE_FORWARD = 1
    MOVE_BACKWARD = 2
    TURN_LEFT = 3
    TURN_RIGHT = 4

    def __init__(self, value):
        self.value = value

    def get_float_argument(self):
        return self.value

class Controller:
    @staticmethod
    def decide_action(angle: float) -> ActionType:
        # Given the angle at which the lander is oriented, choose an action that is opposite to this orientation
        pass



def main():
    env = gym.make("LunarLander-v2",render_mode='human',continuous=True)
    observation, info = env.reset(seed=42)
    for _ in range(1000): # 
        action = env.action_space.sample()  # this is where you would insert your policy
        print(f"action: {action}")
        observation, _, terminated, truncated, info = env.step(action)
        # print(f"observation: {observation}")
        x,y = observation[0], observation[1]
        # x_linear_velocity, y_linear_velocity = observation[2], observation[3]
        angle = observation[4]
        # angular_velocity = observation[5]
        # left_leg_contact:bool = observation[6]
        # right_leg_contact: bool = observation[7]

        # print all in different lines
        print(f"action: {action}")
        print(f"(x,y):({x},{y})")
        print(f"angle:{angle}")   
        env.render()
        time.sleep(0.1)
        if terminated or truncated:
            observation, info = env.reset()
    env.close()


main()


