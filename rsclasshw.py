class Jorah():
    
    def __init__(self, rsn, date_created, magic_xp, magic_level, membership):
        self.rsn = rsn
        self.date_created = date_created
        self.magic_xp = magic_xp
        self.magic_level = magic_level
        self.membership = membership

    def __str__(self):
        return f"""This player is called {self.rsn}. He created his account on {self.date_created}. His current magic xp is {self.magic_xp} 
                    and magic level is {self.magic_level}. His membership status is currently {self.membership}."""
                    
if __name__ == "__main__":
    
    JorahRS = Jorah(rsn="jorah", date_created="January 27th, 2014", magic_xp="13,000,000", magic_level=99, membership="inactive")
    
    print(JorahRS)