import twit
import time

request_text = "This is a test, say 'A'."
invalid_input_text = "Error: you didn't say 'A'."
success_text = "Good girl!"
failure_text = "Error: failed posting tweet."

if __name__ == "__main__":
    API = twit.login()
    start_time = time.time()
    time_since_last_request = time.time()
    twit.contact_owner(API, request_text)
    time.sleep(3)
    while(True):
        print('we looping')
        current_time = time.time()
        if (current_time - time_since_last_request) > 900:
            twit.contact_owner(API, request_text)
            time_since_last_request = time.time()

        inpt = twit.TEST_fetch_reply(API)
        print(inpt['success'])
        print(inpt['success'] == 'valid input')
        if inpt['success'] == 'valid input':
            twit.contact_owner(API, success_text)
            break
        elif inpt['success'] == 'invalid input':
            twit.contact_owner(API, invalid_input_text)
            time.sleep(60)
        else:
            time.sleep(30)