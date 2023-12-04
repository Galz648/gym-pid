
import numpy as np
from abc import ABC, abstractmethod
class Controller(ABC):
    @abstractmethod
    def choose_action(self, observation: np.ndarray) -> np.ndarray:
        pass



class NavigationController(Controller):
    pass


class OrientationController(Controller):
    setpoint: float = 0.0

    def observation_to_process_variable(self, observation: np.ndarray) -> float:
        return observation[4]
    
    @staticmethod
    def choose_action(error: float) -> np.ndarray:
        # Given the error (related to orientation), choose an action that is opposite to this or    ientation
        
        if error < 0:
            # if thee error in negative, make an action in the positive angle direction - fire left thruster
            return np.ndarray(shape=(2,),buffer=np.array([0, -0.51]))

        elif error > 0:
            # main will not fire, right thruster will fire at 50% power
            return np.ndarray(shape=(2,),buffer=np.array([0, 0.51]))
        # do the opposite if the error is positive (need to add proportion in the future) - fire right thruster
        else:
            print("nothing was done")
            return np.ndarray(shape=(2,),buffer=np.array([-1, 0.0]))

    def calculate_error(self, setpoint: float, observation: float) -> float:
        """
        The error calculates the angle of the craft from the landing area
        """
        return OrientationController.setpoint - self.observation_to_process_variable(observation)
