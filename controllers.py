
import numpy as np


class LandingController:
    pass
class Controller:
    pass





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

