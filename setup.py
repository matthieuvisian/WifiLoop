import os

os.system('sudo cp WifiLoop.py /etc/init.d/WifiLoop.py')
os.system('sudo chmod a+x /etc/init.d/WifiLoop.py')
os.system('sudo update-rc.d WifiLoop.py defaults')
print ('----- Installation DONE ------')
