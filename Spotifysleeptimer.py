import time
import subprocess

# Get the wait time from the user (in minutes)
wait_time = int(input('Enter the wait time in minutes: '))

# Convert the wait time from minutes to seconds
wait_time *= 60

# Wait for the specified time
start_time = time.time()
while time.time() - start_time < wait_time:
    # Calculate the elapsed time
    elapsed_time = int(time.time() - start_time)

    # Convert the elapsed time to a string and print it to the console
    print('Elapsed time: ' + time.strftime('%M:%S', time.gmtime(elapsed_time)))

    # Pause the script for 1 second
    time.sleep(1)

# Close Spotify
subprocess.call(['taskkill', '/F', '/IM', 'spotify.exe'])
