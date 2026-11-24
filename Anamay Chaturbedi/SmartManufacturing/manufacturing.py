# Smart Manufacturing System
# Each tuple: (Batch_ID, Product_Name, Units_Produced, Defective_Units, Cost_Per_Unit)
from manufacturing_utils import calculate_total_cost, calculate_defect_percentage
production = [
    (501, "Circuiti Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]

print("Initial production records:")
for batch in production:
    print(batch)

try:
    batch_id = int(input("Enter Batch ID: "))
    product_name = input("Enter Product Name: ")
    units_produced = int(input("Enter Units Produced: "))
    defective_units = int(input("Enter Defective Units: "))
    cost_per_unit = float(input("Enter Cost Per Unit: "))

    if units_produced < 0 or defective_units < 0 or cost_per_unit < 0:
        print("Values cannot be negative.")

    elif defective_units > units_produced:
        print("Defective units cannot be greater than units produced.")

    else:
        new_batch = (
            batch_id,
            product_name,
            units_produced,
            defective_units,
            cost_per_unit
        )

        production.append(new_batch)
        print("New production batch added successfully.")

except ValueError:
    print("Invalid input. Please enter numbers where required.")

else:
    print("Input process completed.")

finally:
    print("Smart Manufacturing System finished input process.")
    total_cost = calculate_total_cost(production)
defect_percentage = calculate_defect_percentage(production)

print("\n--- Manufacturing Report ---")
print("Total Manufacturing Cost:", total_cost)
print("Overall Defect Percentage:", defect_percentage, "%")
# Batches with more than 10 defective units
high_defect_batches = list(filter(lambda batch: batch[3] > 10, production))

print("\nBatches with more than 10 defective units:")
for batch in high_defect_batches:
    print(batch)

# Accepted production quantities
accepted_quantities = list(map(lambda batch: batch[2] - batch[3], production))

print("\nAccepted production quantities:")
print(accepted_quantities)

# Manufacturing cost for each batch
batch_costs = list(map(lambda batch: batch[2] * batch[4], production))

print("\nManufacturing cost of each batch:")
print(batch_costs)