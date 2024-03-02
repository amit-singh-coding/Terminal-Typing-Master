
# 👩‍💻Terminal Typing Master

**Terminal Typing Master** is a simple Python program that helps you improve your typing speed and accuracy. Test your typing skills, create a username, and compete with others on the leaderboard.


![Typing img Screenshot](https://github.com/amit-singh-coding/Terminal-Typing-Master/blob/main/typing_master_img.jpg)



## Features

- Typing test with a random sentence
- Username creation and validation
- Leaderboard to track and compare typing speeds








## Installation

1- Clone the repository: `git clone https://github.com/amit-singh-coding/Terminal-Typing-Master`

2- Navigate to the project directory: `cd Terminal-Typing-Master`

3- Install dependencies: `pip install -r requirements.txt`

4- Run the program: `python type_wpm.py` 



## Usage

Once installed, you can launch Terminal Typing Master by running the following command:

+ `python type_wpm.py` 

**option**

`Start Typing Test:` Select option 1 to begin a typing test. Follow the instructions to type the provided sentence as fast as you can.

`Create Username:` Select option 2 to create a username. If the username already exists, you'll be prompted to choose another one.

`Show Leaderboard:` Select option 3 to view the leaderboard and see how your typing speed compares to others.

`Exit:` Select option 4 to exit the program.

![options img Screenshot](https://github.com/amit-singh-coding/all_images_of_github/blob/main/typing_ing/welcome.PNG)




## Prerequisites

- Basic understanding of arrays, loops, time, json.

- Familiarity with terminal-based input/output.


## Code Components

**Libraries**


`📚 json :` Used for reading and writing data to JSON files like database.

`🖥️ os :` Used for handling file system operations.

`⏱️ time:` Used for measuring time elapsed during typing tests.

`📚 random :` Used for creating a random sentances.

`🌈 color_the_line:` A custom class for adding colored text to the terminal.

**Functions**

1. `create_directory()`: Creates a directory called "typing_master" if it doesn't exist.

2. `create_username()`: Takes user input to create a username for the typing test.

3. `validate_user(username)`: Validates if the username already exists in the leaderboard.

4. `update_leaderboard(username, wpm)`: Updates the leaderboard with the user's typing speed.

5. `show_leaderboard()`: Displays the leaderboard with user rankings and typing speeds.

6. `generate_random_sentence()`: Generates a random sentence for the typing test.

7. `start_typing_test()`: Initiates the typing test and measures the user's typing speed.

8. `measure_wpm(start_time, end_time, words_typed, randem_words)`: Calculates words per minute (WPM) based on user input and the generated sentence.

9. `main()`: The main function that controls the flow of the program.

## New User

![Typing Starting img Screenshot](https://github.com/amit-singh-coding/all_images_of_github/blob/main/typing_ing/new_user.PNG)


## Results

![Typing Results img Screenshot](https://github.com/amit-singh-coding/all_images_of_github/blob/main/typing_ing/new_user.PNG)


## Leaderboard

![Typing Leaderboard img Screenshot](https://github.com/amit-singh-coding/all_images_of_github/blob/main/typing_ing/leaderboard.PNG)


## Contributions
Contributions are welcome! If you find any issues or have improvements in mind, feel free to submit a pull request amitsingh75184@gmail.com Thanks'you.

## License
This Sudoku Solver is licensed under the `MIT License`.


