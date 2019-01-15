数据库帐号：root  
数据库密码：LfB9yOqj#ma&



# 数据库

User:

| key      | type         | comment |
| -------- | ------------ | ------- |
| id       | int          |         |
| username | varchar(255) |         |
| nickname | varchar(255) |         |
| admin    | tinyint      |         |
| ban      | tinyint      |         |
| email    | varchar(255) |         |
| password | varchar(255) |         |

Channel:

| key     | type | comment |
| ------- | ---- | ------- |
| id      | int  |         |
| user_id | int  | fk      |
| content | text |         |

Topic:

| key     | type | comment |
| ------- | ---- | ------- |
| id      | int  |         |
| user_id | int  | fk      |
| title   | text |         |
| sum     | text |         |

image:

| key  | type | comment |
| ---- | ---- | ------- |
| id   | int  |         |
| url  | text |         |

Topic_artical:

| key      | type | comment |
| -------- | ---- | ------- |
| id       | int  |         |
| Topic_id | int  | fk      |
| title    | text |         |
| content  | text |         |
| sum      | text |         |

