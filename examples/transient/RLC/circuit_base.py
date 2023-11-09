# import math
import numpy as np

class element:

    element_list = []

    def __init__(self, name):
        self.name = name
        element.element_list.append(self)
        self.history_x = []
        self.history_y = []
        self.dydx = 2.0 / 1e-9
        self.dy = 0
        self.dydx_prev = 0
        self.dy_prev = 0
        self.value_y = 0.0
        self.value_yc = 0.0

    def set_t(self, val):
        if self.history_y:
            if abs( val ) > ( 3 * abs(self.history_y[-1]) + 10e-6 ):                
                self.value_y = 3 * self.history_y[-1] + 10e-6 
            else:
                self.value_y = val
        else:
            self.value_y = val

    def set_f(self, val, f):
        self.history_x.append(f)
        self.history_y.append(val)

    def _step_t(t):
        for e in element.element_list:            
            if e.history_x:
                delta_t = t - e.history_x[-1]
                e.dydx = 2.0 / delta_t
                e.dy = -(e.dydx * e.value_y + e.dydx_prev * e.value_y + e.dy_prev)
            e.dydx_prev = e.dydx
            e.dy_prev = e.dy
            e.history_x.append(t)
            e.history_y.append(e.value_y)

    def _step_c():
        for e in element.element_list:                        
            e.value_y = e.value_yc

class circuit_base:

    def __init__(self):
        self.timeval = 0.0
        self.delta_timeval = 0.0

    # def delta_time(self):
    #     return self.delta_timeval

    def time(self):
        return self.timeval

    def _delay(self, element_arg, delay_arg):
        return np.interp(
            self.timeval - delay_arg, element_arg.history_x, element_arg.history_y
        )

    def _getv(self, element_arg):
        return element_arg.value_y
    
    def _last(self, element_arg):
        return element_arg.value_yc
    
    def _der0(self, element_arg):
        return element_arg.dy

    def _der1(self, element_arg):
        return element_arg.dydx
    
    def _setc(self, element_arg, val):
        element_arg.value_yc = val * 0.01 + element_arg.value_yc * 0.99
        
    def simulate_t(self, duration, nb):
        self.delta_timeval = duration / nb
        for i in range(0, nb):
            for conv in range(100):
                self.step()
                element._step_c()
            element._step_t(self.timeval)
            self.timeval += self.delta_timeval
            print("Iteration nb {}".format(i), end="\r")

    def simulate_f(self, start, end, nb):
        log_end = np.log10(2 * np.pi * end)
        for i in range(0, nb):
            self.freq = start * 10 ** ((i * log_end) / nb)
            self.s = 2j * np.pi * self.freq          
            print("Iteration nb {}".format(i), end="\r")