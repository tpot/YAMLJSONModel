install:
	python setup.py install --user

test:
	python setup.py nosetests

clean:
	python setup.py clean
