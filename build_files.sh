# build_files.sh
pip install -r requirements.txt
python3.11 flask_app.py collectstatic --noinput