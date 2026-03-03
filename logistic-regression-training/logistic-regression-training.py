import numpy as np

def _sigmoid(z):
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    X = np.array(X)
    y = np.array(y)
    #X shapes
    n_samples, n_features = X.shape
      # Initialize parameters
    w = np.zeros(n_features)
    b = 0
    
    for step in range(steps):
        
        # Forward pass
        z = np.dot(X, w) + b
        y_hat = _sigmoid(z)
        
        # Compute gradients
        dw = (1/n_samples) * np.dot(X.T, (y_hat - y))
        db = (1/n_samples) * np.sum(y_hat - y)
        
        # Update parameters
        w -= lr * dw
        b -= lr * db
        
        # Optional: print loss
        if step % 100 == 0:
            loss = -np.mean(y*np.log(y_hat+1e-9) + (1-y)*np.log(1-y_hat+1e-9))
    return w, b