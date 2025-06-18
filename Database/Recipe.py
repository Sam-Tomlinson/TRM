class Recipe:
    """A recipe that includes basic information, steps, ingredient?s, tags"""
    def __init__(self)):
        self.name = ''
        self.prepTime = 0
        self.cookTime = 0
        self.creationDate = "1/1/2000"
        self.ingredients = []
        self.units = []
        self.amounts = []
        self.steps = []
        self.tags = []
    def set_name(self, name):
       """sets name"""
       self.name = name
    def set_prep(self,time):
        self.prepTime = time
    def set_cook(self,time):
        self.cookTime = time
    def set_date(self,date):
        self.creationDate = date
    def set_ingredients(self,ingredients):
        self.ingredients = ingredients
    def set_units(self,units):
        self.units =  units
    def set_amounts(self,amounts):
        self.amounts = amounts
    def set_steps(self,steps):
        self.steps = steps
    def set_tags(self,tags):
        self.tags = tags
    def check_recipe(self):
        """Checks for non empty name ingredients,units, amounts, and steps.  Additionslly checks to make sure the ingredients units and amounts have the same length. Does not check for tags since you may intentionally not have any tags.
        Returns a boolean value.  1 means recipe is bad"""
        check_name = not self.name
        if not self.ingredients and not self.units and not self.amounts:
            check_ingredients = len(self.ingredients) == len(self.units) and len(self.ingredients) == len(self.amounts)
        check_steps = not self.steps

        return check_name and check_ingredients and check_steps
        
