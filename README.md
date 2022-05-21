# Django-ML-Internship
## Contributors
- Grace Sharma
- Aritra Mitra
## About
On-Going Project.
The goals of this Project
are as follows:
- "Add Points"
- "Add Points" 
## Instruction
- **Create virtual environment**
```bash
sudo pip install virtualenv      # This may already be installed
virtualenv .env                  # Create a virtual environment
```
- **Activate virtual environment**
```bash
source .env/bin/activate         # Activate the virtual environment
pip install -r requirements.txt  # Check/Install dependencies
```
- **Run following commands**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver       # To Start Local Server 
```
- **Procedure to create an administrator**
```bash
python manage.py createsuperuser
```
## HTML File Description
- **templates/base.html** - Basic Layout and Top Navigation Bar
- **static/main.css** - Main CSS file, applied to all pages 
- **Course/templates/Course/home.html** - Body HTML of Course Page contains Main Video, Playlist, Text Editor/Python IDE
- **User/templates/User/** - Body HTML of Login, Logout, Signup Page 
- **User/templates/User/list_codes.html** - HTML of list of codes per user
- **User/templates/User/detail_code.html** - HTML of detail view of a saved code
