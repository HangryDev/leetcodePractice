​       
3 mins to nail approach. coded 27 mins. changed approach midst. 
        #1 strs의 각 words를 sort한다. 
        #2 1의 dict를 key로, value를 word로 하는 bigdict에 넣는다. { ["bat"]}
        #3 strs에 대해 1-2 반복 
        #4 bigDict의 value를 리스트로 출력한다. 
        #o(n)  <- 여기까지 떠올리는데 3분걸림. 
        
        
        #첫 접근 : key를 {{b:1, a:1, t:1} : "bat"} 이렇게 하려고 했음. 
        #python에서 key가 dict인 nested dictionary가 가능한가? 일단 모르겠어서 우회함
        #수정 접근: key를 수정. word를 char순서대로 sort한 다음 그걸 키로 사용함. 
        
        # 막힌 부분 1: key를 dict로 nest 할 수 있는가? 
        # 막힌 부분 2: dict value로 list를 추가/update하는 방법. 
        # 막힌 부분 3: string을 sort하는 방법. 
