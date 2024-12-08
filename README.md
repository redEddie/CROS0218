# CROS0218
로봇운영체제 실습

목표 : 토픽, 서비스, 액션 모두 사용하기

서비스 : `voice_command`, `voice_interaction`, `emergency`

---

# 실행
## Service
### `voice_command`
```
ros2 run voice_command dog_response_server
```
```
ros2 run voice_command voice_command_client {sit, stand, walk}
```


### `voice_interaction`
```
ros2 run voice_interaction dog_behavior_server
```
```
ros2 run voice_interaction interaction_client {play, treat, pat}
```


# YT
### `voice_command` and `voice_interaction`
https://youtu.be/XCqsedKEtdc

### `emergency`
https://youtu.be/YTqCcXQBMKQ

### `navigation`
https://youtu.be/HOMziVH-KMY
