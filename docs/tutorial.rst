.. Facebook User Info documentation master file, created by
   sphinx-quickstart on Mon Jan 25 23:29:21 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tutorial
==================

	Let's run the API project to get Facebook users information!
	The main URI is ``/api/v1/fb-user/``

Create a API Token
-------------------------
	**Note**: It is important that you follow the instructions of the ``README.md`` file, in initial page of the GitHub's project.

	* After you have created the superuser, access ``http://localhost:8000/admin``;
	* Click in ``Token``, on ``FB_USER_INFO`` category;
	* Click in ``Add Token``;
	* If you wish to associate this Token with a User that you have created, you can select by the ``User`` select box;
	* Click in save.

	This is the Token that you have to access the Facebook User Info API. It is important to you keep this Token to access the services.


List the Facebook Users Info
---------------------------------
	``curl -X GET "http://localhost:8000/api/v1/fb-user/?token={valid_token}"``

	Ok! You get the API Token to access the service.
	To Request the list of Facebook Users, access ``http://localhost:8000/api/v1/fb-user/?token={valid_token}&limit={limit}``, where:
		- **valid_token** (**Required**): Token generated in Admin Page of Project (String);
		- **limit**: The limit of Users to display in this page. The default is 10 (Integer);

	Response:
		.. code-block:: json

			"meta": {
				"total_count": 2,
				"previous": false,
				"limit": 10,
				"page": 1,
				"next": false,
			},
			"objects": [
				{
				    "facebook_id": 100011170511979,
				    "link": "https://www.facebook.com/app_scoped_user_id/121802561535427/",
					"name": "Fernando Chimicoviaki",
					"gender": "male",
				},

				{
				    "facebook_id": 132416543126,
				    "link": "https://www.facebook.com/app_scoped_user_id/100000024502625/",
					"name": "Female User",
					"gender": "female",
				},
			]

	**NOTE ABOUT FIELD LINK**: The field ``link`` is avaliable in the API Graph V2.0 and higher. The field ``username`` was deprecated. Because of this, the field ``username`` was replaced by ``link``.


Detail Facebook User Info
---------------------------------
	``curl -X GET "http://localhost:8000/api/v1/fb-user/{facebook_id}/?token={valid_token}"``

	To Request the detail of Facebook User, access ``http://localhost:8000/api/v1/fb-user/{facebook_id}/?token={valid_token}``, where:

		- **facebook_id** (**Required**): The id of the user that you get some information;
		- **valid_token** (**Required**): Token generated in Admin Page of Project (String);

	Response:
		.. code-block:: json

			{
			    "facebook_id": 100011170511979,
			    "link": "https://www.facebook.com/app_scoped_user_id/121802561535427/",
				"name": "Fernando Chimicoviaki",
				"gender": "male",
			},

	**Note**: The request detail of the user will get data first in the database. If the User does not exist in the database API, the service will consult ``https://graph.facebook.com`` to get the informations and save. If the user does not have ``gender``, the service will consult ``https://api.genderize.io`` to get the gender by the first name. By the command ``GET`` above, the API service do this automatically.


Delete Facebook User Info
---------------------------------
	``curl -X DELETE "http://localhost:8000/api/v1/fb-user/{facebook_id}/?token={valid_token}"``

	To delete a Facebook User, type in terminal ``curl -X DELETE "http://localhost:8000/api/v1/fb-user/{facebook_id}/?token={valid_token}"``, where:

		- **facebook_id** (**Required**): The id of the user that you get some information;
		- **valid_token** (**Required**): Token generated in Admin Page of Project (String);
