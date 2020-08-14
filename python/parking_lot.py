# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:41:19 2020

@author: xiaobin
"""
import numpy as np

'''
需求1
构造一个停车场，停车场可以停车和取车，停车成功后得到停车票。 用户取车的时候也需要提供停车票，停车票有效，才可以成功取到车。
'''
class parking_lot(object):
    
    def __init__(self, max_num, park_name):                     
        self.car_num = 0                                        #停车场停车数
        self.name = park_name                                   #停车场名字
        self.max_num = max_num                                  #停车场最大车位数
        self.ticket_mark = [0] * max_num                        #停车票标记数组
        self.ticket_to_carid = dict()                           #停车票和carid对应
        
    def ticket(self, carid):
        for i in self.ticket_mark:                              
            if i == 0:                                          #找到第一个不为空的停车位，将车位号作为停车票
                self.ticket_to_carid[carid] = i                 #将carid与停车票存储下来
                return i

    def parking(self,carid):
        if (self.max_num - self.car_num):                                     #停车场不为空，可以停车
            ticket_num = self.ticket(carid)                                     #停车，获取停车票
            print('%s 停入 %s,停车票为%d' % (carid, self.name, ticket_num))       
            self.car_num = self.car_num + 1                                     #停车场已停车数量加一
            return ticket_num
        else:                                                                   #停车场满，不能停车
            print('停车场已满')
            return None
            
    def pick_up(self, carid, ticket_num):               
        if self.ticket_to_carid[carid] == ticket_num:                         #匹配停车票，相同取车
            print('停车场：%s；车票号 %s -- 正确；取出车辆：%s' % (self.name, ticket_num, carid))
            self.ticket_to_carid.pop(carid)
            self.ticket_mark[ticket_num] = 0                                    #将停车位置空
            return carid
        else:
            print('停车票错误!')
            return None
    

'''
需求2
构造一个停车小弟（ParkingBoy），他能够将车顺序停放到多个停车场，并可以取出
'''
class parkingboy(object):

    def _init_(self, park_lot):
        self.car_to_parklot = dict()
        self.park_lots = park_lot

    def check(self):
        for park_lot in self.park_lots:
            if park_lot.max_num - park_lot.car_num:
                return park_lot
        return None

    def park(self, cars):
        for car in cars:
            if not self.check():
                print('所有停车场已停满，无法停车！')
                return
            self.car_to_parklot[car] = self.check()
        
    def pickup(self, tickets):
        for car, ticket in tickets:
            park_lot = self.car_to_parklot[car]
            park_lot.pick_up(car, ticket)


'''
需求3
构造一个聪明的停车小弟（Smart Parking Boy），他能够将车停在空车位最多的那个停车场      
'''
class smart_parkingboy(parkingboy):
    
    def check(self):
        remainder = []
        for park_lot in self.park_lots:
            temp = park_lot.max_num - park_lot.car_num
            if temp:
                remainder.append(temp)
        myindex = remainder.index(max(remainder))
        return self.park_lots[myindex]
        

'''
需求4
构造一个超级停车小弟（Super Parking Boy），他能够将车停在空置率最高的那个停车场
'''  
class super_parkingboy(parkingboy):
    
    def check(self):
        remainder = []
        for park_lot in self.park_lots:
            temp = park_lot.max_num - park_lot.car_num
            temp = temp / park_lot.max_num
            if temp:
                remainder.append(temp)
        myindex = remainder.index(max(remainder))
        return self.park_lots[myindex]


'''
需求5
构造停车场的经理（Parking Manager），他要管理多个停车仔，让他们停车，同时也可以自己停车
'''        
class parkingmanager(parkingboy):
    
    def boy_park(self, cars, boy):
        boy.park(cars)
        
    def self_park(self, cars):
        self.park(cars)
'''     
if __name__ == "__main__":
    park_lot = parking_lot(100, 'park_1')
    carid = '豫A88888'
    ticket_num = park_lot.parking(carid)
    park_lot.pick_up(carid, ticket_num)
'''

import unittest
from unittest import TestCase

class TestParkingLot(TestCase):
    def test_park_two_cars_should_get_different_tickets(self):
        park_lot = parking_lot(2, 'park')
        carid = ['豫A88888', '豫A66666']
        t1 = park_lot.parking(carid[0])
        t2 = park_lot.parking(carid[1])
        self.assertNotEquals(t1, t2)

    def test_when_park_car_and_parking_lot_is_full_should_get_exception(self):
        park_lot = parking_lot(1, 'park')
        carid = ['豫A88888', '豫A66666']
        park_lot.parking(carid[0])
        self.assertRaises(Exception, park_lot.parking, carid[1])

    def test_get_car(self):
        park_lot = parking_lot(1, 'park')
        carid = '豫A88888'
        t1 = park_lot.parking(carid)
        taken_car = park_lot.pick_up(carid, t1)
        self.assertEquals(carid, taken_car)

    def test_get_car_with_wrong_ticket_should_get_exception(self):
        park_lot = parking_lot(1, 'park')
        self.assertRaises(Exception, park_lot.pick_up, '停车票错误!')

    def test_get_cars_when_a_car_is_taken_should_get_exception(self):
        park_lot = parking_lot(1, 'park')
        carid = '豫A88888'
        t = park_lot.parking(carid)
        park_lot.pick_up(carid, t)
        self.assertRaises(Exception, park_lot.pick_up, t)

if __name__ == '__main__':
    unittest.main()