# coding=UTF-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas


class DataBase():
    def __init__(self):
        try:
            self.engine = create_engine('mysql+pymysql://root:funkey2012@\
localhost:3306/database')
            self.DBSession = sessionmaker(bind=self.engine)
            self.session = self.DBSession()
            print('连接数据库成功')
        except Exception:
            print('连接数据库失败')

    def get_dataI(self):
        try:
            data_dteday = pandas.read_sql(
                                        'SELECT dteday FROM day',
                                        con=self.engine
                                        )
            data_cnt = pandas.read_sql(
                                        'SELECT cnt FROM day',
                                        con=self.engine
                                        )
            data_casual = pandas.read_sql(
                                        'SELECT casual FROM day',
                                        con=self.engine
                                        )
            data_registered = pandas.read_sql(
                                        'SELECT registered FROM day',
                                        con=self.engine
                                        )
            print('获取时间相关数据成功')
            return (data_dteday, data_cnt, data_casual, data_registered)
        except Exception:
            print('获取时间相关数据失败')

    def get_dataII(self):
        try:
            data_wea_1 = pandas.read_sql(
                                        'SELECT cnt FROM day WHERE \
                                        weathersit = 1',
                                        con=self.engine
                                        )
            data_wea_2 = pandas.read_sql(
                                        'SELECT cnt FROM day WHERE \
                                        weathersit = 2',
                                        con=self.engine
                                        )
            data_wea_3 = pandas.read_sql(
                                        'SELECT cnt FROM day WHERE \
                                        weathersit = 3',
                                        con=self.engine
                                        )
            print('获取天气相关数据成功')
            return (data_wea_1, data_wea_2, data_wea_3,)
        except Exception:
            print('获取天气相关数据失败')
