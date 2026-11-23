Role Name
=========

A brief description of the role goes here.

Requirements
------------

OS initialization is available for CentOS 8 and Rocky Linux 9. Select an
available Rocky Linux 9 image with `dl_cloud_image` when deploying on Rocky.
Rocky Linux 10 is not supported by this role.

On Rocky Linux 9, the role installs MongoDB 7.0, compatible with the role's
pinned PyMongo version. MongoDB 7.0 reaches end of support on August 31, 2027.
This setup is intended for a fresh database; the role does not migrate an
existing MongoDB installation or its data. Plan a supported migration separately.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
