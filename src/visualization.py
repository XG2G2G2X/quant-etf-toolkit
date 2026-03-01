import matplotlib.pyplot as plt

def plot_prices(data):
    data.plot(figsize=(10,6))
    plt.title("ETF Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()
