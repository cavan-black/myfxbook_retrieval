import requests

"""
MyFXBook API Connection instance
"""
class Myfxb():
    def __init__(self, email, password, account) -> None:
        self.email = email
        self.password = password
        self.account = account
        self.ENDPOINT = "https://www.myfxbook.com/api/"
        self.session_id = ""
        self.account_id = ""
        self.open_orders = []
    
    def login(self) -> None:
        try:
            login_request = f'{self.ENDPOINT}login.json?email={self.email}&password={self.password}'
            response = requests.get(login_request)
        except requests.exceptions.Timeout:
            # Setup for retry!
            print("TIMEOUT")
        except requests.exceptions.TooManyRedirects:
            print("BAD URL")
            exit()
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        else:
            if response.json()['error'] == 'True':
                print(f'ERROR IN LOGIN: {response.json()["message"]}')
                exit()
            else:
                print(response.json())
                self.session_id = response.json()['session']

    def logout(self) -> None:
        try:
            logout_request = f'{self.ENDPOINT}logout.json?session={self.session_id}'
            response = requests.get(logout_request)
        except requests.exceptions.Timeout:
            # Setup for retry!
            print("TIMEOUT")
        except requests.exceptions.TooManyRedirects:
            print("BAD URL")
            exit()
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        if response.json()['error'] == 'True':
                print(f'ERROR IN LOGOUT: {response.json()["message"]}')
                exit()

    def get_accounts(self) -> None:
        try:
            print(self.session_id)
            accounts_request = f'{self.ENDPOINT}get-my-accounts.json?session={self.session_id}'
            response = requests.get(accounts_request)
            print(response.json())
        except requests.exceptions.Timeout:
            # Setup for retry!
            print("TIMEOUT")
        except requests.exceptions.TooManyRedirects:
            print("BAD URL")
            exit()
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        if response.json()['error'] == 'True':
                print(f'ERROR IN GET_ACCOUNTS: {response.json()["message"]}')
                exit()
        
    def get_trades(self) -> None:
        try:
            trades_request = f'{self.ENDPOINT}get-open-trades.json?session={self.session_id}&id={self.account}'
            response = requests.get(trades_request).text
            print(response)
        except requests.exceptions.Timeout:
            # Setup for retry!
            print("TIMEOUT")
        except requests.exceptions.TooManyRedirects:
            print("BAD URL")
            exit()
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        