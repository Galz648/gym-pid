import gymnasium as gym
import time
import enum
import gymnasium as gym
from typing import List
import numpy as np
from fsm import FSM, Transition, State
from control_system import ControlSystem, ControlSystemState
from simulation import Simulation, SimulationState

"""
This is an attempt at creating a flight controller for the lunar lander project.
This is a continuous action space problem. The action space is a vector of 3 floats.
The first float is the main thruster power, the second float is the left thruster power, and the third float is the right thruster power.
lets start with something simple, only thrusting the main engine at some constant speed.

I want to try and see if an event based fsm would work well here. for example, after getting to the desired spot above the target, the lander needs to descend.
if at any point the degree of orientation is larger than some constant, fix the orientation error

steps to take:
    * encapsulate how the simulation is run, and how the implementation is made.
    * add a basic start and end fsm to the simulation
    * add different states, and have a different controller and setpoint for each state 

TODO:
    * Create a finite state machine
"""


def simulate_moonlander(seed: int = 42, render_mode: str = 'human', continuous: bool = True):
    env = gym.make("LunarLander-v2",render_mode=render_mode,continuous=continuous)
    
    s = Simulation(env=env, control_system=ControlSystem())
    s.setup()
    s.simulate()
    env.close() # TODO: this supposedly could be changed to the s.simulate() function, for clarity

def main():
    simulate_moonlander()


if __name__ == "__main__":
    main()


