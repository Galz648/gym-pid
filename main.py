import gymnasium as gym
import time
import enum
import gymnasium as gym
from typing import List
import numpy as np
from fsm import FSM, Transition, State

"""
This is an attempt at creating a flight controller for the lunar lander project.
This is a continuous action space problem. The action space is a vector of 3 floats.
The first float is the main thruster power, the second float is the left thruster power, and the third float is the right thruster power.
lets start with something simple, only thrusting the main engine at some constant speed.

I want to try and see if an event based fsm would work well here. for example, after getting to the desired spot above the target, the lander needs to descend.
if at any point the degree of orientation is larger than some constant, fix the orientation error

States:
* Fix orientation
* Landing
* Navigation

TODO:
    * Create a finite state machine
"""

class LandingController:
    pass
class Controller:
    pass

class ControlSystem:
    def __init__(self):
        self.controllers: List[Controller] = []
        self.states: List[State] = []
        self.state_controller_mapping = {
            State.FIX_ORIENTATION: OrientationController,
            State.LANDING: LandingController,
            
        }
class OrientationController:
    @staticmethod
    def decide_action(error: float ) -> np.ndarray:
        # Given the error (related to orientation), choose an action that is opposite to this or    ientation
        

        if error < 0:
            # if thee error in negative, make an action in the positive angle direction - fire left thruster
            return np.ndarray(shape=(2,),buffer=np.array([-1.0, -0.51]))

        elif error > 0:
            # main will not fire, right thruster will fire at 50% power
            return np.ndarray(shape=(2,),buffer=np.array([-1.0, 0.51]))
        # do the opposite if the error is positive (need to add proportion in the future) - fire right thruster
        else:
            print("nothing was done")
            return np.ndarray(shape=(2,),buffer=np.array([-1, 0.0]))


def calculate_error(setpoint: float, observation: float) -> float:
    """
    The error calculates the angle of the craft from the landing area
    """
    return observation - setpoint

def main():

    # Initialize the FSM
    # Create states
    # s1 = State.FIX_ORIENTATION
    # s2  = State.LANDING_DONE
    # # Create transitions
    # landing_to_landing_done = Transition(s1, s2)
    # # Create FSM
    # transitions = [landing_to_landing_done]
    # fsm = FSM(transitions, [s1, s2])


    # TODO: Simplify this code block. this needs to be readable, declarative
    setpoint = 0.0
    env = gym.make("LunarLander-v2",render_mode='human',continuous=True)
    observation, info = env.reset(seed=42)
    for _ in range(1000): # 
        error = calculate_error(setpoint, observation=observation[4])
        action_to_perform = Controller.decide_action(error)
        action = env.action_space.sample()  # this is where you would insert your policy
        print(f"action(shape): {action.shape}")
        print(f"action: {action_to_perform}")
        observation, reward, terminated, truncated, info = env.step(action_to_perform)
        # print(f"observation: {observation}")
        x,y = observation[0], observation[1]
        # x_linear_velocity, y_linear_velocity = observation[2], observation[3]
        angle = observation[4]
        # angular_velocity = observation[5]
        # left_leg_contact:bool = observation[6]
        # right_leg_contact: bool = observation[7]

        # print all in different lines
        # print(f"action: {action}")
        print(f"(x,y):({x},{y})")
        print(f"angle:{angle}")   
        env.render()
        time.sleep(0.1)
        if terminated or truncated:
            observation, info = env.reset()
    env.close()


main()


