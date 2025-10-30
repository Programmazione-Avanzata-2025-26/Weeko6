from dataclasses import dataclass

@dataclass
class User:
    user_id : str
    votes_funny : int
    votes_useful : int
    votes_cool : int
    name : str
    average_stars : float
    review_count : int

    def __str__(self):
        return self.user_id+" "+str(self.votes_funny)+" "+str(self.votes_useful)+" "+str(self.votes_cool)+" "+self.name+" "+str(self.average_stars)+" "+str(self.review_count)

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)