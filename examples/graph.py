import math
import time

from phalski_ledshim import app, client, chart


def value():
    t = time.time()
    return (math.sin(t) + 1) / 2


if __name__ == '__main__':
    a = app.App()
    a.configure_worker(0.1, chart.Factory.bar_chart_source(a.pixels, value))
    a.exec()
