from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = "templates"     
env= Environment(loader=FileSystemLoader(TEMPLATES_DIR))


def render_template(template_name, context = None):
    try:
        template = env.get_template(template_name)
        return template.render(context or {})
    except FileNotFoundError:
        return "Template not found"

