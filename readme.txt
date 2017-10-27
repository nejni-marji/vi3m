Put all of these files in ~/.i3/vi3m/.
Copy examples/config.py to the vi3m main directory.
Change your reload binding to:
exec ~/.i3/vi3m/vi3m.sh; reload
And your restart binding to:
exec ~/.i3/vi3m/vi3m.sh; restart
Optionally, but probably ideal, is also to change your restart binding.
Read ~/.i3/vi3m/config.py and probably put your own configs there.

I don't know if this is necessary, but I recommend making these executable.
chmod u+x generate_modes.py show_bar.sh vi3m.sh
