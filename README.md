# 🚅 trAIn
A white-box machine learning system for end-users. 
### Getting Started

### Prerequisites
```
pip install requirements.txt
```
### Contribution

**Install Dependencies**
- Python>=[3.5](https://www.python.org/downloads/release/python-350/)
- [django](https://www.djangoproject.com/download/)
- [mysqlclient](https://pypi.org/project/mysqlclient/)
- Install Mysql ([XAMPP](https://www.apachefriends.org/download.html) is prefered)
- Fork the repository
- Clone the repository
```
git clone https://github.com/your_username/trAIn.git
cd trAIn
```
**Database setup**
- create env.py in dataprocessing direcroty
```
cp dataprocessing/env_example.py env.py
```
- Enter the configuration details in env.py
```
env_var = {
    'DATABASE_NAME'       : 'ENTER_DATABASE_NAME',
    'DATABASE_USER_NAME'  : 'ENER_DATABASE_USERNAME',
    'DATABASE_PASSWORD'   : 'ENTER DATABASE_PASSWORD',
}
```
- Run Commands
```python
~$ python manage.py migrate
~$ python manage.py runsurver
```