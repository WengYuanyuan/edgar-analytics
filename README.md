 
# This is the submission for project Edgar-analytics
## Repo directory structure

The directory structure of the submission repo is as following:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── sessionization.py
    ├── input
    │   └── inactivity_period.txt
    │   └── log.csv
    ├── output
    |   └── sessionization.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── inactivity_period.txt
            |   │   └── log.csv
            |   |__ output
            |   │   └── sessionization.txt
            ├── extra_test_1 
                    
## Dependancy

My solution uses data structure 'Priority Queue Dictionary' which use the following pqdict package:

http://pqdict.readthedocs.io/en/latest/
https://github.com/nvictus/priority-queue-dictionary

Please download and install the module by:
pip install git+https://github.com/nvictus/priority-queue-dictionary

