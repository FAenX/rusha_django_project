#!/bin/bash

# Install Rusha Django Project
ansible-playbook ansible/installation_playbook.yml -i ansible/hosts.ini --user root

