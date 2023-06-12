# Beta
Beta Market Searcher

This project use postgresql as database. Please download it by the OS you have.
sudo apt-get -y install postgresql

createdb market

sudo -u postgres

alter user <username> with encrypted password '<password>';

pip install -r requirements.txt 

Modify Beta/simple_application/betaproject/betaproject/.env
SECRET_KEY=django-insecure-j-^y0owm7%1ar@j$57#nh=6y(u8h#byac%+r2ev9dah#w0tbb5
DB_NAME=market
DB_USER=peter
DB_PASSWORD=betabeta
DB_HOST=localhost
DB_PORT=5432
# Start our redis server
sudo apt install redis
sudo systemctl status redis
please add hostname to your settings
ALLOWED_HOSTS = ['YOUR HOSTNAME']

go to http://[hostname]:8000/markets/
python3 manage.py runserver 0.0.0.0:8000
# Close your redis server
sudo systemctl stop redis

# Apply unit test
python3 manage.py test