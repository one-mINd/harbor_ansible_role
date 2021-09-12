one_mind.harbor_ansible_role
=========

Ansible role to deploy Harbor registry server and manage users, projects and members.


Tags
--------------
**install**
  Download and install Harbor on target host.
  
**users**
  Start a users managment scripts. Vars harbor_projects, harbor_members or harbor_users mast be defined.


Role Variables
--------------
**harbor_hostname** - This var must be overwritten, because by default it localhost, but Harbor can't work on that hostname.

**harbor_admin_password** and **harbor_db_password** must be overwritten to :)

**harbor_config_dir** - place where harbor installation scripts and docker-compose.yml will be stored.

**harbor_connection_protocol** - can be http or https. When value is http secure connection will not configure, and Harbor will be available only on http port.

**harbor_http_port** and **harbor_https_port** - http/https ports

**harbor_remote_certificate_dir** and **harbor_remote_private_key_dir** dirs where certificates for harbor stored.

**harbor_users** - list of users to be created
 - username
 - email
 - password
 - realname
 - comment

**harbor_projects** - list of projects to be created
 - project_name 
 - public (true/false)
    
**harbor_members** - list of members in projects to be created
 - project (existing project)
 - role_id (1/2/3)
 - username (existing user)


Example Playbook
----------------
```
- hosts: servers
  roles:
      - one_mind.harbor_ansible_role
    vars:
      harbor_projects:
        - project_name: "firstproject"
          public: "true"
        - project_name: "secondproject"
          public: "false"
      harbor_members: 
        - project: "firstproject"
          role_id: 1
          username: "user_one"
        - project: "secondproject"
          role_id: 2
          username: "second_one"
      harbor_users:
        - username: "user_one"
          email: "email@mail.com"
          password: "harboruser12345"
          realname: "user one"
          comment: "void"
        - username: "second_one"
          email: "email_two@mail.com"
          password: "harboruser12345"
          realname: "user two"
          comment: "void"
```

More info
----------------
Official docs - https://goharbor.io/docs/2.3.0/
