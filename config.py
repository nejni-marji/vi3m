#!/usr/bin/env python3

# i3 modes are case-insensitive. Please don't try to use cased characters
# anywhere but the final character of the string. If you do, just know that
# generate_modes.py is likely to break, possibly silently.

# I highly recommend changing these, they're really not very good defaults.

configs = [
	{
		'key': '$mod+m',
		'sym': 'M',
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
