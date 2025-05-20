import matplotlib.pyplot as plt

# ELBO values per epoch
elbo_values = [
    -2.220131e+02, -1.934818e+02, -1.805705e+02, -1.664317e+02, -1.548852e+02,
    -1.463868e+02, -1.390776e+02, -1.343981e+02, -1.303842e+02, -1.261567e+02,
    -1.228824e+02, -1.205947e+02, -1.190836e+02, -1.177239e+02, -1.167119e+02,
    -1.159205e+02, -1.151034e+02, -1.143162e+02, -1.135846e+02, -1.129953e+02,
    -1.124856e+02, -1.117956e+02, -1.110689e+02, -1.106104e+02, -1.102020e+02,
    -1.098817e+02, -1.094777e+02, -1.092068e+02, -1.088990e+02, -1.087090e+02
]

# Epoch indices
epochs = list(range(len(elbo_values)))

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(epochs, elbo_values, marker='o')
plt.title('ELBO Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('ELBO')
plt.grid(True)
plt.tight_layout()
plt.show()