# [위코드 x 원티드] 백엔드 프리온보딩 선발 과제
## Endpoint
1. 회원가입 : `POST` /users/signup
2. 로그인 : `POST` /users/signin
3. 게시물 작성 : `POST` /posts/post
4. 전체 게시물 조회 : `GET` /posts/post
5. 특정 게시물 조회 : `GET` /posts/post/<int:post_id>
6. 특정 게시물 삭제 : `DELETE` /posts/post/<int:post_id>
7. 특정 게시물 수정 : `PUT` /posts/post/<int:post_id>


# Users
## 1. 회원가입 
### Endpoint
- `POST` 
- /users/signup


### request
```json
{
	"name" : "김태훈", 
	"email" : "rlaxogns@gmail.com", 
	"password" : "rlaxogns11!"
}
```

### response
- 성공
```json
{
  "MESSAGE": "SUCCESS"
}
```
- 필수 key값 누락 시
```json
{
  "MESSAGE": "KEY_ERROR"
}
```

- 아이디 중복
```json
{
  "MESSAGE": "EMAIL_ALREADY_EXISTS" 
}
```

- 이메일 조건(@, . 포함) 미충족 
```json
{
  "MESSAGE": "INVALID_EMAIL"
}
```

- 비밀번호 조건(비밀번호 8자리 이상, 소문자, 대문자, 특수문자) 미충족
```json
{
  "MESSAGE": "INVALID_PASSWORD"
}
```


## 2. 로그인
### Endpoint
- `POST` 
- /users/signin

### request
- 로그인하기 위한 이메일과 비밀번호
```json
{
	"email" : "rlaxogns@gmail.com",
	"password" : "rlaxogns11!"
}
```

### response
- 로그인 성공시 토큰 발급
```json
{
  "ACCESS_TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30.8cYBjkeD45vXzEbv9SDyIg-bew6LMqaLQKJ_sKXYU1Y"
}
```

- 필수 key값 누락 시
```json
{
  "MESSAGE": "KEY_ERROR"
}
```

- 비밀번호 틀릴 시
```json
{
  "MESSAGE": "INVALID_PASSWORD"
}
```

- 이메일 틀릴 시
```json
{
  "MESSAGE": "INVALID_EMAIL"
}
```

# Posts
## 3. 게시물 작성
- 로그인을 성공하여 토큰을 받은 유저만 게시물을 작성할 수 있다

### Endpoint
- `POST` 
- /posts/post

### request
- title : 게시물 제목
- content : 게시물 내용

```json
{ "headers" : {
    "Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30.8cYBjkeD45vXzEbv9SDyIg-bew6LMqaLQKJ_sKXYU1Y"
    },
    "body" : {
	"title" : "김태훈님의 첫 번째 게시물!!",
	"content" : "게시물1게시물1게시물1게시물1게시물1"
    }
}
```

### reponse
- 게시물
```json
{
  "MESSAGE": "SUCCESS" 
}
```

-필수 key값 누락 시
```json
{
  "MESSAGE": "KEY_ERROR"
}
```

## 4. 전체 게시물 조회
### Endpoint
- `GET` 
- /posts/post

### response
```json
{
  "MESSAGE": "SUCCESS",
  "POST_LIST": [
    {
      "id": 2,
      "작성자": "김민호",
      "제목": "첫번째 게시물!!",
      "내용": "두번째 프로젝트 반이 지나간다....ㅠ!"
    },
    {
      "id": 3,
      "작성자": "김민호",
      "제목": "두번째 게시물!!",
      "내용": "게시물2게시물2게시물2게시물2게시물2게시물2"
    },
    {
      "id": 4,
      "작성자": "김민호",
      "제목": "세번째 게시물!!",
      "내용": "게시물33333333333333333"
    },
    {
      "id": 5,
      "작성자": "구본욱",
      "제목": "수정된게시물",
      "내용": "수정수정수정"
    },
    {
      "id": 6,
      "작성자": "구본욱",
      "제목": "두번째게시물",
      "내용": "규본욱입니다"
    },
    {
      "id": 7,
      "작성자": "김태훈",
      "제목": "김태훈님의 첫 번째 게시물!!",
      "내용": "게시물1게시물1게시물1게시물1게시물1"
    }
  ]
}
```

### Pagination 적용하여 조회
`http://localhost:8000/posts/post?offset=0&limit=3`

```json
{
  "MESSAGE": "SUCCESS",
  "POST_LIST": [
    {
      "id": 2,
      "작성자": "김민호",
      "제목": "첫번째 게시물!!",
      "내용": "두번째 프로젝트 반이 지나간다....ㅠ!"
    },
    {
      "id": 3,
      "작성자": "김민호",
      "제목": "두번째 게시물!!",
      "내용": "게시물2게시물2게시물2게시물2게시물2게시물2"
    },
    {
      "id": 4,
      "작성자": "김민호",
      "제목": "세번째 게시물!!",
      "내용": "게시물33333333333333333"
    }
  ]
}
```

## 5. 특정 게시물 조회
### Endpoint
- `GET` 
- /posts/post/<int:post_id>

### response
- 해당 아이디 게시물 조회 성공시
```json
{
  "MESSAGE": "SUCCESS",
  "POST_IFNO": [
    {
      "id": 7,
      "작성자": "김태훈",
      "제목": "김태훈님의 첫 번째 게시물!!",
      "내용": "게시물1게시물1게시물1게시물1게시물1"
    }
  ]
}
```

- 존재하지 않는 id값 입력시
```json
{
  "MESSAGE": "POST_DOES_NOT_EXIST"
}
```

## 6. 특정 게시물 삭제
### Endpoint
- `DELETE` 
- /posts/post/<int:post_id>

### request
```json
{ "headers" : {
    "Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30.8cYBjkeD45vXzEbv9SDyIg-bew6LMqaLQKJ_sKXYU1Y"
    }
}
```

### response
- 성공시
```json
{
  "MESSAGE": "SUCCESS"
}
```
- 존재하지 않는 id값 입력시
```json
{
  "MESSAGE": "POST_DOES_NOT_EXIST"
}
```

## 7. 특정 게시물 수정
### Endpoint
- `PUT` 
- /posts/post/<int:post_id>

### request
```json
{ "headers" : {
    "Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30.8cYBjkeD45vXzEbv9SDyIg-bew6LMqaLQKJ_sKXYU1Y"
    },
    "body" : {
	"title" : "김태훈 첫번째 게시물 수정수정수정",
	"content" : "수정수정수정"
	}
}
```

### response
- 성공시
```json
{
  "MESSAGE": "SUCCESS"
}
```

- 존재하지 않는 id값 입력시
```json
{
  "MESSAGE": "POST_DOES_NOT_EXIST"
}
```
