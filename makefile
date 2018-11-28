all: launch

install:
	sudo apt-get -y update
	apt-get install git -y > /dev/null
	sudo debconf-set-selections <<< 'mysql-server-5.7 mysql-server/root_password password sys'
	sudo debconf-set-selections <<< 'mysql-server-5.7 mysql-server/root_password_again password sys'
	sudo apt-get -y install mysql-server libapache2-mod-auth-mysql libapache2-mod-php7.0
	sudo apt-get -y install python-dev python-pip -q -y
	sudo apachectl restart

launch:
	# pipenv run python -m api.services.contact.router
	# pipenv run gunicorn -b 0.0.0.0:5000 data.main:app --reload
	# pipenv run gunicorn -b 0.0.0.0:5000 auth.main:app --reload
	# pipenv run gunicorn -b 0.0.0.0:5000 user.main:app --reload

	# pipenv run gunicorn -b 24.138.161.30:80 api.main:router.app
	#
	# pipenv run gunicorn -b 0.0.0.0:5001 api.services.data.router:data.app
	# pipenv run gunicorn -b 0.0.0.0:5002 api.services.auth.router:auth.app
	# pipenv run gunicorn -b 0.0.0.0:5003 api.services.user.router:user.app

	pipenv run gunicorn -b 0.0.0.0:5000 api.main:monolith.app

clean:
	rm -f api/*.pyc
	rm -f api/core/*.pyc
	rm -f api/services/*.pyc
	rm -f api/services/auth/*.pyc
	rm -f api/services/data/*.pyc
	rm -f api/services/user/*.pyc
