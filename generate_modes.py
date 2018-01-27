#!/usr/bin/env python3
from sys import argv
from config import configs

def validate_config(config):
	binds = config['binds']

	chains = list(binds)
	modes = []
	errors = []

	def get_modes(chain):
		if len(chain) > 1:
			chain = chain[:-1]
			modes.append(chain)
			return get_modes(chain)

	for chain in chains:
		mode = chain[:-1]
		if not chain.isalnum():
			errors.append([1, chain])
		if not mode == mode.lower():
			errors.append([2, chain])
		get_modes(chain)

	modes = list(set(modes))
	modes.sort()

	overlap = list(set(chains) & set(modes))
	if overlap:
		errors.append([3, overlap])

	def debug():
		print(binds)
		print()
		print(chains)
		print(modes)

	try:
		if argv[1] in ['d', 'debug']:
			debug()
			exit()
	except:
		pass

	if errors:
		handle_errors(errors)
	return [chains, modes]

def handle_errors(errors):
	types = {
		1: 'non-alphanumeric chars',
		2: 'uppercase char before final char',
		3: 'overlapped mapping(s)',
	}
	for error in errors:
		msg = 'error: %s: ' % types[error[0]]
		err = str(error[1])
		print(msg + err)
		print(' ' * len(msg) + '^' * len(err))
	exit(1)

def generate_config(config):
	try:
		p_key = '$mod+%s' % config['mod']
		p_sym = config['mod'][0].upper() + '-'
	except:
		p_key = config['key']
		p_sym = config['sym']
	binds = config['binds']

	chains, modes = validate_config(config)

	def gen_mode_exits():
		print('\tbindsym Return mode "default"')
		print('\tbindsym Escape mode "default"')
		print('\tbindsym Control+c mode "default"')
		print('\tbindsym Control+bracketleft mode "default"')

	def gen_prefix_mode():
		print('bindsym %s mode "%s"' % (p_key, p_sym))
		print('mode "%s" {' % (p_sym))
		gen_mode_exits()
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
				print('\tbindsym %s mode "%s%s"' % (key, p_sym, mode))
		print('}')
		print()

	def gen_mode(mode):
		elems = [i for i in chains + modes if mode == i[:-1]]
		elems.sort()
		print('mode "%s%s" {' % (p_sym, mode))
		gen_mode_exits()
		print('\tbindsym %s mode "default"' % (p_key))
		print('\tbindsym BackSpace mode "%s%s"' % (p_sym, mode[:-1]))
		for elem in elems:
			key = elem.replace(mode, '', 1)
			if not key == key.lower():
				key = 'Shift+' + key.lower()
			if not elem in modes:
				print('\tbindsym %s %s; mode "default"'
					% (key, binds[elem]
				))
			else:
				print('\tbindsym %s mode "%s%s"' % (key, p_sym, elem))
		print('}')
		print()

	gen_prefix_mode()
	for mode in modes:
		gen_mode(mode)

for config in configs:
	generate_config(config)
