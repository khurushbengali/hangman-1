#!/bin/bash
echo "Welcome to the First round of Mazecoders - Codefiesta" 
cat "logo.txt"

echo "Rules:"
echo "1. Press Backspace for Hints. DO NOT PRESS it MORE THAN ONCE"
echo "2. You have 10 minutes in total from the start of the game."
echo "3. +2 for correct answer. -2 for wrong and -1 for taking a hint."
echo "4. Each word will have 10 lives you can see visually"
echo "5. Please do not use mousekeys or any other shortcuts that can damage your progress"
echo "6.You do not need to press enter"
echo "7. Only acceptable keypresses are alphabets and Backspace(hints)"
echo "8. Afrer completion of the time, call a coordinator to record your score."
echo ""
echo ""
echo ""
echo "Please Enter Name of 1st member"
read name
echo "Please Enter the Phone Number of that member" 
read number
echo "Type start to start the game"
read start
if[ $start == "start" ]
  cd hangman
  echo "$name" >> score.txt
  echo "$number" >> score.txt
  python3 hangman.py
  echo "Lol"
#chmod +x runhangman.sh

