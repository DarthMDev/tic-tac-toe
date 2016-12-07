cd "$(dirname "$0")"
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install git
sudo xcode-select --install
brew install python
sudo pip install gitpython
