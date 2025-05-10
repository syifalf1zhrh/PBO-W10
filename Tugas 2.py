
class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services, language):
        if language == 'English':
            print("Services Provided:")
        elif language == 'Indonesia':
            print("Layanan yang Tersedia:")
        else:
            print("Language not supported.")
            return
        for svc in services:
            print(svc,'')

    def list_pricing(self, services, language):
        if language == 'English':
            print("Pricing for Services:")
            for svc in services:
                print("For", Model.services[svc]['number'],
                    svc, "message you pay $",
                    Model.services[svc]['price'])
        elif language == 'Indonesia':
            print("Harga untuk Layanan:")
            for svc in services:
                print("Untuk setiap", Model.services[svc]['number'],
                    svc, "pesan Anda membayar $",
                    Model.services[svc]['price'])
        else:
            print("Language not supported.")
            return


class Controller(object):
    def __init__(self, language):
        self.model = Model()
        self.view = View()
        self.language = language
    
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services, self.language))
    
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services, self.language))
    
#Instansiasi objek
language = input("What language do you want to use? [1] English [2] Indonesia: ")
if language == '1':
    language = 'English'
elif language == '2':
    language = 'Indonesia'
else:
    print("Error. Choose the language number.")
    exit()

controller = Controller(language)
controller.get_services()
controller.get_pricing()