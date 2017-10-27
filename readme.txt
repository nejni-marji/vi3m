1.
Put all of these files in ~/.i3/vi3m/.

2.
Copy examples/config.py to the vi3m main directory.

3.
Change your reload binding to:
exec ~/.i3/vi3m/vi3m.sh; reload
And your restart binding to:
exec ~/.i3/vi3m/vi3m.sh; restart

4.
Optionally, but probably ideal, is also to change your restart binding.
Read ~/.i3/vi3m/config.py and probably put your own configs there.

5.
I don't know if this is necessary, but I recommend making these executable.
chmod u+x generate_modes.py show_bar.sh vi3m.sh
