#======================================================================
#Title: Module 8.2 Assignment
#Author: Wade Eckert
#Date: 26 October 2025
#Description: This program will ask the user to enter a ticker symbol
#and will return the stock price of that ticker symbol.
#======================================================================

#Create a dictionay of 10 ticker symbols and their stock prices.
stocks = {'AAPL': 150.00, 'GOOGL': 2700.00, 'MSFT': 300.00, 'AMZN': 3300.00, 'FB': 350.00, 'TSLA': 700.00, 'NVDA': 500.00, 'AMC': 10.00, 'JNJ': 150.00, 'V': 200.00}

#Print the dictionary to the console.
print("The following ticker symbols are available for lookup:")
print(', '.join(stocks))
print()

#Define a function to search for the ticker symbol in the dictionary.
def main():
    while True:
        ticker = input("Enter a ticker symbol to look up the price for: ").upper()
        #Validate user input
        if not ticker.isalpha():
            print("\nInvalid input. Ticker symbols should only contain letters.\n")
            continue
        #If the ticker symbol is found, print the ticker symbol and the stock price.
        if ticker in stocks:
            print(f'\nThe stock price for {ticker} is ${stocks[ticker]:,.2f}\n')
            choice = input("Would you like to look up another ticker symbol? (y/n): ").lower()
            print()
            if choice == 'y':
                continue
            else:
                print("Thank you for using the stock price lookup program. Goodbye!")
                exit()
        #If the ticker symbol is not found, print a message indicating that the ticker symbol was not found.
        else:
            print(f'\nThe ticker symbol {ticker} was not found. Please try again.\n')
            continue
          
#Call the function to search for the ticker symbol in the dictionary.
main()

if __name__ == "__main__":
    main()