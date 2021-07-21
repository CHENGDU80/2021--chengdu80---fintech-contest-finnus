Folder structure:

/classification_algorithm
1. Contains the classification model. MLI, feature engineering codes, and the final prediction(.csv file)

/presentation
1. Contains the presentation slides

/chengdu_front_end/assets
1. sample images and design support files for the app

/chengdu_front_end/data
1. sample data for the product prototype (app) to show the results

/chengdu_front_end/views
1. Different pages for the app


How to run the app

1. Start the following EC2 instance - ubuntu-2.

2. SSH into the instance, and change directory into the app folder by following command: cd chengdu_front_end

3. Initialize the python environment using the following command: source activate myenv

4. Install code requirements using the following command: pip3 install -r requirements.txt

5. Check the port 8888 to make sure no operation is running using following command: sudo netstat -tulpn | grep 8888

6. If there is any operation running, kill that operation by following command: sudo kill -9 [operation_code_name]

7. Run the following command: python3 index.py

8. To launch the app, and open it at following address: 3.0.133.209:8888

9. After launching the app, you can login using following 2 accounts:
--For the individual user: user_name - individual_user and password - individual_user
--For the corporate user: user_name - corporate_user and password - corporate_user

