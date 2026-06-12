from jinja2 import Environment, FileSystemLoader


def render_dashboard(dashboard, charts):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("dashboard_template.html")

    html = template.render(
        title=dashboard.title, rows=dashboard.rows, cols=dashboard.cols, charts=charts
    )

    with open(f"builds/{dashboard.title}.html", "w") as f:
        f.write(html)
