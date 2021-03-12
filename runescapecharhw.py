class Jorah():
    def __init__(self, rsn, date_created, magic_xp, magic_level, membership):
        self.rsn = rsn
        self.date_created = date_created
        self.magic_xp = magic_xp
        self.magic_level = magic_level
        self.membership = membership

    def __str__(self):
        return f"""This player is called {rsn}. He created his account on {date_created}. His current magic xp is {magic_xp} 
                    and level is {magic_level}. His membership status is currently {membership}."""
                    
    