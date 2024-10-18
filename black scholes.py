import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
   
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")

def generate_surface_plot(S, K, T, r):
    stock_prices = np.linspace(S * 0.75, S * 1.25, 20)
    volatilities = np.linspace(0.1, 0.5, 20)
   
    call_prices = np.zeros((len(stock_prices), len(volatilities)))
    put_prices = np.zeros((len(stock_prices), len(volatilities)))
   
    # Inefficient looping, calculating the same thing multiple times
    for i in range(len(stock_prices)):
        for j in range(len(volatilities)):
            call_prices[i, j] = black_scholes(stock_prices[i], K, T, r, volatilities[j], 'call')
            put_prices[i, j] = black_scholes(stock_prices[i], K, T, r, volatilities[j], 'put')
   
    stock_mesh, vol_mesh = np.meshgrid(volatilities, stock_prices)
   
    fig = plt.figure(figsize=(14, 6))
   
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(stock_mesh, vol_mesh, call_prices, cmap='viridis', edgecolor='none')
    ax1.set_title('Call Option Prices')
    ax1.set_xlabel('Volatility (σ)')
    ax1.set_ylabel('Stock Price (S)')
    ax1.set_zlabel('Call Price')
   
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(stock_mesh, vol_mesh, put_prices, cmap='plasma', edgecolor='none')
    ax2.set_title('Put Option Prices')
    ax2.set_xlabel('Volatility (σ)')
    ax2.set_ylabel('Stock Price (S)')
    ax2.set_zlabel('Put Price')
   
    plt.tight_layout()
    plt.show()

def get_user_input():
    try:
        S = float(input("Enter the current stock price (S)"))
        K = float(input("Enter the strike price (K)"))
        T = float(input("Enter the time to expiration in years (T)"))
        r = float(input("Enter the risk-free interest rate as a decimal (e.g. 0.01 for 1%)"))
        sigma = float(input("Enter the volatility as a decimal (e.g. 0.1 for 10%)"))
       
        call_price = black_scholes(S, K, T, r, sigma, 'call')
        put_price = black_scholes(S, K, T, r, sigma, 'put')
       
        print(f"\nCall option price: {call_price:.2f}")
        print(f"Put option price: {put_price:.2f}")
       
        generate_surface_plot(S, K, T, r)
   
    except ValueError as e:
        print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    get_user_input()
