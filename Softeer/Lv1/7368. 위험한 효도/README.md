# 위험한 효도

[문제 링크](https://softeer.ai/practice/7368)

---

## 문제 분석 및 알고리즘 설계

d = 100,000 이라서 시뮬레이션으로 while 문 돌림

```python
# 터치 전
while 1:
    if move + a >= d:
        time += (d - move)
        move = d
        break
```

여기서 time을 먼저 업데이트 하고, move를 업데이트 해야 남은 거리만큼 이동할 수 있음
