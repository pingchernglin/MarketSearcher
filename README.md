# Blockchain Market Searcher

Blockchain Market Searcher is a project that utilizes PostgreSQL as its database. Please follow the instructions below to set up and run the project.

## Prerequisites

- PostgreSQL: Install PostgreSQL based on your operating system. For example, on Ubuntu, you can use the following command:
  ```bash
  sudo apt-get -y install postgresql
  ```

## Setting up the Database

Create a new database named "market":
```bash
createdb market
```

Switch to the PostgreSQL user:
```bash
sudo -u postgres
```

Set a password for your user:
```sql
alter user <username> with encrypted password '<password>';
```

## Installation

Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/your-username/beta-market-searcher.git
cd beta-market-searcher
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

Modify the environment variables in `MarketSearcher/simple_application/marketsearcher/marketsearcher/.env`:
```makefile
SECRET_KEY=[private key]
DB_NAME=market
DB_USER=[user]
DB_PASSWORD=[password]
DB_HOST=localhost
DB_PORT=5432
```

## Running the Application

Start the Redis server:
```lua
sudo apt install redis
sudo systemctl start redis
```

Add your hostname to the settings in `MarketSearcher/simple_application/project/project/settings.py`:
```css
ALLOWED_HOSTS = ['YOUR HOSTNAME']
```

Start the application server:
```bash
python3 manage.py runserver 0.0.0.0:8000
```

Access the application by opening `http://[hostname]:8000/markets/` in your web browser.

## Running Unit Tests

To run the unit tests for the project, execute the following command:
```bash
python3 manage.py test
```

Note: Make sure to close the Redis server after you have finished using the application:
```bash
sudo systemctl stop redis
```

Feel free to reach out if you have any further questions or issues regarding the Blockchain Market Searcher project.
