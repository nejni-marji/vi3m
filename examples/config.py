#!/usr/bin/env python3

# i3 modes are case-insensitive. Please don't try to use cased characters
# anywhere but the final character of the string. If you do, just know that
# generate_modes.py is likely to break, possibly silently.

# I highly recommend changing these, they're really not very good defaults.

# These are some shortcut functions I use to make configuration easier.
# I figured I'd add them into the example config.

term = 'i3-sensible-term'
shell = 'bash'

# prepend ~/bin/ to the command
def B(cmd): return '~/bin/%s' % cmd
# prepend exec to the command (you'll probably want this more often than not)
def E(cmd): return 'exec --no-startup-id %s' % cmd
# prepend ~/.i3/bin/ (you probably don't have a script folder there, but I do)
def I(cmd): return '~/.i3/bin/%s' % cmd
# run the command in your preferred shell
def S(cmd): return '%s -c "%s"' % (shell, cmd)
# run the command in your preferred terminal
def T(cmd): return '%s -e %s' % (term, cmd)
# I have a shell script named 'remote' that does ssh and related tasks
def R(cmd): return 'remote %s' % cmd
# This functions basically like a goto.
def C(wm_class): return '[class="%s"] focus' % wm_class

binds = {
	'af': E('firefox'),
	'abcd': E('i3-sensible-term'),
	'ap': E('pavucontrol'),
	'at': E('telegram'),
}

# You can actually have more than one set of binds, each with a different
# prefix key, but I figure most people wouldn't do that anyway, so this bit
# here is a shorthand for just creating one set of binds with one prefix key.

# Also, if you uncomment the 'mod' element, then the script will assume
# key = '$mod+%s' % mod
# sym = mod.upper()
# The commented 'mod' elements will do exactly what is already done in the
# sample configs.

configs = [
	{
		#'key': '$mod+Return',
		#'sym': 'C',
		'mod': 'Return',
		'binds': binds
	},
]

# If you run `./config.py d' or `./config.py debug', it will print out all of
# the bindings, by themselves.

try:
	if argv[1] in ['d', 'debug']:
		for i in binds:
			print('\'%s\': \'%s\'' % (i, binds[i]))
except:
	pass
