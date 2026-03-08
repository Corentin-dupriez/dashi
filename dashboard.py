from parser import parse_yaml, NoConfigFile
from pathlib import Path


class Dashboard:
    DASHBOARD_FOLDER = Path.cwd() / "dashboards"

    def load_dashboard(self):
        data = parse_yaml(self.DASHBOARD_FOLDER, "dashboard")
        dashboard = data["dashboard"]
        print(dashboard)
