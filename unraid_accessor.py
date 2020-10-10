import mechanize, json, os, time, urllib

class UnraidAccessor:
    def __init__(self) -> None:
        super().__init__()
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.base_url = os.getenv("UNRAID_URL", 'http://Tower.local')
        print(f"using {self.base_url} as url")
        self.login()
        

    def login(self):
        try:
            page = self.br.open(self.base_url)
            self.br.select_form(action="/login")
            self.br["username"] = os.getenv("LOGIN_USERNAME", "root")
            self.br['password'] = os.getenv("LOGIN_PASSWORD", "")
            response = self.br.submit()
            logged_in = response.geturl() == f'{self.base_url}/Main'
            print(response.geturl())
        except urllib.error.URLError:
            return False
        return logged_in

    def get_data(self):
        try:
            data = self.br.open(f'{self.base_url}/plugins/jsonapi/api.php?file=disks.ini')
        except urllib.error.URLError:
            return False, "Unable to reach host ip"
        try:
            parsed_data = json.loads(data.read())
            return True, parsed_data
        except json.JSONDecodeError:
            return False, "Response data invalid"


