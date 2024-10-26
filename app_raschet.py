def create_plant():
    plants = []

    # Ask for the number of plants
    num_plants = int(input("How many Plants are in production (Not including RB)? "))

    # Iterate over the number of plants
    for n in range(1, num_plants + 1):
        # Ask for details of each plant
        volume_flow = float(input(f"What is the volume flow for Plant {n} [m3]? "))
        influent_concentration = float(input(f"What is the influent concentration for Plant {n} [mg/l]? "))
        effluent_concentration = float(input(f"What is the effluent concentration for Plant {n} [mg/l]? "))

        additional_concentration = effluent_concentration - influent_concentration

        # Create a list of the three received numbers and add to the plants list
        plant_info = [volume_flow, influent_concentration, effluent_concentration, additional_concentration]
        plants.append(plant_info)

    return plants


def calculate_rb(plants):
    sum_of_output_flows = 0.0
    sum_of_key_pollutant = 0.0

    # Iterate over each plant in the plants list
    for plant in plants:
        output_flow_volume_flow = plant[0] * 1000  # Volume flow of the plant (m3 = 1000l)
        output_flow_concentration = plant[2]  # Effluent concentration of the plant

        sum_of_output_flows += output_flow_volume_flow
        sum_of_key_pollutant += output_flow_volume_flow * output_flow_concentration

    # print(sum_of_output_flows)
    # print(sum_of_key_pollutant)

    # Calculating the parameters for RB
    volume_flow_of_incoming_RB_l = sum_of_output_flows / 2
    concentration_of_input_RB = sum_of_key_pollutant / (2 * volume_flow_of_incoming_RB_l)
    concentration_of_outgoing_RB = concentration_of_input_RB * 0.1

    rounded_concentration_of_input_RB = round(concentration_of_input_RB, 3)
    rounded_concentration_of_outgoing_RB = round(concentration_of_outgoing_RB, 3)

    volume_flow_of_incoming_RB_m = volume_flow_of_incoming_RB_l / 1000

    # Creating the Parameters_RB list
    parameters_RB = [volume_flow_of_incoming_RB_m, rounded_concentration_of_input_RB, rounded_concentration_of_outgoing_RB]

    return parameters_RB


def fill_plants(plants, parameters_RB):

    if len(plants[0]) > 6:
        i = 0
        for plant in plants:
            new_plant = [plant[1], plant[2], plant[3], plant[4], plant[5], plant[6]]
            plants[i] = new_plant
            i += 1

    sum_volume_flows_4_5_6 = 0.0

    # Updating plants 7, 8, and 9 with RB parameters
    setting_numbers = [6, 7, 8]
    sum_volume_flows_7_8_9 = 0
    for i in setting_numbers:
        plants[i][1] = parameters_RB[2]
        plants[i][2] = plants[i][1] + plants[i][3]
        plants[i][2] = round(plants[i][2], 3)
        sum_volume_flows_7_8_9 += plants[i][0]

    remaining_quantity_of_water_with_rb = parameters_RB[0] - sum_volume_flows_7_8_9

    setting_numbers = [3, 4, 5]

    # Calculating the sum of volume flows for plants 4, 5, and 6
    for i in setting_numbers:
        plant = plants[i]
        sum_volume_flows_4_5_6 += plant[0]

    # Defining variables based on RB parameters
    output_RB_concentration = parameters_RB[2]
    pure_water_concentration = 1.0

    # Calculating flows from RB and of clean water to plants 4, 5, and 6
    flow_from_RB_at_4_5_6 = flow_of_clean_water_at_4_5_6 = sum_volume_flows_4_5_6 / 2
    flow_from_RB_at_4_5_6 = round(flow_from_RB_at_4_5_6, 3)

    if remaining_quantity_of_water_with_rb >= flow_from_RB_at_4_5_6:
        # Calculating concentration at plants 4, 5, and 6
        concentration_4_5_6 = ((flow_from_RB_at_4_5_6 * output_RB_concentration) + (flow_of_clean_water_at_4_5_6 * pure_water_concentration)) / sum_volume_flows_4_5_6
        concentration_4_5_6 = round(concentration_4_5_6, 3)

        # Setting the calculated concentration and updating effluent concentration for plants 4, 5, and 6
        for i in setting_numbers:
            plants[i][1] = concentration_4_5_6
            # Assuming there is a fourth element in each plant's data for calculation
            plants[i][2] = plants[i][1] + plants[i][3]
            plants[i][2] = round(plants[i][2], 3)
    else:
        flow_from_RB_at_4_5_6 = remaining_quantity_of_water_with_rb
        flow_of_clean_water_at_4_5_6 = sum_volume_flows_4_5_6 - flow_from_RB_at_4_5_6
        concentration_4_5_6 = ((flow_from_RB_at_4_5_6 * output_RB_concentration) + (flow_of_clean_water_at_4_5_6 * pure_water_concentration)) / sum_volume_flows_4_5_6
        concentration_4_5_6 = round(concentration_4_5_6, 3)

        # Setting the calculated concentration and updating effluent concentration for plants 4, 5, and 6
        for i in setting_numbers:
            plants[i][1] = concentration_4_5_6
            # Assuming there is a fourth element in each plant's data for calculation
            plants[i][2] = plants[i][1] + plants[i][3]
            plants[i][2] = round(plants[i][2], 3)

    return plants


def calculate_conditional_concentration_installation(plants):

    for i in range(9):
        plants[i][5] = plants[i][1] * plants[i][4]
        plants[i][5] = round(plants[i][5], 3)

    return plants


# ##################################### You can create a new factory list
# plants_1 = create_plant()
# print("List of production plants: ", plants_1)

##################################### You can write your variable values in the list below
# Plant = [Rashod, conz_nach, conz_kon, dob_conz, koef_uslovn, uslovn_conz]
plants_1 = [[1.0, 1.0, 2.0, 1.0, 1.01, 0.0], [39.0, 1.0, 311.0, 310.0, 2.34, 0.0], [150.0, 1.0, 3001.0, 3000.0, 10.0, 0.0], [1.0, 1.0, 3001.0, 3000.0, 10.0, 0.0], [112.0, 1.0, 417.0, 416.0, 7.83, 0.0], [150.0, 1.0, 2.0, 1.0, 1.01, 0.0], [1.0, 1.0, 1021.0, 1020.0, 4.46, 0.0], [97.0, 1.0, 26.0, 25.0, 7.22, 0.0], [150.0, 1.0, 2514.0, 2513.0, 2.08, 0.0]]
print(plants_1)


##################################### The Beginning of programm
percentage_of_change_concentration = 100
n = 1

parameters_RB = []

while percentage_of_change_concentration > 0.001:
    if parameters_RB:
        concentration_out_of_the_rb_previous = parameters_RB[2]
    else:
        concentration_out_of_the_rb_previous = 1.0

    parameters_RB = calculate_rb(plants_1)
    print(n, parameters_RB)
    plants_filled = fill_plants(plants_1, parameters_RB)
    print(n, plants_filled)
    n += 1

    concentration_of_exhaust_from_rb = parameters_RB[2]

    percentage_of_change_concentration = ((concentration_of_exhaust_from_rb - concentration_out_of_the_rb_previous) * 100) / concentration_out_of_the_rb_previous

plants_filled_2 = calculate_conditional_concentration_installation(plants_filled)
print(plants_filled_2)

print(parameters_RB)
print(plants_filled)





