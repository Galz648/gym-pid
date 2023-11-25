"""
"""
from enum import Enum, auto
from typing import List, Dict, Tuple, Callable

"""
Diagram 
Thoughts and Questions.

2 goals, 1 after another.
* the first - getting to 90 degrees (0 degrees with the lateral axis of the landing point)
* the second - landing from that point. if the degree between the lander and the lateral line becomes to big, a tranisition to the navigation state is made.
* I wonder if the fsm is event based, I wonder if I really need an FSM here, but I thought it would be nice
Transitions:
* 
"""
class State(Enum):
    START = auto(),
    END = auto(),
    FIX_ORIENTATION = auto(),

    

    def __eq__(self, other: object) -> bool:
        if self.value == other.value:
            return True
        
        return False




class Transition:
    def __init__(self, from_state: State, to_state: State):
        self.from_state = from_state
        self.to_state = to_state



    def __eq__(self, other: object) -> bool:
        if self.from_state == other.from_state and self.to_state == other.to_state:
            return True
        
        return False
        
class FSM:
    def __init__(self, transitions: List[Transition], states: List[State]):
        self.valid_tranisitions = transitions
        self.states = states
        self.current_state = State.START
        self.actions = { # Dict[Tuple[str, callable]]
        }
    

    @property.setter
    def add_transition(self, t: Transition):
        # add error handle for if the tranisition already exists and such
        self.valid_tranisitions.append(t)


        
    def transition(self, t:Transition):
        if self.is_transition_valid(t):
            self.current_state = t.to_state
        else:
            raise Exception("Invalid transition")



    def is_transition_valid(self, t: Transition) -> bool:
        # TODO: add error handling for invalid transition
        return t in self.valid_tranisitions and t.from_state in self.states and t.to_state in self.states



def main():
    # Create states
    landing = State.LANDING
    landing_done = State.LANDING_DONE
    # Create transitions
    landing_to_landing_done = Transition(landing, landing_done)
    # Create FSM
    transitions = [landing_to_landing_done]
    fsm = FSM(transitions, [landing, landing_done])
    
    # Test transitions
    assert fsm.is_transition_valid(landing_to_landing_done) == True

    # Test invalid transitions
    assert fsm.is_transition_valid(Transition(landing_done, landing)) == False



if __name__ == "__main__":
    main()
