import math

#시간이 1씩 늘어나면 안되나보다 
#

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        # position과 speed를 리스트로 묶고, position 순서대로 정렬하자.
        cars = [[x,y] for x,y in zip(position, speed)]
        cars.sort(key = lambda x: x[0], reverse=True)
        j = 0 
        while cars != []:
            # (선두의 차가 target까지 남은 거리 가는 시간) 동안만큼의 모든 차의 이동 거리
            # speed/time을  position에 더해주고 
            time = (target - cars[0][0]) / cars[0][1]
            
            for i in range(len(cars)):
                cars[i][0] += time * cars[i][1]
            del cars[0]
            left = target 
            for car in cars:
                #앞의 차(left)보다 크거나 같으면 cars에서 제외  
                if car[0] >= left :
                    car[1] = -1
                else:
                    left = car[0]            
            fleet += 1 
            cars = [x for x in cars if x[1] > 0]
           
        return fleet