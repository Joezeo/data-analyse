# coding=UTF-8
from matplotlib import pyplot as plt


class DataPlot():
    def plot_data_line(self, x, y, str_data):
        """画数据图：
        画出数据折线图
        """
        y[str_data] = y[str_data].apply(lambda z: int(z))
        data_1 = y
        plt.plot(x, data_1)
        plt.show()

    def plot_data_pie(self, a, b, c,):
        """画数据图：
        画出数据饼状图
        """
        # 将pandas DataFrame每一列转化为int型整数
        a['cnt'] = a['cnt'].apply(lambda x: int(x))
        b['cnt'] = a['cnt'].apply(lambda x: int(x))
        c['cnt'] = a['cnt'].apply(lambda x: int(x))

        # 将三个DataFrame 'cnt'列进行求和
        part_1 = a['cnt'].sum()
        part_2 = b['cnt'].sum()
        part_3 = c['cnt'].sum()

        # 画饼状图所需参数定义
        labels = ['Sunny, less cloudy, partly cloudy',
                'The mist, cloudy ',
                'Rain, snow, cloudy']
        sizes = [part_1, part_2, part_3]
        colors = ['red', 'yellowgreen', 'lightskyblue']
        explode = (0, 0, 0)

        patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels,
                                        colors=colors, labeldistance = 1.1,
                                        autopct = '%3.1f%%', shadow = False,
                                        startangle = 90, pctdistance = 0.6,)
        plt.axis('equal')
        plt.legend()
        plt.show()
