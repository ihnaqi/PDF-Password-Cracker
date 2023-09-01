# PDF Password Cracker

I coded this script to open one of my PDF file whose password I forgot, the one thing taht I knew was the length of the password was five digits long, so I generated all the permutation of five digit numbers and tried them on my document. In your case it might be different you can make changes accordingly I have placed comments there so that you can change them according to you need.

## Step 1

Make sure you change this line of code

```python
pdf_file = "<<filename.pdf>>"
```

in the above line of code change `<<filename.pdf>>` with that of the name of your _pdf_ file.

## Step 2

Change the following line on line number _19_ with the file containing you password, randomly generated or copied from the intenet.

```python
passwords = []
```

## Step 3

Run the script and wait for the magic to happen.
