#Stock Checker

## Purpose
After the PS5 was released in Novemeber, the stocks quickly ran out. The scripts in this repo when run will check for stocks of the PS5. This is a command line tool which on finding available stock will notify the user with the links to purchase online.

This is for anyone who is looking for PS5 availibility online and this gives direct control for a user/buyer over the traditional email notifications on stock availability.

There are 3 scripts that work together to check availability for a product(in this case the PS5). Initially, based on the url in the main script, data is scrapped that contains info on stock availablity and if any stock is found, the subsequent is run that generates a desktop GUI which acts as a notification (audio and visual) presenting the user with the product details and links for purchase.

###Note:
Every 10 minutes, the product availability is checked. This can be modified in the main.py file.

## Instructions
Run the following to run the scripts.
```shellscript

pip install -r requirements.txt
python main.py

```

## GUI Screen Grab
![image](<image src="./notification.png" alt="notification"/>)