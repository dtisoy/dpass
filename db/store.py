from schema import Website, Account
from base import Base, session, engine


if __name__ == "__main__":
    Base.metadata.create_all(engine) 
