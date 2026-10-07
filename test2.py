import random

def main():
     print("Khansole Academy")
    # TODO: your code here
    
     first = random.randint(1, 100)
     second = random.randint(1, 100)
     sum = first + second
     print(f"What is {first} + {second}?")
     ans = int(input())
     if ans == sum:
         print("Correct!")
     else:
         print(f"Incorrect. The correct answer is {sum}.")
     
    



if __name__ == "__main__":
    main()
