

def getDistance(s, h, m):
    distance = s * (h + (m / 60))
    return distance


def getTime(s, d):
    t = d / s
    h = int(t) # 시간 단위는 정수형만 하면 해결
    m = (t-h)*100 * 60 / 100 # 쉽게 생각, 소수점 뒤를 100곱해 분으로 만들어주고 0.6(60분단위) 곱하면됨
    return [h, m]

print('-' * 60)
s = float(input('속도(km/h) 입력 : '))
h = float(input('시간(h) 입력 : '))
m = float(input('시간(m) 입력 : '))
d = getDistance(s,h,m)
print(f'{s}(km/h)속도로 {h}시간 {m}분 동안 이동한 거리 {d:.2f}km')
print('-' * 60)

print('-' * 60)
s = float(input('속도(km/h) 입력 : '))
d = float(input('거리(km) 입력 : '))
t = getTime(s,d)
print(f'{s}(km/h)속도로 {d}km 이동한 시간 : {t[0]}시간 {t[1]:.2f}분 소요')
print('-' * 60)