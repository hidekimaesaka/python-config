from os import environ

from app.config import init

from app.config.base import base_configs

def test_config_is_loading_the_correct_values_when_given_development_mode():
    
    """
    GIVEN = development mode
    WHEN = calling init function of the config module
    THEN = base config values must be development ones
    """
    mode = 'development'

    init(mode)
    
    expected_config = base_configs.get(mode)

    for key, value in expected_config.items():
        assert environ[key] == value


def test_config_is_loading_the_correct_values_when_given_production_mode():
    
    """
    GIVEN = production mode
    WHEN = calling init function of the config module
    THEN = base config values must be production ones
    """
    mode = 'production'

    init(mode)
    
    expected_config = base_configs.get(mode)

    for key, value in expected_config.items():
        print(key, value)
        assert environ[key] == value

def test_config_is_loading_the_development_mode_when_given_no_mode():

    """
    GIVEN = no mode
    WHEN = calling init function of the config module
    THEN = base config values must be development ones
    """

    init()
    
    expected_config = base_configs.get('development')

    for key, value in expected_config.items():
        print(key, value)
        assert environ[key] == value

def test_config_is_loading_the_development_mode_when_given_non_defined_mode():
    
    """
    GIVEN = non defined mode
    WHEN = calling init function of the config module
    THEN = base config values must be development ones
    """
    mode = 'something_we_didnot_create_in_the_base_config_file'

    init(mode)
    
    expected_config = base_configs.get('development')

    for key, value in expected_config.items():
        print(key, value)
        assert environ[key] == value
