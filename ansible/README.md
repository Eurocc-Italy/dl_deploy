Place your OpenStack cloud configuration in `~/.config/openstack/clouds.yml`.

The requirements use Ansible 9's bundled `openstack.cloud` 2.3 collection
with openstacksdk 1.x. The collection requires the SDK in the Python
interpreter that runs the OpenStack modules, not just the interpreter that
runs `ansible-playbook`.

For a local deployer, install the root requirements in a virtual environment
and explicitly use that environment's Python:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cd ansible
ansible-playbook -i inventory/hosts site.yml 
```

Some dependencies require a C compiler and Python development headers when
installing; on Ubuntu these are provided by `build-essential` and
`python3-dev`.

`python-openstackclient` is a separate package from `openstacksdk`; changing
only the client version does not necessarily change the SDK used by Ansible.
If another `openstack.cloud` collection is installed, check which version
Ansible selects with `ansible-galaxy collection list openstack.cloud`.

The HPC account setup uses a working `python3` or `python` from the login
shell. If neither is available, it runs `module load python` in a Bash login
shell and uses the resulting environment to create the virtual environment and
install dependencies. The Python module must provide a version supported by
Ansible and the required Python packages. If the Python module supplies shared
libraries, it must also be loaded when the virtual environment is used later.
