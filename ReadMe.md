# The mouse & the cheese
![Capture2](https://github.com/user-attachments/assets/f9174f45-efdd-451d-aeb5-42199601443e)

### Install the requirements.txt

-   Create a virtual environment with `python -m venv venv`
-   Activate the environment with running `venv\Scripts\activate`
-   After that install the dependencies with running
    `pip install -r /path/to/requirements.txt`

### Run the `QLearn.py` to start learning process

-   With adjusting the sleep times you can visually see the learning process.
-   After this process it will generate the q-table and saved to `q_table.json`.
-   The q-table plot and the direction values will be plotted in the screen.

### Run the `demo.py` to see the mouse is following the learned paths to eat the cheese.

-   Input a starting position in the beginning of the program.
