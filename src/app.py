from flask import Flask
import time
import threading
import random

application = Flask(__name__)

@application.route('/test', methods=['GET'])
def test():
    return "test"




@application.route('/sleep', methods=['GET'])
def sleep():
    for i in range(10):
        print("sleeping...", 10-i)
        time.sleep(1)
    print("sleeping done!")
    return "test"



@application.route('/show_thread_name', methods=['GET'])
def show_thread_name():
    thread_name = threading.current_thread().name
    for i in range(10):
        print(f"working: {thread_name}")
        time.sleep(1)
    return "success"




not_threadsafe_dict = {"random": 0}

@application.route('/not_threadsafe', methods=['GET'])
def not_threadsafe():
    r = random.random() * 1000
    not_threadsafe_dict["random"] = round(r)
    for i in range(10):
        print("id", i, not_threadsafe_dict["random"])
        time.sleep(1)
    return "success"


threadsafe_dict = threading.local()
threadsafe_dict = {}

@application.route('/threadsafe', methods=['GET'])
def threadsafe():
    r = random.random() * 1000
    threadsafe_dict["random"] = round(r)
    for i in range(10):
        print("id", i, threadsafe_dict["random"])
        time.sleep(1)
    return "success"




# Main function for setting up port 5001 , global host name
if __name__ == '__main__':
    pass
    #application.run(port=5000, host='0.0.0.0', threaded=True)
    #application.run(port=5000, host='0.0.0.0', threaded=False)
    #application.run(port=5000, host='0.0.0.0', threaded=False, processes=3)
