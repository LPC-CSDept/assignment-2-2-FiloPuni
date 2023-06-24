def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = int(input("Enter tempertature of Celcius: "));
    fahrenheit = (9/5 * celcius) + 32;

    print(f"Celcius: {celcius}");
    print(f"Farenheit: {fahrenheit: .2f}");
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
