import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import statistics


def get_segmentation(onset, duration, signal, frequency):
	"""
	"""
	signal_list = []

	if onset == 0:
		beg_index = 0
		end_index = int((duration + 1) * frequency) - 1

	else:

		beg_index = int(onset * frequency)  # error
		end_index = int(duration * frequency)

	signal_list = get_segment(beg_index, end_index, signal)

	# return (start (sek), duration (sek))
	return tuple((signal_list, beg_index, end_index))


def mean_val(signal_list):
	"""
	"""
	return sum(signal_list) / len(signal_list)


def std_val(signal_list):
	"""
	"""
	return statistics.stdev(signal_list)


def get_segment(index1, index2, signal):
	"""
	Args:
	index1:
	index2:
	signal:

	"""
	signal_list = []

	for i in range(index2 - index1):
		# while index < len(signal)
		signal_list.append(signal[index1 + i])

	return signal_list
