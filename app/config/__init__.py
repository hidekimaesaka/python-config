import os

from dotenv import load_dotenv

from app.config.base import base_configs


def init(mode=None):

    # load .env data on environment variables
    load_dotenv(override=True)
    
    if mode == 'production':

        """
        if you are using frameworks with dependencie injection pattern
        like flask, you can receive the app in the params of the init function
        and inject the base_configs on it

        on our case, we gonna build an script, sou we load the base config on the
        env vars instead.
        """

        env = os.environ
        config = base_configs.get(mode)

        env.update(config)


    else:

        env = os.environ
        config = base_configs.get('development')

        env.update(config)
