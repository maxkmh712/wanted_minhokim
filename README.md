# [위코드 x 원티드] 백엔드 프리온보딩 선발 과제
## Endpoint
- 회원가입 : `POST` /users/signup
- 로그인 : `POST` /users/signin
- 게시물 작성 : `POST` /posts/post
- 전체 게시물 조회 : `GET` /posts/post
- 특정 게시물 조회 : `GET` /posts/post/<int:post_id>
- 특정 게시물 삭제 : `DELETE` /posts/post/<int:post_id>
- 특정 게시물 수정 : `PUT` /posts/post/<int:post_id>


# Users
## 회원가입 
- `POST` 
- /users/signup
- request
```python
{
	"name" : "김태훈", # 유저 이름
	"email" : "rlaxogns@gmail.com", # 유저 이메일
	"password" : "rlaxogns11!" # 유저 비밀번호
}
```

- response
```json
{
  "MESSAGE": "SUCCESS" # 성공
}
```

```json
{
  "MESSAGE": "KEY_ERROR" # 필수 key값 누락 시
}
```

```json
{
  "MESSAGE": "EMAIL_ALREADY_EXISTS" # 아이디 중복
}
```


```json
{
  "MESSAGE": "INVALID_EMAIL"
}
```

```json
{
  "MESSAGE": "INVALID_PASSWORD" # 비밀번호 조건 미충족
}
```
