t = int(input())

for _ in range(t):
    n,H,M = map(int,input().split())
    sleep_time = (H*60) + M 
    
    min_diff = 24*60 
    
    for i in range(n):
        hi,mi = map(int,input().split())
        alarm_time = (hi*60) + mi

        if alarm_time >= sleep_time:
            diff = alarm_time - sleep_time 
        else:
            diff = (24 * 60 - sleep_time) + alarm_time 
        
        if diff < min_diff:
            min_diff = diff 
        
    ans_h = min_diff//60 
    ans_m = min_diff % 60 

    print(ans_h,ans_m)
        
        