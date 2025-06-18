CREATE TABLE IF NOT EXISTS Recipe(
                recipeID INTEGER PRIMARY KEY AUTOINCREMENT,
                recipeName STRING NOT NULL,
                recipePrepTime FLOAT,
                recipeCookTime FLOAT,
                recipeCreationDate STRING
                );
CREATE TABLE IF NOT EXISTS Ingredient(
                ingredientID INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredientName STRING NOT NULL
                );
CREATE TABLE IF NOT EXISTS Step(
               stepID INTEGER PRIMARY KEY AUTOINCREMENT,
               stepInstructions STRING NOT NULL
                );
CREATE TABLE IF NOT EXISTS Unit(
                unitID INTEGER PRIMARY KEY AUTOINCREMENT,
                unitName STRING NOT NULL
                );
CREATE TABLE IF NOT EXISTS Tag(
                tagID INTEGER PRIMARY KEY AUTOINCREMENT,
                tagName STRING NOT NULL
                );
CREATE TABLE IF NOT EXISTS RecipeIngredient(
               RecIngID INTEGER PRIMARY KEY AUTOINCREMENT,
               recID INTEGER REFERENCES Recipe(recipeID),
               ingID INTEGER REFERENCES Ingredient(ingredientID),
               unitID INTEGER REFERENCES Unit(unitID),
               unitAmount FLOAT NOT NULL    
               );
CREATE TABLE IF NOT EXISTS RecipeStep(
               RecStepID INTEGER PRIMARY KEY AUTOINCREMENT,
               recID INTEGER REFERENCES Recipe(recipeID),
               stepID INTEGER REFERENCES Step(stepID),
               stepNumber INTEGER NOT NULL
               );
CREATE TABLE IF NOT EXISTS RecipeTag(
               RecTag INTEGER PRIMARY KEY AUTOINCREMENT,
               recID INTEGER REFERENCES Recipe(recipeID),
               tagID INTEGER REFERENCES Tag(tagID)
               );
PRAGMA user_version = 15424;

