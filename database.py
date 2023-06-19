from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터 베이스 설정

# 데이터 베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# 데이터 베이스 에 접속 하기 위해 필요한 클래스
# autocommit=False --> 데이터 를 변경 했을 때 commit 이라는 사인을 줘야만 실제 저장이 된다. (rollback 가능)
# autocommit=True --> commit 사인이 없어도 즉시 데이터 베이스 에 변경 사항이 적용 된다. (rollback 불가능)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base() --> 함수에 의해 반환된 Base 클래스 는 데이터 베이스 모델을 구성할 때 사용 되는 클래스 이다.
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
