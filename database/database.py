from typing import DefaultDict


class User(Base):
   __tablename__ = "users"
   id = Column(Integer, primary_key=True, index=True)
   lname = Column(String)
   fname = Column(String)
   email = Column(String, unique=True, index=True)
   todos = relationship("TODO", back_populates="owner", cascade="all, delete-orphan")

class TODO(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key= True, index=True)
    text = Column(String, index = True)
    Completd = Column(bool, defaul=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = Column("User",back_populates= "todos")

