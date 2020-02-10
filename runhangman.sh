#!/bin/bash
echo "Welcome to the First round of Mazecoders - Codefiesta" 
cat << "logo.txt" 
echo "Please Enter Name of 1 member"
read name
echo "Please Enter Number of that Member" 
read number
cd hangman
echo name >> score.txt
echo number >> score.txt


python3 hangman.py

#chmod +x runhangman.sh

