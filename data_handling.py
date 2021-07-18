from data_structure import DataStruct
from gsheet import Gspread
import datetime as dt
from flask import request


class DataHandler:
    def __init__(self):
        self.data_base = []
        self.master_data_set = []
        self.data_set = []
        self.sheet = Gspread()
        self.main_data = self.sheet.main_data
        self.response = None
        self.today = dt.datetime.today().strftime("%d/%m/%Y")

    def structure_data(self):
        self.response = None
        self.data_base = []
        self.sheet.sort_alpha()
        self.sheet.get_records()
        for data in self.main_data:
            date = data['Date']
            month = data['Month']
            name = data['WebinarName']
            reg = data['Region']
            room = data['Room']
            start_time = data['StartTime']
            end_time = data['EndTime']
            year = dt.datetime.strptime(date, "%d/%m/%Y").strftime('%Y')
            data_obj = DataStruct(date, month, name, reg, room, start_time,
                                  end_time, year)
            self.data_base.append(data_obj)
        print("passed object allocation")

    def search_day(self):
        self.structure_data()
        item_index = -1
        self.response = None
        self.data_set = []
        self.master_data_set = []
        self.today = dt.datetime.today().strftime("%d/%m/%Y")

        for data in self.data_base:
            if data.date == self.today:
                item = {
                    "date": data.date,
                    "month": data.month,
                    "name": data.name,
                    "reg": data.reg,
                    "room": data.room,
                    "start_time": data.start_time,
                    "end_time": data.end_time
                }
                self.data_set.append(item)
                item_index += 1
                if (item_index+1) % 12 == 0:
                    self.master_data_set.append(self.data_set)
                    self.data_set = []

