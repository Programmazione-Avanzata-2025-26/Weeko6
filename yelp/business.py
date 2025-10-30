from dataclasses import dataclass

@dataclass
class Business:
    business_id: str
    full_address: str
    active : str
    categories : str
    city : str
    review_count : int
    business_name : str
    neighborhoods : str
    latitude : float
    longitude : float
    state : str
    stars : float

    def __str__(self):
        return self.business_id+" "+self.full_address+" "+self.active+" "+self.categories+" "+self.city+" "+str(self.review_count)+" "+self.business_name+" "+self.neighborhoods+" "+str(self.latitude)+" "+str(self.longitude)+" "+self.state+" "+str(self.stars)

    def __eq__(self, other):
        return self.business_id == other.business_id

    def __hash__(self):
        return hash(self.business_id)