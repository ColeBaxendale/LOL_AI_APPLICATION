import requests
from bs4 import BeautifulSoup


class ServiceScrapper:
    def get_status(self):
        service_status_list = []
        # Define the URL of the web page to scrape
        url = "https://developer.riotgames.com/api-status/"

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all the service containers
            service_containers = soup.find_all("div", class_="service")

            # Loop through each service container
            for service_container in service_containers:
                # Extract the service name
                service_name = service_container.text.strip()

                # Determine the status based on the presence of the checkmark
                service_status = "Online"

                # If the service name contains additional regions within parentheses, extract the common service name
                if "(" in service_name:
                    common_service_name = service_name.split("(")[0].strip()
                    service_status = "Offline or Partly Offline"
                else:
                    common_service_name = service_name

                # Append the common service name and status to the list
                service_status_list.append({"Service": common_service_name, "Status": service_status})
            return service_status_list
        else:
            print("Failed to retrieve the web page.")
            return None
