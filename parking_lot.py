# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:41:19 2020

@author: xiaobin
"""

import numpy as np

class parking():
    
    def _init_(self):
        self.num_max = 100                                      #停车场最大车位数
        self.spare = self.num_max                               #停车场剩余车位数
        self.mark = np.random.rand(1, self.num_max)             #每个车位对应的停车票
        
    def parking(self):
        if(self.spare > 0):                                     #停车场不为空，可以停车
            print('停车票是', self.mark(1,self.spare-1))
            print('停车位置为', self.spare - 1)
            self.spare = self.spare - 1
            return self.mark(1,self.spare-1), self.spare - 1
        else:
            print('停车场已满')
            return -1
            
    def pick_up(self, i, user_mark):
        if(self.mark(1,i-1) == user_mark):                        #判断停车票是否正确
            print('停车票正确，请取车!')
            self.spare = self.spare + 1
            return 0
        else:
            print('停车票错误!')
            return -1
            
    def print_spare(self):
        return self.spare
    
class parkingboy():
    
    def _init_(self, park_lot):
        self.car_num = 0
        self.mark = {}
        self.park_lot = park_lot
        
    def parking(self, num):
        for i in range(num):
            park_mark, park_spare = {self.park_lot.parking()}
            self.mark
            
        
        

        
        
        
        
        