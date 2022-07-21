import imp
import gym
from gym_db.common import EnvironmentType


def train():
    env = gym.make()


def make_env(id: str):
    action = None

    observation = None

    reward = None

    env = gym.make(
                f"DB-v1",
                environment_type=1,
                config={
                    # "database_name": self.schema.database_name,
                    # "globally_indexable_columns": self.globally_indexable_columns_flat,
                    # "workloads": workloads,
                    # "random_seed": self.config["random_seed"] + env_id,
                    # "max_steps_per_episode": self.config["max_steps_per_episode"],
                    # "action_manager": action_manager,
                    # "observation_manager": observation_manager,
                    # "reward_calculator": reward_calculator,
                    # "env_id": env_id,
                    # "similar_workloads": self.config["workload"]["similar_workloads"],
                },
            )
    return env



if __name__ == "__main__":
    pass
