class Pokemon:
    def __init__(self, name, height, weight, poketype, color):
        self.name = name
        self.height = height
        self.weight = weight
        self.poketype = poketype
        self.color = color
        self.poketype_revealed = False
        self.color_revealed = False

    def check_guess(self, other):
        return self.name == other.name
    
    def is_taller_than(self, other):
        return self.height > other.height
    
    def is_heavier_than(self, other):
        return self.weight > other.weight
    
    def have_same_type(self, other):
        return self.poketype == other.poketype
    
    def reveal_type(self, other):
        self.poketype_revealed = True
        print(f"I'm not {other.name}, but have the same pokemon type...\nYou're getting closer!!")

    def have_same_color(self, other):
        return self.color == other.color
    
    def reveal_color(self, other):
        self.color_revealed = True
        print(f"Me and {other.name} have the same color... I'd say we are kinda {self.color}")
