import requests
from requests.exceptions import RequestException

def check_application_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        
        if status_code == 200:
            print(f"The application at {url} is UP. Status Code: {status_code}")
        else:
            print(f"The application at {url} is DOWN. Status Code: {status_code}")
    except RequestException as e:
        print(f"Failed to reach the application at {url}. Error: {e}")

if __name__ == "__main__":
    # Replace 'http://example.com' with the URL of the application you want to check
    application_url = 'http://example.com'
    
    check_application_status(application_url)