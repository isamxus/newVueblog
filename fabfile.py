#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fabric.api import *
from fabric.operations import sudo
env.user = 'root'
env.hosts = ['112.74.47.33']
env.password = 'Qq123456'


def deploy():
	with settings(warn_only=True):
		run('useradd -m -s /bin/bash ljc')
		run('usermod -a -G sudo ljc')
		run('echo "ljc":"ljc834775778" | chpasswd')
	run('sudo apt-get update')
	run('sudo apt-get upgrade')
	run('sudo apt-get install nginx')
	run('sudo apt-get install git python3 python3-pip')
	run('sudo apt-get install virtualenv')
	run('sudo service nginx start')
	with settings(warn_only=True):
		result = run('git clone https://github.com/isamxus/blogManagement.git /home/ljc/blogManagement')
	run('cd /home/ljc/')
	run('virtualenv --python=python3 env')
	run('source env/bin/activate')
	with cd('/home/ljc/blogManagement/'):
		run('ls')
		run('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt')
	with settings(warn_only=True):
		result = put('C:\\Users\\Administrator\\Desktop\\myblogdjango\\amxusli.conf', '/home/ljc/blogManagement')
	with cd('/home/ljc/blogManagement'):
		run('ls')
		run('sudo mv amxusli.conf /etc/nginx/sites-available')
		run('chmod 777 /etc/nginx/sites-available/amxusli.conf')
	with settings(warn_only=True):
		run('sudo ln -s /etc/nginx/sites-available/amxusli.conf /etc/nginx/sites-enabled/amxusli.conf')
		run('pip3 install gunicorn')
	with cd('/home/ljc/blogManagement'):
		run('sudo service nginx stop')
		run('sudo service nginx start')
		run('gunicorn --bind unix:/tmp/www.amxus.info.socket myblogdjango.wsgi:application')
	#run('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt')

	#run('su - ljc')
	#run('git clone https://github.com/isamxus/blogManagement.git')