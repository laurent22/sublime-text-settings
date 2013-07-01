Installing on Ubuntu:

	sudo add-apt-repository ppa:webupd8team/sublime-text-2
	sudo apt-get update
	sudo apt-get install sublime-text
	
	mkdir ~/.config/sublime-text-2/
	cd ~/.config/sublime-text-2/
	git clone https://github.com/laurent22/sublime-text-settings.git customsettings
	mv Packages Packages.DEFAULT
	mv customsettings/* .
	mv customsettings/.* .
	git submodule init
	git submodule update
