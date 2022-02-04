import twit
import time

request_text = "TEST TEST TEST! Please enter the Quality/Animal/Buyer, separated by spaces."
invalid_input_text = "TEST Error: Invalid input."
success_text = "TEST Thread posted successfully!"
failure_text = "TEST Error: failed posting {} tweet."

if __name__ == "__main__":
    API = twit.login()

    with open('input_log.txt', 'r') as f:
        latest = f.readlines()[-1]
        data = latest.split(' ')
        latest_message = data[0]
        latest_quality = data[1]
        latest_animal = data[2]
        latest_buyer = data[3]

    twit.contact_owner(API, request_text)
    start_time = time.time()
    start_time_string = str(start_time).split('.')[0]
    time_since_last_request = time.time()

    while (True):
        time.sleep(60)
        current_time = time.time()
        if (current_time - time_since_last_request) > 1200:
            twit.contact_owner(API, request_text)
            time_since_last_request = time.time()

        inpt = twit.fetch_reply(API)

        if not inpt['success']:
            continue

        if inpt['timestamp'] < max(latest_message, start_time_string):
            continue

        else:
            latest_message = inpt['timestamp']

        if inpt['success'] == 'valid input':
            result = inpt['data'][0]
            if result == -1:
                twit.contact_owner(API, success_text)
            else:
                twit.contact_owner(API, failure_text.format(result))
            break

        elif inpt['success'] == 'invalid input':
            twit.contact_owner(API, invalid_input_text)

    with open('input_log.txt', 'a') as f:
        log_addition = '\n' + latest_message
        if result == -1:
            log_addition += ' {} {} {}'.format(*inpt['data'])
        else:
            log_addition += ' 0 0 0'

        f.write(log_addition)