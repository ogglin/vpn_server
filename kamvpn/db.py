# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
#
# def init_db():
#     # Здесь нужно импортировать все модули, где могут быть определены модели,
#     # которые необходимым образом могут зарегистрироваться в метаданных.
#     # В противном случае их нужно будет импортировать до вызова init_db()
#     import kamvpn.models
#     Base.metadata.create_all(bind=engine)

