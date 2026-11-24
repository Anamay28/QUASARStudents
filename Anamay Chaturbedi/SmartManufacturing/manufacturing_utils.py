def calculate_total_cost(production):
    total_cost = 0

    for batch in production:
        units_produced = batch[2]
        cost_per_unit = batch[4]
        total_cost += units_produced * cost_per_unit

    return total_cost


def calculate_defect_percentage(production):
    total_produced = 0
    total_defective = 0

    for batch in production:
        total_produced += batch[2]
        total_defective += batch[3]

    if total_produced == 0:
        return 0

    return (total_defective / total_produced) * 100