## Voight-Kampf test

### Check if you are a person or a replicant

1. To run the test, enter from the terminal:

        python3 main.py
2. Questions and answers to them are displayed automatically.
3. After that, you need to enter the following parameters:

    - respiration
    - heart rate
    - blushing level
    - pupillary dilation

4. If the entered data does not pass validation, it is necessary to repeat the data entry.
5. If the sum of the test points is greater than the average value, then you are a person. If less, then replicant.
6. To run the tests should be entered in the terminal, located in the root directory of the project:

         pytest
7. To create documentation, you need to install the 'Sphinx':

         python3 -m venv venv
         . venv/bin/activate
         pip install --upgrade pip
         pip install -U sphinx
8. Then, being in the 'docs' folder, you need to run the Makefile:

        make html
9. After that, open _build/html/index.html