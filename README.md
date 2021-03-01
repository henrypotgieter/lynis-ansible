# lynis-ansible
Simple set of files to automate scanning hosts with lynis using ansible to run
the audit process locally on each system.  Gather reports back to master system for review.

# Usage
Update your /etc/ansible/hosts and define activehosts (or whatever group of
hosts you like) to conduct the audit service against.

Run the python script to automatically download the latest version of the lynis
software package.  Place this file into wherever you store your ansible static
files (/ansible/static_files typically)

Execute the playbook and wait for it to process through each of the hosts.

Finally check your /tmp directory, you should see all the reports contained
under /tmp/lynis-report/
