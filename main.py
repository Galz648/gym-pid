import gymnasium as gym
import time
import enum
import gymnasium as gym
from typing import List
import numpy as np
from control_system import ControlSystem
from simulation import Simulation




def simulate_moonlander(seed: int = 42, render_mode: str = 'human', continuous: bool = True):
    env = gym.make("LunarLander-v2",render_mode=render_mode,continuous=continuous)
    
    s = Simulation(env=env, control_system=ControlSystem())
    s.simulate()
    env.close() # TODO: this supposedly could be changed to the s.simulate() function, for clarity

def main():
    simulate_moonlander()


if __name__ == "__main__":
    main()


