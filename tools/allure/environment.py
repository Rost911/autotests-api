from config import settings


def create_allure_environment_file():
    # Create a list of items in the format {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]

    # Combine all items into a single string separated by new lines
    properties = '\n'.join(items)

    # Open the file ./allure-results/environment.properties for writing
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Write the variables to the file