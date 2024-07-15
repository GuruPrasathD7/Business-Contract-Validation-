from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Signatory(Base):
    __tablename__ = 'signatories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    authority_level = Column(Integer)
    signature_sample = Column(String)


engine = create_engine('sqlite:///contracts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def verify_signatory(signatory_name):
    signatory = session.query(Signatory).filter_by(name=signatory_name).first()
    if signatory:
        return True, signatory.authority_level
    return False, None


def secure_sign_contract(contract, signatory_name):
    is_verified, authority_level = verify_signatory(signatory_name)
    if not is_verified:
        return "Signatory not authorized."

    signed_contract = contract.copy()
    signed_contract["signed_by"] = signatory_name
    signed_contract["authority_level"] = authority_level
    return signed_contract
