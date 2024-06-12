def calculate_metrics(contingency_table):
    x_and_y = contingency_table['X and Y']
    x_and_not_y = contingency_table['X and not Y']
    not_x_and_y = contingency_table['not X and Y']
    not_x_and_not_y = contingency_table['not X and not Y']
    
    N = x_and_y + x_and_not_y + not_x_and_y + not_x_and_not_y
    
    support_X_and_Y = x_and_y / N
    support_X = (x_and_y + x_and_not_y) / N
    support_Y = (x_and_y + not_x_and_y) / N
    
    confidence_X_to_Y = x_and_y / (x_and_y + x_and_not_y)
    lift_X_to_Y = confidence_X_to_Y / support_Y
    
    return {
        'support_X_and_Y': support_X_and_Y,
        'confidence_X_to_Y': confidence_X_to_Y,
        'lift_X_to_Y': lift_X_to_Y
    }

# Example contingency table
contingency_table = {
    'X and Y': 32,
    'X and not Y': 21,
    'not X and Y': 5,
    'not X and not Y': 17
}

# Calculate the metrics
metrics = calculate_metrics(contingency_table)

print("Support(X and Y): {:.4f}".format(metrics['support_X_and_Y']))
print("Confidence(X -> Y): {:.4f}".format(metrics['confidence_X_to_Y']))
print("Lift(X -> Y): {:.4f}".format(metrics['lift_X_to_Y']))
