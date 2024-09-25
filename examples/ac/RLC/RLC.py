
# Copyright (C) 2006-2024 The Analog System Compiler project

# This file was automatically generated by the ASysC compiler. Don't modify it.


import math
import circuit_base
from circuit_base import circuit_base, element

class circuit( circuit_base ):

	def __init__(self):
		super().__init__()
		self.C_U = element('C_U')
		self.V_I = element('V_I')
		self.V_U = element('V_U')
		self.R_U = element('R_U')
		self.R_I = element('R_I')
		self.L_U = element('L_U')
		self.L_I = element('L_I')
		self.C_I = element('C_I')

	def step(self):
		self._setf(self.C_U, -(1/((0.001*self.s+1)+1e-08*self.s**2)), self.freq)
		self._setf(self.V_I, -((1e-05*self.s)/((0.001*self.s+1)+1e-08*self.s**2)), self.freq)
		self._setf(self.V_U, ((1e-08*self.s**2+0.001*self.s)+1)/((1e-08*self.s**2+0.001*self.s)+1), self.freq)
		self._setf(self.R_U, -((0.001*self.s)/((0.001*self.s+1)+1e-08*self.s**2)), self.freq)
		self._setf(self.R_I, -((1e-05*self.s)/((0.001*self.s+1e-08*self.s**2)+1)), self.freq)
		self._setf(self.L_U, -((1e-08*self.s**2)/((1e-08*self.s**2+1)+0.001*self.s)), self.freq)
		self._setf(self.L_I, -((1e-05*self.s)/((1+1e-08*self.s**2)+0.001*self.s)), self.freq)
		self._setf(self.C_I, -((1e-05*self.s)/((0.001*self.s+1)+1e-08*self.s**2)), self.freq)

