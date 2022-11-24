import yaml 


def get_hostname():
    """Get host_name.

    Returns:

        str: host_name.

    """
    try:
        with open(f'rusha_config.yml', 'r') as f:
            yaml_content = yaml.load(f, Loader=yaml.FullLoader)
            host_name = yaml_content["host_name"]
            return f"{host_name['prefix']}://{host_name['name']}"
    except Exception as e:
        raise e