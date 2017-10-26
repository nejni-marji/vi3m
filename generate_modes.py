#!/usr/bin/env python3
from sys import argv
from os.path import dirname
from config import configs

#
# WARNING! This script does not check for configuration errors!
#

def generate_config(config):
	try:
		p_key = '$mod+%s' % config['mod']
		p_sym = config['mod'].upper()
		binds = config['binds']
	except:
		p_key = config['key']
		p_sym = config['sym']
		binds = config['binds']
	chains = list(binds)
	modes = []

	def getmodes(mode):
		if len(mode) > 1:
			mode = mode[:-1]
			modes.append(mode.lower())
			return getmodes(mode)

	for mode in list(chains):
		getmodes(mode)
	modes = list(set(modes))
	modes.sort()

	def debug():
		print(binds)
		print()
		print(chains)
		print(modes)

	try:
		if argv[1] in ['d', 'debug']:
			debug()
			return None
	except:
		pass

	def gen_prefix_mode():
		print('bindsym %s exec ~/.i3/show_bar.sh; mode "%s-"' % (p_key, p_sym))
		print('mode "%s-" {' % (p_sym))
		print('\tbindsym Return mode "default"')
		print('\tbindsym Escape mode "default"')
		print('\tbindsym %s mode "default"' % (p_key))

		elems = [i for i in chains if len(i) == 1]
		elems.sort()
		for elem in elems:
			key = elem
			if not key == key.lower():
				key = 'Shift+' + key.lower()
			print('\tbindsym %s %s; mode "default"'
				% (key, binds[elem]
			))

		for mode in modes:
			key = mode.lower()
			if len(key) == 1:
				print('\tbindsym %s mode "%s-%s"' % (key, p_sym, mode))
		print('}')
		print()

	def gen_mode(mode):
		elems = [i for i in chains + modes if mode == i[:-1]]
		elems.sort()
		print('mode "%s-%s" {' % (p_sym, mode))
		print('\tbindsym Return mode "default"')
		print('\tbindsym Escape mode "default"')
		print('\tbindsym %s mode "%s-"' % (p_key, p_sym))
		for elem in elems:
			key = elem.replace(mode, '', 1)
			if not key == key.lower():
				key = 'Shift+' + key.lower()
			if not elem in modes:
				print('\tbindsym %s %s; mode "default"'
					% (key, binds[elem]
				))
			else:
				print('\tbindsym %s mode "%s-%s"' % (key, p_sym, elem))
		print('}')
		print()

	gen_prefix_mode()
	for mode in modes:
		gen_mode(mode)

for config in configs:
	generate_config(config)
