
# Copyright (C) 2006-2024 The Analog System Compiler project

# This file was automatically generated by the ASysC compiler. Don't modify it.


import math
import circuit_base
from circuit_base import circuit_base, element

class circuit( circuit_base ):

	def __init__(self):
		super().__init__()
		self.R2_U = element('R2_U')
		self.D1_U = element('D1_U')
		self.D1_I = element('D1_I')
		self.V_I = element('V_I')
		self.R2_I = element('R2_I')
		self.V_U = element('V_U')

	def step(self):
		self._setc(self.R2_U, (((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026-1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1))/((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1))
		self._setc(self.D1_U, -((1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1)+5*math.sin(23687.0505626*self._time()))/(1+(1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026)))
		self._setc(self.D1_I, (1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1)-((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026)/((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1))
		self._setc(self.V_I, (1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1)-((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026)/(1+(1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026))
		self._setc(self.R2_I, (((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026-1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1))/(1+(1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026))
		self._setc(self.V_U, (((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1)*(5*math.sin(23687.0505626*self._time())))/((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1))

