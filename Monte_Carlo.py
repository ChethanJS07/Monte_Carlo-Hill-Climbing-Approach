import numpy as np

def sample_A():
    return np.random.choice([0, 1], p=[0.4, 0.6])

def sample_B(A):
    if A == 0:
        return np.random.choice([0, 1], p=[0.7, 0.3])
    else:
        return np.random.choice([0, 1], p=[0.2, 0.8])

def sample_C(A):
    if A == 0:
        return np.random.choice([0, 1], p=[0.5, 0.5])
    else:
        return np.random.choice([0, 1], p=[0.4, 0.6])

def monte_carlo_inference(num_samples, evidence=None):
    target_counts = {0: 0, 1: 0}
    for _ in range(num_samples):
        A = sample_A()
        B = sample_B(A)
        C = sample_C(A)
        
        if evidence:
            if evidence.get("B") is not None and evidence["B"] != B:
                continue
            if evidence.get("C") is not None and evidence["C"] != C:
                continue
        
        target_counts[A] += 1
    
    prob_A_given_evidence = target_counts[1] / num_samples
    return prob_A_given_evidence

num_samples = int(input("Enter the no of samples: "))
evidence = {"B": 1}
probability_A_given_B_1 = monte_carlo_inference(num_samples, evidence)
print(f"Estimated P(A=1 | B=1) using Monte Carlo: {probability_A_given_B_1}")