class classHero():
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
ml = classHero("Hanabi", "Marksman")
ml2 = classHero("Lesley", "Marksman")

print(f"{ml.name}\n{ml.role}")

print(f"{ml2.name}\n{ml2.role}")