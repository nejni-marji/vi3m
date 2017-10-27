#!/usr/bin/env python3

# i3 modes are case-insensitive. Please don't try to use cased characters
# anywhere but the final character of the string. If you do, just know that
# generate_modes.py is likely to break, possibly silently.

# I highly recommend changing these, they're really not very good defaults.

# If you uncomment the 'mod' element, then the script will assume you want
# key = '$mod+%s' % mod
# sym = mod.upper()
# The commented 'mod' elements will do exactly what is already done in the
# sample configs.

configs = [
	{
		'key': '$mod+m',
		'sym': 'M',
		#'mod': 'm'
		'binds': {
			'h': 'focus left',
			'j': 'focus down',
			'k': 'focus up',
			'l': 'focus right',
			'H': 'move left',
			'J': 'move down',
			'K': 'move up',
			'L': 'move right',
			'gt': 'exec telegram',
		}
	},
	{
		'key': '$mod+z',
		'sym': 'Z',
		#'mod': 'z',
		'binds': {
			'h': 'focus left',
			'l': 'focus right',
			'ap': 'exec pavucontrol',
			'aP': 'exec pavucontrol',
			'ax': 'exec xterm',
			'abcd': 'exec xterm',
		}
	},
]
