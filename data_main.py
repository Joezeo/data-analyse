# coding=UTF-8
import data_base
import data_plot
import pymysql
import matplotlib
from warnings import filterwarnings
filterwarnings('ignore', category = pymysql.Warning)# 关闭pymysql warning提示


class DataMain():
    def __init__(self):
        """初始化：
        建立DataBase对象，DataPlot对象
        """
        self.database = data_base.DataBase()
        self.dataplot = data_plot.DataPlot()

    def start(self):
        """程序主函数：
        用户选择功能
        """
        #  定义列表来存放数据
        data_dteday = data_cnt = data_casual = data_registered = []
        data_wea_1 = data_wea_2 = data_wea_3 = []

        data_dteday, data_cnt, data_casual, data_registered =\
        self.database.get_dataI()

        data_wea_1, data_wea_2, data_wea_3 = self.database.get_dataII()

        while True:
            print('\n\n0.退出程序')
            print('1.查看时间与用户总数的关系')
            print('2.查看时间与注册用户的关系')
            print('3.查看时间与未注册用户的关系')
            print('4.查看天气与用户总数的关系')
            print('5.查看天气与日均用户数的关系')
            cho = int(input('请输入你的选择 -->'))
            if cho == 0:
                break
            if cho == 1:
                self.dataplot.plot_data_line(data_dteday, data_cnt, 'cnt')
            if cho == 2:
                self.dataplot.plot_data_line(data_dteday, data_registered, 'registered')
            if cho == 3:
                self.dataplot.plot_data_line(data_dteday, data_casual, 'casual')
            if cho == 4:
                self.dataplot.plot_data_pie(data_wea_1, data_wea_2, data_wea_3)
            if cho == 5:
                self.dataplot.plot_data_histo(data_wea_1, data_wea_2, data_wea_3)


if __name__ == "__main__":
    datamain = DataMain()
    datamain.start()
