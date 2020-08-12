# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:41:19 2020

@author: xiaobin
"""

import numpy as np

class parking():
    
    def _init_(self):
        self.num_max = 100                                      #停车场最大车位数
        self.car_num = 0                                        #停车场停车数
        self.mark = np.random.rand(1, self.num_max)             #每个车位对应的停车票
        
    def parking(self):
        if(self.car_num < num_max):                                     #停车场不为空，可以停车
            print('停车票是', self.mark(1,self.car_num))
            self.car_num = self.car_num + 1
            return self.mark(1,self.car_num-1)
        else:
            print('停车场已满')
            return -1
            
    def pick_up(self, user_mark):
        for i  in range(self.num_max):
            if(self.mark(1,i) == user_mark):                        #判断停车票是否正确
                print('停车票正确，请取车!')
                self.car_num = self.car_num - 1
                return 0
        print('停车票错误!')
        return -1
            
    def print_spare(self):
        return self.num_max - self.car_num, self.num_max
    
    
class parkingboy():
    
    def _init_(self, park_lot):
        self.car_num = 0
        self.mark_num = {}
        self.park_lot = park_lot
        
    def parking_car(self, park_num):
        park_mark = self.park_lot[park_num].parking()
        self.mark[park_mark] = park_num
        
    def pick_up_car(self, park_mark):
        park_num = self.mark[park_mark]
        self.park_lot[park_num].pick_up(park_mark)
            
        
class smart_parkingboy():
    
    def _init_(self, park_lot):
        self.car_num = 0
        self.mark_num = {}
        self.park_lot = park_lot
        
    def parking_car(self, park_num):
        max_parknum = 0
        max_parkspare = 0
        for i in self.park_lot:
            parkspare, temp = self.park_lot.print_spare()
            if(max_parkspare < parkspare):
                max_parknum = i
                max_parkspare = parkspare
        park_mark = self.park_lot[max_parknum].parking()
        self.mark[park_mark] = park_num
        
    def pick_up_car(self, park_mark):
        park_num = self.mark[park_mark]
        self.park_lot[park_num].pick_up(park_mark)
        
        
class super_parkingboy():
    
    def _init_(self, park_lot):
        self.car_num = 0
        self.mark_num = {}
        self.park_lot = park_lot
        
    def parking_car(self, park_num):
        max_parknum = 0
        max_parkspare = 0
        for i in self.park_lot:
            parkspare, max_num = self.park_lot.print_spare()
            temp = parkspare / max_num
            if(max_parkspare < temp):
                max_parknum = i
                max_parkspare = temp
        park_mark = self.park_lot[max_parknum].parking()
        self.mark[park_mark] = park_num
        
    def pick_up_car(self, park_mark):
        park_num = self.mark[park_mark]
        self.park_lot[park_num].pick_up(park_mark)

        
class parkingmanager():
    
    def _init_(self, park_lot):
        self.car_num = 0
        self.mark_num = {}
        self.park_lot = park_lot
        
    def parking_car(self, park_num):
        max_parknum = 0
        max_parkspare = 0
        for i in self.park_lot:
            parkspare, max_num = self.park_lot.print_spare()
            temp = parkspare / max_num
            if(max_parkspare < temp):
                max_parknum = i
                max_parkspare = temp
        park_mark = self.park_lot[max_parknum].parking()
        self.mark[park_mark] = park_num
        
    def pick_up_car(self, park_mark):
        park_num = self.mark[park_mark]
        self.park_lot[park_num].pick_up(park_mark)
        
    def boy_parking(self, park_num, boy):
        boy.parking_car(park_num)
        
    def boy_pickup(self, park_mark, boy):
        boy.pick_up_car(park_mark)
        
        