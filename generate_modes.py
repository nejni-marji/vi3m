#!/usr/bin/env python3
from sys import argv
from config import configs

#
# WARNING! This script does not check for configuration errors!
#

def generate_config(config):
	try:
		p_key = '$mod+%s' % config['mod']
		p_sym = config['mod'][0].upper()
	except:
		p_key = config['key']
		p_sym = config['sym']
	binds = config['binds']

	chains = list(binds)
	modes = []

	def get_modes(chain):
		if len(chain) > 1:
			chain = chain[:-1]
			modes.append(chain.lower())
			return get_modes(chain)

	for chain in chains:
		get_modes(chain)

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
		print('bindsym %s mode "%s-"' % (p_key, p_sym))
		print('mode "%s-" {' % (p_sym))
		print('\tbindsym Return mode "default"')
		print('\tbindsym Escape mode "default"')
		print('\tbindsym %s mode "default"' % (p_key))
		print('\tbindsym BackSpace mode "default"')

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
		print('\tbindsym %s mode "default"' % (p_key))
		print('\tbindsym BackSpace mode "%s-%s"' % (p_sym, mode[:-1]))
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
