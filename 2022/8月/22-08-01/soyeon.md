책 신청

- [x]  수강신청
- [x]  도메인 설계 완료
- [ ]  빌드 성공
- [x]  amazons3에러 해결 → 일단 지워버림
- [x]  access key 삭제

## @JoinColumn

- ex) @JoinColumn(name=”member_id”, referencedColumnName = “member_id”)
    - name
        - 매핑할 외래 키 이름
        - 외래키 칼럼명을 `만들어주는` 설정
    - referencedColumnName
        - 외래키가 참조하는 `대상 테이블의 컬럼명`