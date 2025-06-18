import sqlite3

class DAO:
    """Data Access Object, used to interact with the Thyme Database"""
    def __init__(self, dbName):
        """Attempts to open database of name dbName and adds some basic data"""
        self.dbName = dbName    # Name of Database
        self.debug=[]           # Creates empty debug array
        self.schemaFile = "schema.sql"   # Set the schema for formatting the database
        self.version = 15424   # Database version, hopefully implemented for compatibility issues
        
        # Protect against bad connections
        try:
            self.con = sqlite3.connect(self.dbName)
        except Exception as e:
            print("Exception occured as: {}".format(e))
            self.debug.append("Error: {}".format(e))

        
    def format_database(self):
        """Formats connected database self.dbName"""
        self.cur = self.con.cursor()
        # Check if the database is empty
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = self.cur.fetchall()
        self.debug.append("Fetching tables from sqlite_master:")
        self.debug.append(result)
        if len(result) == 0:
            # Format using schema.sql
            with open(self.schemaFile, 'r') as f:
                schema = f.read()
            self.cur.executescript(schema)
            self.con.commit()
            self.debug.append("Database was empty, Formated using version {} from {}".format(self.version, self.schemaFile))
        # Check for user version
        self.cur.execute("PRAGMA user_version;") 
        result = self.cur.fetchall()[0][0]
        if result != self.version:
            raise ValueError("Invalid Version Number: {}, Is {} a TRM database?".format(result, self.dbName))
            self.debug.append("Version number is {}, db probably has a different schema".format(result))
        else:
            self.debug.append("Version number is {}, assuming db is correct".format(result))
        self.cur.close()

    def get_debug(self):
        """Flushes self.debug"""
        return self.debug

    def insert_recipe(self, recipe):
        """Insert Recipe, checks if the recipe is successful or not"""
    def query_ingredients(self):
        """Returns a list of all defined ingredients.  As a design note, ingredients should NOT BE CASE SENSITIVE"""
        c = self.con.cursor()
        res = c.execute("SELECT * FROM Ingredient").fetchall() # Doing the fetch all to get string
        c.close()
        return res
    def query_units(self):
        """Querries from database all units"""
        c = self.con.cursor()
        res = c.execute("SELECT * FROM Unit").fetchall() # Doing the fetch all to get string
        c.close()
        return res
    def query_tags(self):
        """Queries from database all tags + their id"""
        c = self.con.cursor()
        res = c.execute("SELECT * FROM Unit").fetchall() # Doing the fetch all to get string
        c.close()
        return res
    def insert_ingredients(self, ingredients):
        """
        INPUT: ingredients -> list(str)
        1.) Check if all ingredients are of type string
        2.) Query all ingredients already defined
        3.) Use case insensitive matching to find any unique ingredients
        4.) Insert all (if any) unique ingredietns into ingredient table

        OUTPUT: success-> boolean
                 True for success
                 False for failure (mainly non string ingredient
        """
        if not all(isinstance(item,str) for item in ingredients):
            self.debug.append("ERROR: Ingredient not a string")
            return False # Something wasn't a string
        # Get all ingredients
        ingredientList  = self.query_ingredients()
        # Lowercase both sets of ingredients
        ingredientList = list(map(str.lower,ingredientList))
        ingredients = list(map(str.lower,ingredients))
        # find the difference between the ingredients and ingredientList
        toAdd = list(set(ingredients) - set(ingredientList))
        # Put all strings into the 
