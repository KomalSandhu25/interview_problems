import requests
class Client:

    def __init__(self, api_url):
        self.dic = {}
        self.api_url = api_url

    def get(self):
        url = self.api_url
        response = requests.get(url)
        try:
            if response.status_code == 200:
                data = response.json()

                return data
            else:
                raise Exception("Failed to retrieve. Response code:", response.status_code)
        except Exception as e:
            print(e)
            return None


    def update(self, payload):
        url = self.api_url
        response = requests.put(url, json=payload)
        try:
           if response.status_code == 200:
                print("updated successfully")
           else:
                raise Exception("Failed to update. Response code:", response.status_code)
        except Exception as e:
            print(e)
            return None

def main():
    api_url = "https://example.com/api/"
    client = Client(api_url)
    client.get()


