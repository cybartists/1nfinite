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
| sex      | int(4)       |         |
| country  | int(4)       |         |

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

sex:

| sex  | int  |
| ---- | ---- |
| 未知 |  0  |
|  男  | 1 |
|  女  | 2 |
|女汉子 | 3 |
|女装大佬| 4 |

country:

| country    | int  |
| ---------- | ---- |
| 霍格沃兹   | 0    |
| 赛博坦     | 1    |
| 瓦坎达     | 2    |
| 新日暮里   | 3    |
| 3栋501     | 4    |
| 卡塞尔     | 5    |
| 召唤师峡谷 | 6    |

## channelLIst

| status | 标注                       |
| ------ | -------------------------- |
| 0      | 获取成功，并且不是最后一页 |
| 1      | 获取失败                   |
| 2      | 获取成功，并且为最后一页   |

