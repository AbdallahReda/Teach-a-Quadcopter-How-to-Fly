import numpy as np
from physics_sim import PhysicsSim

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""
        reward = 1.-.1*(abs(self.sim.pose[:3] - self.target_pos)).sum()
        if reward > 0:
            reward = 1
        else:
            reward = -1
        return reward
        
        if velocity[0] > 0 or velocity[0] < 0:
            reward -= 10
        if velocity[2] > 0 or velocity[2] < 0:
            reward -= 10
        if velocity[1] > 0:
            reward += 50
        euler_angles = self.sim.pose[3:6].sum()
        reward -= euler_angles
        
        lateral_distance = ((current_pos[0] - self.target_pos[0]) + (current_pos[2] - self.target_pos[2])) ** 2
        reward -= lateral_distance
        vertical_distance = (current_pos[1] - self.target_pos[1]) ** 2
        if vertical_distance != 0:
            reward += 100 / vertical_distance 
        
        if done and self.sim.time < self.sim.runtime:
            reward = -1
        
    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state