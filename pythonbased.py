import math
weight_per_leg= 250 
weight_per_wing = 250 
weight_per_flesh= 1000
chicken_weight = 2000
def solve_chicken_problem(legs, wings, flesh):
    chickens_needed_legs = math.ceil(legs / 2)
    chickens_needed_wings = math.ceil(wings / 2)
    chickens_needed_flesh = flesh
    chickens_needed = max(chickens_needed_legs, chickens_needed_wings, chickens_needed_flesh)
    total_legs = chickens_needed * 2
    total_wings = chickens_needed * 2
    total_flesh = chickens_needed * 1
    remaining_legs = total_legs - legs
    remaining_wings = total_wings - wings
    remaining_flesh = total_flesh - flesh
    order_weight = (legs * weight_per_leg) + (wings * weight_per_wing) + (flesh * weight_per_flesh)
    remaining_weight = (remaining_legs * weight_per_leg) + (remaining_wings *weight_per_wing ) + (remaining_flesh * weight_per_flesh)
    print("\n--- Chicken Order Summary ---")
    print(f"Total Order Weight      : {order_weight / 1000:.2f} kg")
    print(f"Chickens Needed         : {chickens_needed}")
    print(f"Remaining Legs          : {remaining_legs}")
    print(f"Remaining Wings         : {remaining_wings}")
    print(f"Remaining Flesh Portions: {remaining_flesh}")
    print(f"Remaining Inventory Wt  : {remaining_weight / 1000:.2f} kg")
if __name__ == "__main__":
    print("Enter customer order details:")
    legs = int(input("Number of legs required: "))
    wings = int(input("Number of wings required: "))
    flesh = int(input("Number of flesh portions required: "))
    solve_chicken_problem(legs, wings, flesh)
