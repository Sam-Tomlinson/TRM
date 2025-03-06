###################
#   INFORMATION   #
###################
# bmk
#
#
#
#
#
###################
#     Imports     #
###################
from rich.console import Console
from ..Database import RecipeDAO


###################
#    FUNCTIONS    #
###################



def main():
    console = Console()
    try:
        db = RecipeDAO("b.db")
        #db = RecipeDAO("database.db")
        
        db.format_database()
    except ValueError as e:
        print("Exception: "+e)
        return -1
    except:
        print("There was some other exception")

    print(db.debug_log())
if __name__ == "__main__":
    main()
