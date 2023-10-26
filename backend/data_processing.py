```python
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserPreferences(Base):
    __tablename__ = 'user_preferences'

    id = Column(Integer, primary_key=True)
    reply_styles = Column(Text)
    sign_offs = Column(Text)
    common_phrases = Column(Text)

class EmailChain(Base):
    __tablename__ = 'email_chain'

    id = Column(Integer, primary_key=True)
    email_chain = Column(Text)

class SuggestedReplies(Base):
    __tablename__ = 'suggested_replies'

    id = Column(Integer, primary_key=True)
    suggested_replies = Column(Text)

engine = create_engine('sqlite:///ai_email_assistant.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def save_user_preferences(user_preferences):
    user_pref = UserPreferences(reply_styles=user_preferences['reply_styles'], sign_offs=user_preferences['sign_offs'], common_phrases=user_preferences['common_phrases'])
    session.add(user_pref)
    session.commit()

def save_email_chain(email_chain):
    email_chain_db = EmailChain(email_chain=email_chain)
    session.add(email_chain_db)
    session.commit()

def save_suggested_replies(suggested_replies):
    suggested_replies_db = SuggestedReplies(suggested_replies=suggested_replies)
    session.add(suggested_replies_db)
    session.commit()

def get_user_preferences():
    return session.query(UserPreferences).all()

def get_email_chain():
    return session.query(EmailChain).all()

def get_suggested_replies():
    return session.query(SuggestedReplies).all()
```