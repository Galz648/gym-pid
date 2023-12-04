
This is an attempt at creating a flight controller for the lunar lander project.
This is a continuous action space problem. The action space is a vector of 2 floats.
The first float is the main thruster power, the second float is the left thruster power/ right thruster power.
lets start with something simple, only thrusting the main engine at some constant speed.

I want to try and see if an event based fsm would work well here. for example, after getting to the desired spot above the target, the lander needs to descend.
if at any point the degree of orientation is larger than some constant, fix the orientation error

My intention is to explicitly ask what the external object, interfacing with it, needs to know about the state machine or any other encapsulated object.

steps to take:
    * refactor fsm
    * refactor control system (Sensor, controller, actuator, process, control system, feedback loop)
    * use the git prehook to generate fsm diagrams
    * add test for the control system
    * Control System - change the setpoint in according to the current state
    * Add a navigation state and navigation controller to the control system controllers
    * add different states, and have a different controller and setpoint for each state
    * Wondering when to add some pid functionality
