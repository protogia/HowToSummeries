# How to stop a playbook with a marker

The following playbook will stop at ´meta: end_play´ and wont print the last task.

stop-example.yml
´´´
---
- hosts: 
  - localhost

  tasks:
    - name: first debug-msg
      debug: msg="hello ansible!"

    - name: stop play for test-purposes
      meta: end_play

    - name: second debug-msg
      debug: msg="ciao ansible!"
´´´

