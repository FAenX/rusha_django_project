# rusha_django_project

Install Docker and docker compose then run the following command

`docker-compose -f docker-compose-dev.yml up`

Basically i am trying to build an infrastructure that 'high level' looks like the image below, so let the complexity begin...

![high level](https://drive.google.com/uc?export=view&id=1rIn8i7xZXocjQ5AfaQqDeWUk-Y3907Hd)


You can create containers using git post-recieve by pushing to a git bare repo in the server.

When you create a new app via Rushiwa, the Cron job will pick it up and create Nginx virtual server config and a git bare repo where a user can push their application to. 

When a user pushes code to the bare repo,  git post receive will run a docker script to either build and run a container or update an existing container. 

The container will be exposed to the outside via Nginx conf that was created by the cronjob. 
