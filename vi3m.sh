#!/bin/bash
I3="$HOME/.i3"

if ! [[ -f $I3/preconfig ]]; then
cat << EOM
You need to move ~/.i3/config to ~/.i3/preconfig.
Also, back it up somewhere else: although this should never overwrite that file,
I really don't want to be the reason you lose your i3 config.

Also, another note: generate_modes.py does NOT check for configuration errors.
If you give it a weird config it will probably break, possibly silently.
EOM
exit
fi

{
	cat "$I3"/preconfig;
	"$I3"/vi3m/generate_modes.py
} > "$I3"/config
i3-msg reload
