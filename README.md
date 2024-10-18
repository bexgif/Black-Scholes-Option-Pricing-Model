# Black-Scholes-Option-Pricing-Model

This Python project implements the Black-Scholes model for pricing European-style options. It allows users to calculate the price of both call and put options based on various input parameters, and also provides a visual representation of how option prices change with respect to stock price and volatility.

## Requirements
Make sure you have the following Python libraries installed:

numpy

matplotlib

scipy

## How It Works

1. Black-Scholes Formula: The black_scholes function implements the formula to calculate the theoretical price of a call or put option:

    𝑆 = Current stock price

    𝐾 = Strike price

    𝑇 = Time to expiration (in years)

    𝑟 = Risk-free interest rate
  
    𝜎 = Volatility of the stock (standard deviation of returns)

2. Surface Plot Generation: The generate_surface_plot function creates two 3D surface plots showing the variation in call and put option prices across a range of stock prices and volatilities. The matplotlib library is used for visualisation.

3. User Input Handling: The get_user_input function gathers input from the user and then calculates the option prices, displaying the results in the console and generating the plots

## Code Overview

Black-Scholes Formula

The main function used for calculating option prices is:

![image](https://github.com/user-attachments/assets/a8ceed9a-9589-4bea-8ae6-7fcd8618efa1)


## Generating the Surface Plot
The generate_surface_plot function creates a 3D surface plot for call and put prices over a range of stock prices and volatilities:

![image](https://github.com/user-attachments/assets/55eaa4c2-3655-4987-b0fb-02132157ffa5)

## Getting User Input
The get_user_input function allows the user to interactively input the required parameters, calculates the option prices, and displays the results:

![image](https://github.com/user-attachments/assets/3e7578c8-1cdd-45f1-bd29-7f7193844ebc)

