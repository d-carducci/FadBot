import twit
import time

request_text = "Bone Market Update! Please enter the Quality/Animal/Buyer, separated by spaces."
invalid_input_text = "Error: Invalid input."
success_text = "Thread posted successfully!"
failure_text = "Error: failed posting {} tweet."

if __name__ == "__main__":
    API = twit.login()
    start_time = time.time()
    time_since_last_request = time.time()
    twit.contact_owner(API, request_text)
    time.sleep(60)
    while(True):
        current_time = time.time()
        if (current_time - time_since_last_request) > 900:
            twit.contact_owner(API, request_text)
            time_since_last_request = time.time()

        inpt = twit.fetch_reply(API)
        if inpt['success'] == 'valid input':
            result = twit.update(API, *inpt['data'])
            if result == -1:
                twit.contact_owner(API, success_text)
            else:
                twit.contact_owner(API, failure_text.format(result))
            break
        elif inpt['success'] == 'invalid input':
            twit.contact_owner(API, invalid_input_text)
        else:
            time.sleep(60)