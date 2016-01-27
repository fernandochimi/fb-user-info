doc:
		$(MAKE) -C docs/ html
		# Uncomment open ... if you use Mac
		# open docs/_build/html/index.html
		xdg-open docs/_build/html/index.html

test:
		coverage run --source="fb_user_info/fb_user_info" --omit="../../**migrations**, ../../**tests**" ./fb_user_info/manage.py test fb_user_info -v 2 --settings=settings.test --failfast
		coverage report -m

html:
		coverage html
		# Uncomment open ... if you use Mac
		# open htmlcov/index.html
		xdg-open htmlcov/index.html

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log