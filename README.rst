
.. |image1| image:: https://cloud.githubusercontent.com/assets/1279644/15648187/8c09c7be-2671-11e6-80dc-45753d327fbe.png
.. |image2| image:: https://cloud.githubusercontent.com/assets/1279644/15648193/93930298-2671-11e6-9f8f-c2500d435902.png
.. |image3| image:: https://cloud.githubusercontent.com/assets/1279644/15648195/97213ac4-2671-11e6-8c2e-13c906c483b0.png
.. |image4| image:: https://cloud.githubusercontent.com/assets/1279644/15648201/9c03fa7c-2671-11e6-9a80-37aac250099e.png
.. |image5| image:: https://cloud.githubusercontent.com/assets/1279644/15648205/a4565aa8-2671-11e6-938a-6fb2a614650c.png
.. |image6| image:: https://cloud.githubusercontent.com/assets/1279644/15648208/a657c0a8-2671-11e6-9c68-840b869cca6f.png
.. |image7| image:: https://cloud.githubusercontent.com/assets/1279644/15648209/a8de86ea-2671-11e6-884d-ecc12222b1d1.png
.. |image8| image:: https://cloud.githubusercontent.com/assets/1279644/15648212/ab8ab1fc-2671-11e6-8411-737c7f120bf2.png
.. |image9| image:: https://cloud.githubusercontent.com/assets/1279644/15648228/bf89c27e-2671-11e6-99aa-fba1c9ce64bc.png
.. |image10| image:: https://cloud.githubusercontent.com/assets/1279644/15648232/c1444a9e-2671-11e6-9e92-ea0ad43e3352.png
.. |image11| image:: https://cloud.githubusercontent.com/assets/1279644/15648233/c3436744-2671-11e6-8a6e-f4b21ea52945.png
.. |image12| image:: https://cloud.githubusercontent.com/assets/1279644/15648237/c5b9ce00-2671-11e6-9620-0fc959e20313.png
.. |image13| image:: https://cloud.githubusercontent.com/assets/1279644/15648240/c87a95a2-2671-11e6-9ab8-b6561c736d11.png




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

**Here are few things you can test;**

* Create some tickets (teamleader and root users can create tickets)
* Login as developer or teamleader to approve some transitions (teamleader and developers can approve transitions.)
* While **developer** can approve **"open -> inprogress"**, **"in-progress -> resolved"** and **"re-opened -> in-progress"**, **teamleader** can approve **"resolved -> re-opened"** and **"resolved -> closed"**

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


Images:
^^^^^^^

|image1|
|image2|
|image3|
|image4|
|image5|
|image6|
|image7|
|image8|
|image9|
|image10|
|image11|
|image12|
|image13|
