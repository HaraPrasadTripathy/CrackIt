from flask import Flask, render_template, request
import itertools
import time

app = Flask(__name__)

def crack_password(password, max_length, timeout):
    # Define the characters to be used for password generation
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/#@!&*$%_-+(){}[]"
    start_time = time.time()  # Record the start time of the cracking process
    attempts = 0  # Initialize the number of attempts made to crack the password
    # Iterate through different lengths of combinations
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            attempts += 1  # Increment the attempt counter
            attempt = "".join(combination)  # Generate a password attempt from the combination
            if attempt == password:
                # If the attempt matches the password, calculate the elapsed time and return
                elapsed_time = time.time() - start_time
                if elapsed_time <= timeout:
                    return attempt, elapsed_time  # If the cracking time is within the timeout, return the result
                else:
                    estimated_time = (elapsed_time / attempts) * (len(characters) ** length)
                    # If the cracking time exceeds the timeout, estimate the remaining time and return
                    return attempt, estimated_time

            if time.time() - start_time > timeout:
                # If the cracking time exceeds the timeout, estimate the remaining time and return
                elapsed_time = time.time() - start_time
                estimated_time = (elapsed_time / attempts) * (len(characters) ** length)
                return "Time Exceeded", estimated_time
    # If the password is not found within the specified maximum length, return appropriate message
    return "Password not found within the specified maximum length.", None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("string")
        if not password: 
            return render_template("index.html", message="Please Enter a password.")
        max_length = 8  # Maximum length of password to consider during cracking
        timeout = 45  # Timeout duration in seconds
        # Call the crack_password function to attempt cracking the password
        result, time_taken = crack_password(password, max_length, timeout)
        if result == "Time Exceeded":
            return render_template("index.html", message=f"Time Exceeded. Estimated time to crack: {round(time_taken, 2)} seconds.")
        elif result == "Password not found within the specified maximum length.":
            return render_template("index.html", message=result)
        else:
            return render_template("index.html", result=result, time_taken=round(time_taken, 2))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)