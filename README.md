# Google-Forms-Spammer

NOTE: This program only works with Google Forms that don't require you to sign in.

This is the link to the sample form I have created to test out the code.
https://docs.google.com/forms/d/e/1FAIpQLSfxx3IIT6geNAFPA-VwvHXnsVs1UQMKKDZjgQ7bb7x3G71yjA/viewform?usp=sf_link

## Installation

Install requests package using following command

```sh
$ pip3 install requests
```

## Usage

1. Goto the google form you want to spam.
2. Change Form ID in the code with the form ID of your form.
2. Right-click & select view page source.
3. In find dialog, enter 'entry' without the quotes.
4. Replace entery numbers in the code with one you found in the page source code.  (For e.g. entry.2005620554)
5. Modify the code as per the fields in your form. Also change the names to your desire.
6. Run the code and enjoy.
