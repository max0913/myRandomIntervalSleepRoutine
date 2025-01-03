# https://chatgpt.com/c/6777c60d-48bc-800b-b751-e29cfa318b51

import time
import random
import subprocess
import sys

def myRandomIntervalSleepRoutine(min_wait_mins, max_wait_mins, call_script_name):
    try:
        while True:
            # Generate a random interval in seconds
            interval = random.randint(min_wait_mins * 60, max_wait_mins * 60)
            print(f"Sleeping for {interval // 60} minutes ({interval} seconds)...")

            # Sleep for the calculated interval
            time.sleep(interval)

            # Execute the specified script
            print(f"Executing script: {call_script_name}")
            result = subprocess.run(call_script_name, shell=True, capture_output=True, text=True)

            # Log output (optional)
            print(f"Script output:\n{result.stdout}")
            if result.stderr:
                print(f"Script error:\n{result.stderr}")

    except KeyboardInterrupt:
        print("Routine interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 myDaemon.py <minWaitMins> <maxWaitMins> <callScriptname>")
        sys.exit(1)

    # Parse command-line arguments
    try:
        min_wait_mins = int(sys.argv[1])
        max_wait_mins = int(sys.argv[2])
        call_script_name = sys.argv[3]

        if min_wait_mins <= 0 or max_wait_mins <= 0 or min_wait_mins > max_wait_mins:
            raise ValueError("Invalid wait time values.")

        # Start the random interval sleep routine
        myRandomIntervalSleepRoutine(min_wait_mins, max_wait_mins, call_script_name)

    except ValueError as ve:
        print(f"Error in input arguments: {ve}")
        sys.exit(1)
