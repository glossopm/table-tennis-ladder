tasks:
    - name: Update and upgrade apt packages
    become: true
    apt:
        upgrade: yes
        update_cache: yes


  - name: Install nginx
    apt:
      name: nginx
      state: present
