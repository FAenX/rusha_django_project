import yaml

def generate_domain_name(application_name):
    """Generate a domain name for the application.

    Args:

        application_name (str): The name of the application.

    Returns:

        str: A domain name.

    """
    try:
        with open(f'/home/manu/private/rusha_django/rusha_config.yml', 'r') as f:
            yaml_content = yaml.load(f, Loader=yaml.FullLoader)
            host = yaml_content["host_name"]
            domain_name = f"{host['prefix']}://{application_name}.{host['name']}"
            return domain_name
    except Exception as e:
        raise e