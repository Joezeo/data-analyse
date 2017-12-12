# coding=UTF-8
from matplotlib import pyplot as plt


class DataPlot():
    def plot_data_line(self, x, y,):
        plt.plot(x, y)
        plt.show()

    def plot_data_pie(self, a, b, c,):
        a['cnt'] = a['cnt'].apply(lambda x: int(x))
        b['cnt'] = a['cnt'].apply(lambda x: int(x))
        c['cnt'] = a['cnt'].apply(lambda x: int(x))
        part_1 = a['cnt'].sum()
        part_2 = b['cnt'].sum()
        part_3 = c['cnt'].sum()
        # type(np.float32(0).item(part_1))
        # type(np.float32(0).item(part_2))
        # type(np.float32(0).item(part_3))
        print('求和成功', part_1)
        labels = [u'weather 1', u'weather 2', u'weather 3']
        sizes = [part_1, part_2, part_3]
        colors = ['red', 'yellowgreen', 'lightskyblue']
        explode = (0, 0, 0)

        patches, l_text, p_text = plt.pie(sizes, explode=explode,labels=labels,
                                        colors=colors, labeldistance = 1.1,
                                        autopct = '%3.1f%%', shadow = False,
                                        startangle = 90, pctdistance = 0.6,)
        plt.axis('equal')
        plt.legend()
        plt.show()
