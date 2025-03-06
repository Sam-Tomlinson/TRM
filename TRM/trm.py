#################
#  INFORMATION  #
#################
# `T -> Top (Here)
# `M -> Main function
# `F -> Functions
#
#
#
#
#################
#    IMPORTS    #
#################
import sqlite3
from os import path
#################
#   Functions   #
#################

#############
# Database  #
# Functions #
#############
def getDatabase():
    """
    |Get Database name
    |If database file does not exist
    | |-Create and format using dBName
    | |-return connector and cursor
    |If database file exists
    | |If database is empty
    | | |-Format database
    | | |-return connector and cursor
    | |If database is not empty
    | | |If user version is correct
    | | | |-return connector and curso
    | | |Else
    | | | |-print info
    | | | |-raise error
    | | | |-return                    
    """
    name = getDatabaseName()
    if path.exists(name):
        print("database exists")
    else:
        print("database does not exist")




def getDatabaseName():
	"""
    Get database name string. Requires $name end in ".db".  Asks for confirmation 
    INPUT:
       NONE 
    OUTPUT:
        $name(string): string that ends in .db
	"""
	name = input("Input new or existing database name: ")
	while True:
		if name[-3::] == ".db":
			print("Using {}\nNOTE:Please confirm this is a new or TRM database\nTRM may destroy functionality of a non TRM database".format(name))
			if input("confirm(y/n)") == 'y':
				return name
		name = input("Invalid File Extension, make sure you are entering a file name of the form \".*\\.db\"")
	
def db_is_empty(cur):
	"""
	Checks if the database is empty
	INPUT:
		cur(sqlite3.Cursor): database cursor
	OUTPUT:
		res(boolean): empty flag
	RESULT:
		res will be true if database is empty ie sqlite_master table has no entries in table
	"""
	cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
	result = cur.fetchall()
	if len(result) == 0:
		return False
	return True

#
# 
#

def main():
	# Get User's database, new or existing
    getDatabase()


if __name__ == "__main__":
	main()
