# 데이터 조작 쿼리 모듈 (DML.py)
    SELECT, INSERT, UPDATE, DELETE

        select_one: 단일행 검색
        select_all: 복수행 검색
        count: 쿼리에 대한 사이즈를 구함
        insert: 테이블에 데이터 입력 (INSERT INTO로 데이터를 집어 넣으나 추후 INSERT IGNORE나, INSERT   INTO ~ ON DUPLICATE KEY UPDATE로 처리하는 방법도 있음
        update: 테이블에 존재하는 데이터 업데이트 기능 수행

# 데이터 정의 쿼리 모듈 (DDL.py)
    CREATE
    ALTER
    DROP
    RENAME
    TRUNCATE

# 데이터 제어 쿼리 모듈 (DCL)
    GRANT
    REVOKE

# 트랜잭션 제어 쿼리 모듈 (TCL)
    COMMIT
    ROLLBACK
    SAVEPOINT