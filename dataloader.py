import pybullet as p
import numpy as np

data_path = ""
data = p.loadURDF(data_path)

observations = []
actions = []
rewards = []
done_flags = []

num_steps = ""

for i in range(num_steps):
    action = "アクション"
    obervation, reward, done, _ = env.step(action)
    observations.append(obervation)
    actions.append(reward)
    done_flags(done)

observations = np.array(observations)
actions = np.array(actions)
rewards = np.array(rewards)
done_flags = np.array(done_flags)

np.save("file_path", observations=observations,actions=actions,rewards=reward,done_flags=done_flags)
p.disconnect()