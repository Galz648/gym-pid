from fsm import FSM, State, Transition
from control_system import ControlSystem
import gymnasium as gym

from enum import Enum, auto

class SimulationState(Enum):
    START = auto(),
    IN_PROGRESS= auto(),
    END = auto()



class Simulation:

    def __init__(self, env: gym.Env, control_system: ControlSystem, fsm: FSM):
            self.env = env
            self.control_system = control_system
            self.observation = None
            self.fsm = fsm

    def setup(self):
            self.observation, info = self.env.reset()

    def step(self, action):
            observation, reward, terminated, truncated, info = self.env.step(action)
            self.observation = observation
            return observation


    def simulate(self):
            self.setup()
            # some default action/ first action has to be defined
            while self.fsm.current_state != State.END:
                # feed the observation to the control system
                controller_action = self.control_system.choose_action(observation)
                observation = self.step(controller_action)

    """
    # for _ in range(1000): #
        #     error = calculate_error(setpoint, observation=observation[4]) # TODO: move to Control System
        #     action_to_perform = Controller.decide_action(error) 
        #     print(f"action: {action_to_perform}")
        #     observation, reward, terminated, truncated, info = env.step(action_to_perform)
        #     x,y = observation[0], observation[1]
        #     # x_linear_velocity, y_linear_velocity = observation[2], observation[3]
        #     angle = observation[4]
        #     # angular_velocity = observation[5]
        #     # left_leg_contact:bool = observation[6]
        #     # right_leg_contact: bool = observation[7]

        #     # print all in different lines
        #     # print(f"action: {action}")
        #     print(f"(x,y):({x},{y})")
        #     print(f"angle:{angle}")   
        #     env.render()
        #     time.sleep(0.1)
        #     if terminated or truncated:
        #         observation, info = env.reset()
        # env.close()
    """
