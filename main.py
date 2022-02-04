import twit
import time
import wiki

request_text = "Bone Market Update! Please enter the Quality/Animal/Buyer, separated by spaces."
bootup_text = "Bone Market Update! Fetching WQ data from wiki."
repetitions_text = "Wiki qualities haven't been updated yet (checked {} times)"
invalid_input_text = "Error: Invalid input."
success_text = "Thread posted successfully!"
failure_text = "Error: failed posting {} tweet."

if __name__ == '__main__':
    API = twit.login()
    twit.contact_owner(API, bootup_text)

    with open('input_log.txt', 'r') as f:
        latest = f.readlines()[-1]
        data = latest.split(' ')
        prev_message = data[0]
        prev_qualities = data[1:]

    repetitions = 0

    while(True):

        inpt = wiki.fetch_BM_values()
        same_inpts = 0
        for prev_quality, current_quality in zip(prev_qualities, inpt):
            same_inpts += (prev_quality == current_quality)

        if same_inpts:
            print('some qualities haven\'t been updated yet')
            repetitions += 1
            if not repetitions % 5:
                twit.contact_owner(API, repetitions_text.format(repetitions))
            time.sleep(60)


        else:
            update_time = time.time()
            result = twit.update(API, *inpt)

            if result == -1:
                twit.contact_owner(API, success_text)
            else:
                twit.contact_owner(API, failure_text.format(result))
            break

    if result == -1:
        with open('input_log.txt', 'a') as f:
            f.write('\n{} {} {} {}'.format(update_time, *inpt))
'''
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
    time_since_last_request = time.time()
    start_time = str(time_since_last_request).split('.')[0]

    while(True):
        time.sleep(60)
        current_time = time.time()
        if (current_time - time_since_last_request) > 1200:
            twit.contact_owner(API, request_text)
            time_since_last_request = time.time()

        inpt = twit.fetch_reply(API)

        if not inpt['success']:
            continue

        if inpt['timestamp'] < max(latest_message, start_time):
            continue

        else:
            latest_message = inpt['timestamp']

        if inpt['success'] == 'valid input':
            result = twit.update(API, *inpt['data'])
            if result == -1:
                twit.contact_owner(API, success_text)
            else:
                twit.contact_owner(API, failure_text.format(result))
            break

        elif inpt['success'] == 'invalid input':
            twit.contact_owner(API, invalid_input_text)

    if result == -1:
        with open('input_log.txt', 'a') as f:
            f.write('\n{} {} {} {}'.format(latest_message, *inpt['data']))'''