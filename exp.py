from config import ConfigParse
from utils  import Schema
import gym

class Experiment:
    def __init__(self, config_file) -> None:
        self.config_file = config_file
        self.config = ConfigParse(config_file)
        self.config.parse()

        self.schema = None
        self.workload_generator = None

    
    def prepare(self):
        # ! todo 
        self.schema = Schema()
        self.workload_generator = None


        # TODO prepare workload and embedding workload
        # TODO generate canditate indexes


    def make_env(self):
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

        
        