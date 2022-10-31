import yaml

def generate_application_path(application_name):
    """Generate file path for new application"""
    try:
        with open(f'/home/manu/private/rusha_django/rusha_config.yml', 'r') as f:
            yaml_content = yaml.load(f, Loader=yaml.FullLoader)
            applications_dir = yaml_content['applications_dir']
            application_path = f'{applications_dir}/{application_name}'
            return application_path
    except Exception as e:
        raise e

    
        