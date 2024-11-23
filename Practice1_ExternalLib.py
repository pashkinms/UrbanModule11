
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class Numbers:
    def __init__(self, x=10, y=10, minimal=-1, maximal=1):
        self.array = np.logspace(minimal, maximal, num=x*y).reshape(x, y)
        self.x = x
        self.y = y

    def make_identy(self):
        return self.array * np.eye(self.x, self.y)

    def make_trian(self):
        return self.array * np.tri(self.x, self.y)

    def recover_array(self):
        self.__init__(self.x, self.y)

    def get_linear(self):
        return self.array.reshape(self.x * self.y)


matplotlib.use('Qt5Agg')

fig, ax = plt.subplots(1, 3)
fig.set_size_inches(19,8)
fig.set_facecolor('#eef')

data = Numbers()

ax[0].plot(data.get_linear(), '-.r')
ax[1].plot(data.make_identy(), 'd', )
ax[2].plot(data.make_trian(), '*')


plt.grid()


plt.show()
