from .Service_Scrapper import ServiceScrapper

class ServerStatusChecker:
    def server_online(self):
        service = ServiceScrapper()
        server_online = False
        service_status_list = service.get_status()
        if service_status_list is not None:
            for item in service_status_list:
                if item['Status'] == 'Offline or Partly Offline':
                    server_online = False  
                    print(f"{item['Service']} is offline or not working correctly")
                else:
                    server_online = True  
            return server_online