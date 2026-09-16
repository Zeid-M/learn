import os

from jinja2 import Environment, FileSystemLoader


def prepare_template_body(email_template_path: str, **kwargs):
    # Split the email template path into directory and filename
    template_directory_and_filename = os.path.split(email_template_path)

    # Create a Jinja2 environment using the directory of the email template
    env = Environment(loader=FileSystemLoader(template_directory_and_filename[0]))

    # Load the email template from the filename
    template = env.get_template(template_directory_and_filename[1])

    # Render the email template with the provided keyword arguments
    template_body = template.render(**kwargs)

    # Return the rendered email body
    return template_body


print(
    prepare_template_body(
        "./Python/Modules/jinjaTests/templates/helloName.jinja", name="Zeid"
    )
)
