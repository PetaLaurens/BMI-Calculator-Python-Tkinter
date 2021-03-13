from tkinter import *
import csv
import datetime


root = Tk()
root.title('BMI Calculator')


def calculate_metric():
    # Valid values only, with exception handling

    # Avoiding non numbers input
    try:
        # Getting values from user
        weight_kilograms = float(entry_kilograms.get())
        height_centimeters = float(entry_centimeters.get())
    except ValueError:
        print('Input is not a number.')
        label_result['text'] = f''
        label_info['text'] = f'Please enter \npositive numbers.'
    else:
        bmi_metric = round((weight_kilograms / (height_centimeters ** 2) * 10000), 2)
        pounds_to_kilograms['text'] = ''
        inches_to_centimeters['text'] = ''
        label_result['text'] = f'BMI: {bmi_metric}'

        # Converting values
        kilograms_conversion = weight_kilograms * 2.2046226218
        kilograms_to_pounds['text'] = '%.2f' % kilograms_conversion
        centimeters_conversion = height_centimeters * 0.3937
        centimeters_to_inches['text'] = '%.2f' % centimeters_conversion

        # Displaying information
        if bmi_metric < 18.5:
            label_info['text'] = 'According to your BMI, \nyou are underweight.'
        elif (bmi_metric >= 18.5) and (bmi_metric <= 24.9):
            label_info['text'] = 'Well done! You are \na healthy weight.'
        elif (bmi_metric >= 25) and (bmi_metric <= 29.9):
            label_info['text'] = 'Your results show \nthat you are overweight.'
        elif bmi_metric >= 30:
            label_info['text'] = 'Your BMI puts you \nin the obese category.'

        # Getting user name and time
        user_name = str(entry_name.get())
        now = datetime.datetime.now()

        # Saving user information in csv file
        with open('User information.csv', 'w', newline='') as csv_file:
            field_names = ['Name', 'Height', 'Weight', 'Date']
            the_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            the_writer.writeheader()

            the_writer.writerow({'Name': user_name, 'Height': height_centimeters,
                                 'Weight': weight_kilograms, 'Date': now.strftime('%d-%m-%y %H:%M:%S')})

    # Avoiding negative numbers input
    try:
        # Getting values from user
        weight_kilograms = float(entry_kilograms.get())
        height_centimeters = float(entry_centimeters.get())
        if (weight_kilograms <= 0) or (height_centimeters <= 0):
            raise ValueError
    except ValueError:
        print('Input is not a positive number.')
        label_result['text'] = f''
        label_info['text'] = f'Please enter \npositive numbers.'
    else:
        bmi_metric = round((weight_kilograms / (height_centimeters ** 2) * 10000), 2)
        pounds_to_kilograms['text'] = ''
        inches_to_centimeters['text'] = ''
        label_result['text'] = f'BMI: {bmi_metric}'


def calculate_imperial():
    # Valid values only with exception handling

    # Avoiding non numbers input
    try:
        # Getting values from user
        weight_pounds = float(entry_pounds.get())
        height_inches = float(entry_inches.get())
    except ValueError:
        print('Input is not a number.')
        label_result['text'] = f''
        label_info['text'] = f'Please enter \npositive numbers.'
    else:
        bmi_imperial = round((weight_pounds / (height_inches * height_inches) * 703), 2)
        kilograms_to_pounds['text'] = ''
        centimeters_to_inches['text'] = ''
        label_result['text'] = f'BMI: {bmi_imperial}'

        # Converting values
        pounds_conversion = weight_pounds / 2.2046226218
        pounds_to_kilograms['text'] = '%.2f' % pounds_conversion
        inches_conversion = height_inches * 2.54
        inches_to_centimeters['text'] = '%.2f' % inches_conversion

        # Displaying information
        if bmi_imperial < 18.5:
            label_info['text'] = 'According to your BMI, \nyou are underweight.'
        elif (bmi_imperial >= 18.5) and (bmi_imperial <= 24.9):
            label_info['text'] = 'Well done! You are \na healthy weight.'
        elif (bmi_imperial >= 25) and (bmi_imperial <= 29.9):
            label_info['text'] = 'Your results show \nthat you are overweight.'
        elif bmi_imperial >= 30:
            label_info['text'] = 'Your BMI puts you \nin the obese category.'

        # Getting user name and time
        user_name = str(entry_name.get())
        now = datetime.datetime.now()

        # Saving user information in csv file
        with open('User information.csv', 'w', newline='') as csv_file:
            field_names = ['Name', 'Height', 'Weight', 'Date']
            the_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            the_writer.writeheader()

            the_writer.writerow({'Name': user_name, 'Height': height_inches,
                                 'Weight': weight_pounds, 'Date': now.strftime('%d-%m-%y %H:%M:%S')})

    # Avoiding negative numbers input
    try:
        # Getting values from user
        weight_pounds = float(entry_pounds.get())
        height_inches = float(entry_inches.get())
        if (weight_pounds <= 0) or (height_inches <= 0):
            raise ValueError
    except ValueError:
        print('Input is not a positive number.')
        label_result['text'] = f''
        label_info['text'] = f'Please enter \npositive numbers.'
    else:
        bmi_imperial = round((weight_pounds / (height_inches * height_inches) * 703), 2)
        kilograms_to_pounds['text'] = ''
        centimeters_to_inches['text'] = ''
        label_result['text'] = f'BMI: {bmi_imperial}'


# TKINTER

# User name
label_name = Label(root, text="Name: ")
label_name.grid(column=0, row=0)

entry_name = Entry(root)
entry_name.grid(column=2, row=0)

# Weight
label_kilograms = Label(root, text="Kilograms: ")
label_kilograms.grid(column=0, row=1)

entry_kilograms = Entry(root)
entry_kilograms.grid(column=2, row=1)

label_pounds = Label(root, text="Pounds: ")
label_pounds.grid(column=3, row=1)

entry_pounds = Entry(root)
entry_pounds.grid(column=5, row=1)

# Height
label_centimeters = Label(root, text="Centimeters: ")
label_centimeters.grid(column=0, row=2)

entry_centimeters = Entry(root)
entry_centimeters.grid(column=2, row=2)

label_inches = Label(root, text="Inches: ")
label_inches.grid(column=3, row=2)

entry_inches = Entry(root)
entry_inches.grid(column=5, row=2)

# Results
button_calculate_metric = Button(root, text='Calculate Metric', command=calculate_metric)
button_calculate_metric.grid(column=2, row=3)

button_calculate_imperial = Button(root, text='Calculate Imperial', command=calculate_imperial)
button_calculate_imperial.grid(column=5, row=3)

empty_line = Label(root, text="")
empty_line.grid(column=0, row=4)

label_result = Label(root, text="BMI: ")
label_result.grid(column=0, row=5)

label_info = Label(root, text="")
label_info.grid(column=0, row=6)

# Values converted

kilograms_to_pounds = Label(root, text="")
kilograms_to_pounds.grid(column=4, row=1)

centimeters_to_inches = Label(root, text="")
centimeters_to_inches.grid(column=4, row=2)

pounds_to_kilograms = Label(root, text="")
pounds_to_kilograms.grid(column=1, row=1)

inches_to_centimeters = Label(root, text="")
inches_to_centimeters.grid(column=1, row=2)


root.mainloop()
