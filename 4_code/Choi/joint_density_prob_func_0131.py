
#!/usr/bin/env python
# coding: utf-8

import sys
import os

import numpy as np
import pandas as pd

# 결합확률밀도함수를 데이터프레임 형태로 출력하는 클래스
class Joint_Probability_Density_df(object):
        def __init__(self, x, y, z, s):
            self.x = x
            self.y = y
            self.z = z
            self.s = s
        
        # factorial function
        def factorial(self, n):
            num = 1
            n = int(n)
            for _n in range(1, n+1):
                num = _n*num
            return num
        
        # combination calculator
        def comb_calc(self, n,r):
            n,r = int(n), int(r)
            return self.factorial(n)/(self.factorial(n-r)*self.factorial(r))
        
        # joint probability density function calculator
        def jpdf_calc(self, x, y, z, s, _x, _y):
            x,y,z,s = int(x), int(y), int(z), int(s)
            
            # combination 시 두 변수와 영역의 차이가 0 이하인 경우는 0처리
            if (s-_x-_y) >= 0:
                out = self.comb_calc(x, _x)*self.comb_calc(y, _y)*self.comb_calc(z,(s-_x-_y))/self.comb_calc(x+y+z,s)
            else: 
                out = 0
        
            return out
        
        # generate to dataframe
        def gen_df(self):
            
            col, row = int(x)+1, int(y)+1
            
            # gen dataframe
            _df = pd.DataFrame(np.zeros(shape=(row, col)))

            # joint probability density function
            for idx, row in _df.iterrows():
                for _r_idx in range(len(row)):
                    _df.loc[idx, _r_idx] = self.jpdf_calc(x,y,z,s,_r_idx, idx)

            return _df
            
def main(x,y,z,s):
    gen_jpd_df = Joint_Probability_Density_df(x,y,z,s)
    df = gen_jpd_df.gen_df()
    print(df)
    return df
    
            
if __name__ == '__main__':
    # 사용법 
    # 문제 예시 교재 p.40 예 2.5
    # 터미널에서 python3 파일명.py 3,2,4,3
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]
    s = sys.argv[4]
    
    main(x,y,z,s)
