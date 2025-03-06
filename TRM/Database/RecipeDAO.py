import sqlite3

# Stands for Recipe Data Access Object
class RecipeDAO:
    def __init__(self, dBName):
        self.dBName = dBName
        self.con = sqlite3.connect(self.dBName)

        self.debug = []

        self.schemaFile = "schema.sql"
        self.version = 15424 
        
    def format_database(self):   
        """
        If database is empty
        |-Format database
        |-return connector and cursor
        If database is not empty
        |If user version is correct
        | |-return connector and curso
        |Else
        | |-print info
        | |-raise error
        | |-return                    
        INPUT:
            SELF(RecipeDAO)
        OUTPUT:
            VOID
        Exception:
            RunTimeError
        """

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
            raise ValueError("Invalid Version Number: {}, Is {} a TRM database?".format(result, self.dBName))
            self.debug.append("Version number is {}, db probably has a different schema".format(result))
        else:
            self.debug.append("Version number is {}, assuming db is correct".format(result))
        self.cur.close()

    def debug_log(self):
        """
        Returns the debug list for printing and clears all debug logs
        INPUT
            self(RecipeDAO)
        OUTPUT
            res(list[string]): Debug logs
        """
        res = self.debug
        self.debug = []
        return res
