import data_base
import data_plot


class DataMain():
    def __init__(self):
        self.database = data_base.DataBase()
        self.dataplot = data_plot.DataPlot()

    def start(self):
        data_dteday = data_cnt = data_casual = data_registered = []
        data_dteday, data_cnt, data_casual, data_registered =\
        self.database.pandas_connect()
        while True:
            print('\n\n0.退出程序')
            print('1.查看时间与用户总数的关系')
            print('2.查看时间与注册用户的关系')
            print('3.查看时间与未注册用户的关系')
            cho = int(input('请输入你的选择 -->'))
            if cho == 0:
                break    
            if cho == 1:
                self.dataplot.plot_data(data_dteday, data_cnt)
            if cho == 2:
                self.dataplot.plot_data(data_dteday, data_registered)
            if cho == 3:
                self.dataplot.plot_data(data_dteday, data_casual)


if __name__ == "__main__":
    datamain = DataMain()
    datamain.start()
