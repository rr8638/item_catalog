from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup_RR import Company, Base, BoardGame

engine = create_engine('sqlite:///gamemenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

company1 = Company(name = "Alderac Entertainment Group (AEG)")
session.add(company1)
session.commit()

company2 = Company(name = "Stonemaier")
session.add(company2)
session.commit()

company3 = Company(name = "Hasbro")
session.add(company3)
session.commit()

game1 = BoardGame(name = "Thunderstone",
num_of_players = "1 to 5",
play_time = "60 min",
cost = "126.74",
rating = "7 out of 10",
description = "Thunderstone is a fantasy deck building card game much in the style of Dominion.",
boardGameCompany = company1
)
session.add(game1)
session.commit()

game2 = BoardGame(name= "Love Letter",
num_of_players = "2-4",
play_time = "20 min",
cost = "$11.04",
rating = "7.3 out of 10",
description = "Love Letter is a game of risk, deduction, and luck for 2 to 4 players. Your goal is to get your love letter into Princess Annettes hands while deflecting the letters from competing suitors.",
boardGameCompany = company1
)
session.add(game2)
session.commit()

game3 = BoardGame(name = "Candy Land",
num_of_players = "2-4",
play_time = "15-21 min",
cost = "$12.99",
rating = "8.4 out of 10",
description = "Candy Land (also Candyland) is a simple racing board game currently published by Hasbro. The game requires no reading and minimal counting skills, making it suitable for young children. Due to the design of the game, there is no strategy involved: players are never required to make choices, just follow directions.",
boardGameCompany = company3
)
session.add(game3)
session.commit()
