from typing import Literal, Type
import pandas as pd
import gymnasium as gym

def make_env(
    data: pd.DataFrame,
    env_cls: Type[gym.Env],
    **env_kwargs
):
    env = env_cls(df=data, **env_kwargs)
    env, _ = env.get_sb_env()
    return env

def train(
    env,
    model_name: str,
    model_params: dict,
    drl_lib: Literal['elegantrl', 'stable_baselines3'] = 'stable_baselines3',
    drl_params: dict = ...,
    save_model_path: str = ...,
    **kwargs
):
    if drl_lib == 'elegantrl':
        raise NotImplementedError(f'{drl_lib} is not implemented yet!')
    elif drl_lib == 'stable_baselines3':
        from finrl.agents.stablebaselines3.models import DRLAgent
        agent = DRLAgent(env=env)
    else:
        raise NotImplementedError(f'{drl_lib} is not implemented yet!')

    model = agent.get_model(model_name=model_name, model_kwargs=model_params)

    trained_model = agent.train_model(
        model=model,
        **drl_params
    )
    trained_model.save(save_model_path)
    return trained_model

def test(
    env: gym.Env,
    model,
    drl_lib: Literal['elegantrl', 'stable_baselines3'] = 'stable_baselines3',
    **kwargs
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if drl_lib == 'stable_baselines3':
        from finrl.agents.stablebaselines3.models import DRLAgent as agent
    else:
        raise NotImplementedError(f"{drl_lib} not implemented yet!")
    df_account_value, df_actions = agent.DRL_prediction(
        model=model,
        environment=env,
        **kwargs
    )
    return df_account_value, df_actions
