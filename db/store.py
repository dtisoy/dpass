from schema import Website, Account
from base import Base, engine
from sqlalchemy.orm import Session
from sqlalchemy import select 


if __name__ == "__main__":
    Base.metadata.create_all(engine) 
    
    # create rows

    #session
    with Session(engine) as session:
        google = Website(name="accounts.google.com")
        session.add(google)
        session.commit()

        cuenta = Account(username="tisoy", password="123445", website=google.id)
        session.add(cuenta)
        session.commit()
        stmt1 = select(Account)
        #scalars returns an iterable
        result = session.scalars(stmt1).all()

