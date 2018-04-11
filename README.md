Users
=========

This role attempt the goal to manage users on Odoo. To use this module, an existing Odoo infrastructure need to be setup prior and credentials information set.
This role support three type of action:

* **create**: create users based on a list dictionary of dictionary (look at the variable `users` variable), only some few parameters are required to create single user

* **configure**: configure Odoo user's attributes, it's a simple re-writing of user attribute even if the value change or not (look at the `users_to_configure` variable)

* **delete**: simply delete the list of users provided (look at the `users_to_delete` variable)

Odoo version tested
-------------------
-> 10.0

Requirements
------------

You need to install python dependancies on odoo host : xmlrpclib

Role Variables
--------------

There are a lot of variables, so to see all of them plase check the `default/main.yml` where i present variable with description and cautions

Dependencies
------------

.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      user: root
      become: yes
      gather_facts: false

      pre_tasks:
        - block:
            - name: "Check connectivity"
             ping: ~
          rescue:
            - debug:
                msg: "Module ping: error"
            - raw: bash -c "test -f /usr/bin/python || (apt-get update && apt-get install python python3 -yqq) || (yum -y install python)"
              register: output
          always:
            - setup: ~

      roles:
        - { role: users, tags: ['create', 'configure'] }

License
-------

BSD

Author Information
------------------

- Dirane TAFEN (diranetafen@yahoo.com)
