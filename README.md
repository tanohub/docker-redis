### docker-redis ###

# Services

| Service   | Note |
| :---      | :--- |
| http://localhost:8001 | redis insight web gui 
| | |
| tcp://localhost:6371 ->6379 | redis1 |
| tcp://localhost:6372 ->6379 | redis2 |
| tcp://localhost:6373 ->6379 | redis3 |
| | |
| tcp://localhost:2631 ->26379 | sentinel1 |
| tcp://localhost:2632 ->26379 | sentinel2 |
| tcp://localhost:2633 ->26379 | sentinel3 |

# Gotchas :
- sentinel bind mount, real folder ( data/sentinel/sentinelX should be writable from anyone due to the config rewrite feature )
- insight bind mount, db folder should be writable from anyone

