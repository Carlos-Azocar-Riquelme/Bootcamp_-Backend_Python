class Patient:
    def __init__(self,name, current_city ):
        self.id = id
        self.name = name
        self.current_city= current_city

    def __dict__(self):
        return {
            "patiuent_id":self.id,
            "name": self.name,  
            "current_city": self.current_city
        }