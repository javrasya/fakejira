Fake Jira an example for django-river
=====================================

This is an example for django-river which is created in its first video tutorial. In here, everything is ready. Just follow the documentation below.

django-river: https://github.com/javrasya/django-river

Documentation
-------------

   .. code:: python

      git clone https://github.com/javrasya/fakejira
      pip install -r requirements.txt
      cd fakejira
      python manage.py migrate
      python manage.py loaddata base/fixtures/base.yaml

It is ready to workflowing now. All configuration and scenario in the video tutorial is created by loading the fixture file.

Here are few things you can test;

* Create some tickets (teamleader and root users can create tickets)
* Login as developer or teamleader to approve some transitions (teamleader and developers can approve transitions.)
* While developer can approve "open -> inprogress", "in-progress -> resolved" and "re-opened -> in-progress", teamleader can approve "resolved -> re-opened" and "resolved -> closed"

User Credentials:
^^^^^^^^^^^^^^^^^

+-------------+---------------+----------+
| **Role**    | **Username**  | **Pass** |
+=============+===============+==========+
| Super Admin | root          | q1w2e3r4 |
+-------------+---------------+----------+
| Team Leader | team_leader_1 | q1w2e3r4 |
+-------------+---------------+----------+
| Developer   | developer_1   | q1w2e3r4 |
+-------------+---------------+----------+

