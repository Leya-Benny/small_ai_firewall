# AI-Powered Firewall (Demo)

This is a simple Python project that captures network packets and uses a basic machine learning model to block malicious packets.

## How It Works
- We train a machine learning model using example data.
- The firewall captures packets and checks if they are malicious using the model.
- If a packet is malicious, it is logged and blocked.

## How to Run
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Train the model:
```
python train_model.py
```

3. Run the firewall:
```
python firewall_ai.py
```

## Files
- `train_model.py`: Trains the ML model.
- `firewall_ai.py`: Captures packets and checks them with the model.
- `dataset.csv`: Sample data used to train the model.
