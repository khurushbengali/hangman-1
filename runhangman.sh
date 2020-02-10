#!/bin/bash
echo "Welcome to the First round of Mazecoders - Codefiesta" 
cat "logo.txt" 
echo "Please Enter Name of 1st member"
read name
echo "Please Enter the Number of that member" 
read number
cd hangman
echo name >> score.txt
echo number >> score.txt


python3 hangman.py

#chmod +x runhangman.sh

