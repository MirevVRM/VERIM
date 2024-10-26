def create_list_plants():
    plants = []

    # Ask for the number of plants
    num_plants = int(input("How many Plants are in production (Not including RB)? "))

    # Iterate over the number of plants
    for n in range(1, num_plants + 1):

        volume_flow = float(input(f"What is the volume flow for Plant {n} [m3/h]? "))
        influent_concentration = float(input(f"What is the influent concentration for Plant {n} [mg/l]? "))
        effluent_concentration = float(input(f"What is the effluent concentration for Plant {n} [mg/l]? "))
        maximum_concentration_of_inbound_flow = float(input(f"What is the maximum concentration of the incoming flow for Plant {n} [mg/l]? ")) # Conditional concentration

        additional_concentration = effluent_concentration - influent_concentration

        plant_info = [volume_flow, influent_concentration, effluent_concentration, additional_concentration, maximum_concentration_of_inbound_flow]
        plants.append(plant_info)

    # Parametrs of RB
    volume_flow_rb = float(input("What is the volume flow for RB [m3/h]? "))
    influent_concentration_rb = float(input("What is the influent concentration for RB [mg/l]? "))
    effluent_concentration_rb = float(input("What is the effluent concentration for RB [mg/l]? "))

    user_response = str(input("Do you want to do a calculation of the remaining RB concentration factor? (Write True or False) ")) # True or False
    if user_response == "True":
        remaining_concentration_factor = effluent_concentration_rb / influent_concentration_rb
    elif user_response == "False":
        remaining_concentration_factor = float(input("What is the coefficient of the remaining concentration for RB [-]? "))
    else:
        print("Your answer was not recognized (No True or False was found in the answer)")
        remaining_concentration_factor = 1 # 100% => influent_concentration_rb = effluent_concentration_rb
    print(remaining_concentration_factor)

    max_volume_flow_rb = float(input("What is the maximum volume flow for RB [m3/h]? "))

    parametrs_rb = [volume_flow_rb, influent_concentration_rb, effluent_concentration_rb, remaining_concentration_factor, max_volume_flow_rb]
    print(parametrs_rb)

    # Parametrs of fresh water
    volume_consumption_of_fresh_water = float(input("What is the amount of fresh water used [m3/h]? "))
    fresh_water_concentration = float(input("What is the concentration of fresh water [mg/l]? "))

    parametrs_fresh_water = [volume_consumption_of_fresh_water, fresh_water_concentration]

    return plants, parametrs_rb, parametrs_fresh_water


def optimization_flows_plants(plants, parametrs_rb, parametrs_fresh_water):

    num_plant = 1
    table_1 = []
    table_2 = []
    table_4 = []

    # table_1
    for plant_info in plants:
        new_plant_info_for_table_1 = [num_plant, plant_info[0], plant_info[4], plant_info[3]]
        table_1.append(new_plant_info_for_table_1)

        num_plant += 1

    # table_2
    num_plant = 1
    for plant_info in plants:
        new_plant_info_for_table_2 = [num_plant, plant_info[0], plant_info[2]]
        table_2.append(new_plant_info_for_table_2)

        num_plant += 1

    table_2_sorted = sorted(table_2, key=lambda item: item[2], reverse=True)

    # table_3
    new_info_rb = [parametrs_rb[0], parametrs_rb[2]]
    new_info_fresh_water = [parametrs_fresh_water[0], parametrs_fresh_water[1]]
    table_3 = [new_info_rb, new_info_fresh_water]

    # start optimization
    ostatok = 0
    number_digits_after_the_comma = 5
    for plant in table_1:
        number_of_iteration = 0
        #print(f"{plant[0]} итерация ...")
        #print(f"Параметры установки: {plant}")
        #print(f"Для установки {plant[0]} запускаю процесс оптимизации")

        for stream in table_2_sorted:
            #print(f"{number_of_iteration} итерация вложенного цикла ...")
            #print(f"Параметры потока: {stream}")

            if stream[1] > 0:
                #print(f"stream[1] > 0: {stream[1]} > 0")

                if stream[2] < plant[2]:  # First
                    #print(f"1 stream[2] < plant[2] # First: {stream[1]} < {plant[2]}")

                    if ostatok > 0:
                        #print(f"1.1 ostatok > 0: {ostatok} > 0")

                        if stream[1] > ostatok:
                            #print(f"1.1.1 stream[1] > ostatok: {stream[1]} > {ostatok}")
                            table_2_sorted[number_of_iteration][1] = round(stream[1] - ostatok, number_digits_after_the_comma)
                            stream_for_table_4 = [stream[0], ostatok, stream[2]]
                            ostatok = 0
                            index_of_plant = plant[0] - 1
                            table_4[index_of_plant][1].append(stream_for_table_4)
                            break

                        elif stream[1] == ostatok:
                            #print(f"1.1.2 stream[1] == ostatok: {stream[1]} = {ostatok}")
                            table_2_sorted[number_of_iteration][1] = 0
                            stream_for_table_4 = [stream[0], ostatok, stream[2]]
                            ostatok = 0
                            index_of_plant = plant[0] - 1
                            table_4[index_of_plant][1].append(stream_for_table_4)
                            break

                        elif stream[1] < ostatok:
                            #print(f"1.1.3 stream[1] < ostatok: {stream[1]} < {ostatok}")
                            table_2_sorted[number_of_iteration][1] = 0
                            stream_for_table_4 = [stream[0], stream[1], stream[2]]
                            ostatok = round(ostatok - stream[1], number_digits_after_the_comma)
                            index_of_plant = plant[0] - 1
                            table_4[index_of_plant][1].append(stream_for_table_4)

                    elif stream[1] > plant[1]:
                        #print(f"1.2 stream[1] > plant[1]: {stream[1]} > {plant[1]}")
                        table_2_sorted[number_of_iteration][1] = round(stream[1] - plant[1], number_digits_after_the_comma)
                        stream_for_table_4 = [plant[0], [[stream[0], plant[1], stream[2]]]]
                        table_4.append(stream_for_table_4)
                        break

                    elif stream[1] == plant[1]:
                        #print(f"1.3 stream[1] == plant[1]: {stream[1]} = {plant[1]}")
                        table_2_sorted[number_of_iteration][1] = 0
                        stream_for_table_4 = [plant[0], [[stream[0], plant[1], stream[2]]]]
                        table_4.append(stream_for_table_4)
                        break

                    elif stream[1] < plant[1]:
                        #print(f"1.4 stream[1] < plant[1]: {stream[1]} < {plant[1]}")
                        table_2_sorted[number_of_iteration][1] = 0
                        stream_for_table_4 = [plant[0], [[stream[0], stream[1], stream[2]]]]
                        ostatok = round(plant[1] - stream[1], number_digits_after_the_comma)
                        table_4.append(stream_for_table_4)

                ###############################################################################################################
                elif stream[2] == plant[2]:  # Second
                    #print(f"2 stream[2] == plant[2]: {stream[2]} = {plant[2]}")

                    if ostatok > 0:
                        #print(f"2.1 ostatok > 0: {ostatok} > 0")

                        if stream[1] > ostatok:
                            #print(f"2.1.1 stream[1] > ostatok: {stream[1]} > {ostatok}")
                            table_2_sorted[number_of_iteration][1] = round(stream[1] - ostatok, number_digits_after_the_comma)
                            stream_for_table_4 = [stream[0], ostatok, stream[2]]
                            ostatok = 0
                            index_of_plant = plant[0] - 1
                            table_4[index_of_plant][1].append(stream_for_table_4)
                            break

                        elif stream[1] == ostatok:
                            #print(f"2.1.2 stream[1] == ostatok: {stream[1]} = {ostatok}")
                            table_2_sorted[number_of_iteration][1] = 0
                            stream_for_table_4 = [stream[0], ostatok, stream[2]]
                            ostatok = 0
                            index_of_plant = plant[0] - 1
                            table_4[index_of_plant][1].append(stream_for_table_4)
                            break

                        elif stream[1] < ostatok:
                            #print(f"2.1.3 stream[1] < ostatok: {stream[1]} < {ostatok}")
                            table_2_sorted[number_of_iteration][1] = 0
                            stream_for_table_4 = [stream[0], stream[1], stream[2]]
                            ostatok = round(ostatok - stream[1], number_digits_after_the_comma)
                            index_of_plant = plant[0] - 1
                            table_4[index_of_plant][1].append(stream_for_table_4)

                    elif stream[1] > plant[1]:
                        #print(f"2.2 stream[1] > plant[1]: {stream[1]} > {plant[1]}")
                        table_2_sorted[number_of_iteration][1] = round(stream[1] - plant[1], number_digits_after_the_comma)
                        stream_for_table_4 = [plant[0], [[stream[0], plant[1], stream[2]]]]
                        table_4.append(stream_for_table_4)
                        break

                    elif stream[1] == plant[1]:
                        #print(f"2.3 stream[1] == plant[1]: {stream[1]} = {plant[1]}")
                        table_2_sorted[number_of_iteration][1] = 0
                        stream_for_table_4 = [plant[0], [[stream[0], plant[1], stream[2]]]]
                        table_4.append(stream_for_table_4)
                        break

                    elif stream[1] < plant[1]:
                        #print(f"2.4 stream[1] < plant[1]: {stream[1]} < {plant[1]}")
                        table_2_sorted[number_of_iteration][1] = 0
                        stream_for_table_4 = [plant[0], [[stream[0], stream[1], stream[2]]]]
                        ostatok = round(plant[1] - stream[1], number_digits_after_the_comma)
                        table_4.append(stream_for_table_4)

                ################################################################################################################
                elif stream[2] > plant[2]:  # Third
                    #print(f"3 stream[2] > plant[2]: {stream[2]} > {plant[2]}")

                    if ostatok > 0:
                        #print(f"3.1 ostatok > 0: {ostatok} > 0")

                        if table_3[0][1] < plant[2]:  # Using water from RB
                            #print(f"3.1.1 table_3[0][1] < plant[2]: {table_3[0][1]} < {plant[2]}")
                            required_volume_flow_rate_from_table_3 = round(ostatok * (plant[2] - stream[2]) / (table_3[0][1] - stream[2]), number_digits_after_the_comma)
                            required_volume_flow_rate_from_table_2 = round(ostatok - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                            #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)
                            #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                            if table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.1 table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2: {table_3[0][0]} > {required_volume_flow_rate_from_table_3} and {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.2 table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2: {table_3[0][0]} = {required_volume_flow_rate_from_table_3} and {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[0][0] = 0
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.3 table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2: {table_3[0][0]} < {required_volume_flow_rate_from_table_3} and {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_2 = round(table_3[0][0] * (table_3[0][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[0][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["RB", table_3[0][0], table_3[0][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_3[0][0] = 0
                                #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                            elif table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.4 table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2: {table_3[0][0]} > {required_volume_flow_rate_from_table_3} and {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.5 table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2: {table_3[0][0]} = {required_volume_flow_rate_from_table_3} and {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = 0
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.6 table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2: {table_3[0][0]} < {required_volume_flow_rate_from_table_3} and {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_2 = round(table_3[0][0] * (table_3[0][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[0][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["RB", table_3[0][0], table_3[0][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_3[0][0] = 0
                                #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                            elif table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.7 table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2: {table_3[0][0]} > {required_volume_flow_rate_from_table_3} and {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[0][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], stream[1], stream[2]]
                                stream_for_table_4_2 = ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)

                            elif table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.8 table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2: {table_3[0][0]} = {required_volume_flow_rate_from_table_3} and {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[0][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], stream[1], stream[2]]
                                stream_for_table_4_2 = ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)

                            elif table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                #print(f"3.1.1.9 table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2: {table_3[0][0]} < {required_volume_flow_rate_from_table_3} and {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_2 = round(table_3[0][0] * (table_3[0][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[0][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                                if stream[1] > required_volume_flow_rate_from_table_2:
                                    #print(f"3.1.1.9.1 stream[1] > required_volume_flow_rate_from_table_2: {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                    ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                    stream_for_table_4_2 = ["RB", table_3[0][0], table_3[0][1]]
                                    index_of_plant = plant[0] - 1
                                    table_4[index_of_plant][1].append(stream_for_table_4_1)
                                    table_4[index_of_plant][1].append(stream_for_table_4_2)
                                    table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                    table_3[0][0] = 0

                                elif stream[1] == required_volume_flow_rate_from_table_2:
                                    #print(f"3.1.1.9.2 stream[1] == required_volume_flow_rate_from_table_2: {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                    ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                    stream_for_table_4_2 = ["RB", table_3[0][0], table_3[0][1]]
                                    index_of_plant = plant[0] - 1
                                    table_4[index_of_plant][1].append(stream_for_table_4_1)
                                    table_4[index_of_plant][1].append(stream_for_table_4_2)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[0][0] = 0

                                elif stream[1] < required_volume_flow_rate_from_table_2:
                                    #print(f"3.1.1.9.3 stream[1] < required_volume_flow_rate_from_table_2: {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                    required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[0][1] - plant[2]), number_digits_after_the_comma)
                                    non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                    ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4_1 = [stream[0], stream[1], stream[2]]
                                    stream_for_table_4_2 = ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]
                                    index_of_plant = plant[0] - 1
                                    table_4[index_of_plant][1].append(stream_for_table_4_1)
                                    table_4[index_of_plant][1].append(stream_for_table_4_2)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                    #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)

                        ###################################################################################################
                        else:  # Using Fresh water
                            #print(f"3.1.2 table_3[0][1] !< plant[2]: {table_3[1][1]} !< {plant[2]}")
                            required_volume_flow_rate_from_table_3 = round(ostatok * (plant[2] - stream[2]) / (table_3[1][1] - stream[2]), number_digits_after_the_comma)
                            required_volume_flow_rate_from_table_2 = round(ostatok - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                            #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)
                            #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                            if table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.1 table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2: {table_3[1][0]} > {required_volume_flow_rate_from_table_3} and {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.2 table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2: {table_3[1][0]} = {required_volume_flow_rate_from_table_3} and {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[1][0] = 0
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.3 table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2: {table_3[1][0]} < {required_volume_flow_rate_from_table_3} and {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_2 = round(table_3[1][0] * (table_3[1][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[1][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["FW", table_3[1][0], table_3[1][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_3[1][0] = 0
                                #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                            elif table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.4 table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2: {table_3[1][0]} > {required_volume_flow_rate_from_table_3} and {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.5 table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2: {table_3[1][0]} = {required_volume_flow_rate_from_table_3} and {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = 0
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]
                                ostatok = 0
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                break

                            elif table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.6 table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2: {table_3[1][0]} < {required_volume_flow_rate_from_table_3} and {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_2 = round(table_3[1][0] * (table_3[1][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[1][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2, stream[2]]
                                stream_for_table_4_2 = ["FW", table_3[1][0], table_3[1][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_3[1][0] = 0
                                #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                            elif table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.7 table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2: {table_3[1][0]} > {required_volume_flow_rate_from_table_3} and {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[1][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], stream[1], stream[2]]
                                stream_for_table_4_2 = ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)

                            elif table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.8 table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2: {table_3[1][0]} = {required_volume_flow_rate_from_table_3} and {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[1][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4_1 = [stream[0], stream[1], stream[2]]
                                stream_for_table_4_2 = ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]
                                index_of_plant = plant[0] - 1
                                table_4[index_of_plant][1].append(stream_for_table_4_1)
                                table_4[index_of_plant][1].append(stream_for_table_4_2)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)

                            elif table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                #print(f"3.1.2.9 table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2: {table_3[1][0]} < {required_volume_flow_rate_from_table_3} and {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                required_volume_flow_rate_from_table_2 = round(table_3[1][0] * (table_3[1][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[1][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                                if stream[1] > required_volume_flow_rate_from_table_2:
                                    #print(f"3.1.2.9.1 stream[1] > required_volume_flow_rate_from_table_2: {stream[1]} > {required_volume_flow_rate_from_table_2}")
                                    ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2,stream[2]]
                                    stream_for_table_4_2 = ["FW", table_3[1][0], table_3[1][1]]
                                    index_of_plant = plant[0] - 1
                                    table_4[index_of_plant][1].append(stream_for_table_4_1)
                                    table_4[index_of_plant][1].append(stream_for_table_4_2)
                                    table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                    table_3[1][0] = 0

                                elif stream[1] == required_volume_flow_rate_from_table_2:
                                    #print(f"3.1.2.9.2 stream[1] == required_volume_flow_rate_from_table_2: {stream[1]} = {required_volume_flow_rate_from_table_2}")
                                    ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4_1 = [stream[0], required_volume_flow_rate_from_table_2,stream[2]]
                                    stream_for_table_4_2 = ["FW", table_3[1][0], table_3[1][1]]
                                    index_of_plant = plant[0] - 1
                                    table_4[index_of_plant][1].append(stream_for_table_4_1)
                                    table_4[index_of_plant][1].append(stream_for_table_4_2)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[1][0] = 0

                                elif stream[1] < required_volume_flow_rate_from_table_2:
                                    #print(f"3.1.2.9.3 stream[1] < required_volume_flow_rate_from_table_2: {stream[1]} < {required_volume_flow_rate_from_table_2}")
                                    required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[1][1] - plant[2]), number_digits_after_the_comma)
                                    non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                    ostatok = round(ostatok - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4_1 = [stream[0], stream[1], stream[2]]
                                    stream_for_table_4_2 = ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]
                                    index_of_plant = plant[0] - 1
                                    table_4[index_of_plant][1].append(stream_for_table_4_1)
                                    table_4[index_of_plant][1].append(stream_for_table_4_2)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                    #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)

                    #########################################################################################################################
                    else:
                        #print(f"3.2 ostatok !> 0: {ostatok} !> 0")

                        if table_3[0][1] < plant[2]:  # Using water from RB
                            #print(f"3.2.1 table_3[0][1] < plant[2]: {table_3[0][1]} < {plant[2]}")
                            required_volume_flow_rate_from_table_3 = round(plant[1] * (plant[2] - stream[2]) / (table_3[0][1] - stream[2]), number_digits_after_the_comma)
                            required_volume_flow_rate_from_table_2 = round(plant[1] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                            #print("required_volume_flow_rate_from_table_3 = ", required_volume_flow_rate_from_table_3)
                            #print("required_volume_flow_rate_from_table_2 = ", required_volume_flow_rate_from_table_2)

                            if table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[0][0] = 0
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_2 = round(table_3[0][0] * (table_3[0][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[0][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", table_3[0][0], table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                table_3[0][0] = 0

                            elif table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = 0
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_2 = round(table_3[0][0] * (table_3[0][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[0][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", table_3[0][0], table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                table_3[0][0] = 0

                            elif table_3[0][0] > required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[0][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], round(stream[1], number_digits_after_the_comma), stream[2]], ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)

                            elif table_3[0][0] == required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[0][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], round(stream[1], number_digits_after_the_comma), stream[2]], ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]]]
                                table_4.append(stream_for_table_4)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)

                            elif table_3[0][0] < required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_2 = round(table_3[0][0] * (table_3[0][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[0][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)

                                if stream[1] > required_volume_flow_rate_from_table_2:
                                    ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                    table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                    stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", table_3[0][0], table_3[0][1]]]]
                                    table_4.append(stream_for_table_4)
                                    table_3[0][0] = 0

                                elif stream[1] == required_volume_flow_rate_from_table_2:
                                    ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["RB", table_3[0][0], table_3[0][1]]]]
                                    table_4.append(stream_for_table_4)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[0][0] = 0

                                elif stream[1] < required_volume_flow_rate_from_table_2:
                                    required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[0][1] - plant[2]), number_digits_after_the_comma)
                                    non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                    ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4 = [plant[0], [[stream[0], stream[1], stream[2]], ["RB", required_volume_flow_rate_from_table_3, table_3[0][1]]]]
                                    table_4.append(stream_for_table_4)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[0][0] = round(table_3[0][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)

                        ###################################################################################################
                        else:  # Using Fresh water
                            required_volume_flow_rate_from_table_3 = round(plant[1] * (plant[2] - stream[2]) / (table_3[1][1] - stream[2]), number_digits_after_the_comma)
                            required_volume_flow_rate_from_table_2 = round(plant[1] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)

                            if table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                table_3[1][0] = 0
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] > required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_2 = round(table_3[1][0] * (table_3[1][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[1][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", table_3[1][0], table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                table_3[1][0] = 0

                            elif table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = 0
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                break

                            elif table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] == required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_2 = round(table_3[1][0] * (table_3[1][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[1][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", table_3[1][0], table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                table_3[1][0] = 0

                            elif table_3[1][0] > required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[1][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], stream[1], stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)

                            elif table_3[1][0] == required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[1][1] - plant[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                stream_for_table_4 = [plant[0], [[stream[0], stream[1], stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]
                                table_4.append(stream_for_table_4)
                                table_2_sorted[number_of_iteration][1] = 0
                                table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)

                            elif table_3[1][0] < required_volume_flow_rate_from_table_3 and stream[1] < required_volume_flow_rate_from_table_2:
                                required_volume_flow_rate_from_table_2 = round(table_3[1][0] * (table_3[1][1] - plant[2]) / (plant[2] - stream[2]), number_digits_after_the_comma)
                                non_full_volume_consumption = round(table_3[1][0] + required_volume_flow_rate_from_table_2, number_digits_after_the_comma)

                                if stream[1] > required_volume_flow_rate_from_table_2:
                                    ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                    table_2_sorted[number_of_iteration][1] = round(stream[1] - required_volume_flow_rate_from_table_2, number_digits_after_the_comma)
                                    stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", table_3[1][0], table_3[1][1]]]]
                                    table_4.append(stream_for_table_4)
                                    table_3[1][0] = 0

                                elif stream[1] == required_volume_flow_rate_from_table_2:
                                    ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4 = [plant[0], [[stream[0], required_volume_flow_rate_from_table_2, stream[2]], ["FW", table_3[1][0], table_3[1][1]]]]
                                    table_4.append(stream_for_table_4)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[1][0] = 0

                                elif stream[1] < required_volume_flow_rate_from_table_2:
                                    required_volume_flow_rate_from_table_3 = round(stream[1] * (plant[2] - stream[2]) / (table_3[1][1] - plant[2]), number_digits_after_the_comma)
                                    non_full_volume_consumption = round(stream[1] + required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
                                    ostatok = round(plant[1] - non_full_volume_consumption, number_digits_after_the_comma)
                                    stream_for_table_4 = [plant[0], [[stream[0], stream[1], stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]
                                    table_4.append(stream_for_table_4)
                                    table_2_sorted[number_of_iteration][1] = 0
                                    table_3[1][0] = round(table_3[1][0] - required_volume_flow_rate_from_table_3, number_digits_after_the_comma)

                else:
                    print("PUPUPUP")

            number_of_iteration += 1

########################################################################################################################
        if ostatok != 0: # Zelenoe uslovie FRESH WATER OR RB
            if table_3[0][1] < plant[2] and table_3[0][0] >= ostatok:
                stream_for_table_4 = ["RB", ostatok, table_3[0][1]]
                index_of_plant = plant[0] - 1
                table_4[index_of_plant][1].append(stream_for_table_4)
                table_3[0][0] = round(table_3[0][0] - ostatok, number_digits_after_the_comma)
                ostatok = 0

            elif table_3[0][1] < plant[2] and table_3[0][0] < ostatok:
                stream_for_table_4 = ["RB", table_3[0][0], table_3[0][1]]
                index_of_plant = plant[0] - 1
                table_4[index_of_plant][1].append(stream_for_table_4)
                ostatok = round(ostatok - table_3[0][0], number_digits_after_the_comma)
                table_3[0][0] = 0
                stream_for_table_4 = ["FW", ostatok, table_3[1][1]]
                table_4[index_of_plant][1].append(stream_for_table_4)
                table_3[1][0] = round(table_3[1][0] - ostatok, number_digits_after_the_comma)
                ostatok = 0

            elif table_3[0][1] == plant[2] and table_3[0][0] >= ostatok:
                stream_for_table_4 = ["RB", ostatok, table_3[0][1]]
                index_of_plant = plant[0] - 1
                table_4[index_of_plant][1].append(stream_for_table_4)
                table_3[0][0] = round(table_3[0][0] - ostatok, number_digits_after_the_comma)
                ostatok = 0

            elif table_3[0][1] == plant[2] and table_3[0][0] < ostatok:
                stream_for_table_4 = ["RB", table_3[0][0], table_3[0][1]]
                index_of_plant = plant[0] - 1
                table_4[index_of_plant][1].append(stream_for_table_4)
                ostatok = round(ostatok - table_3[0][0], number_digits_after_the_comma)
                table_3[0][0] = 0
                stream_for_table_4 = ["FW", ostatok, table_3[1][1]]
                table_4[index_of_plant][1].append(stream_for_table_4)
                table_3[1][0] = round(table_3[1][0] - ostatok, number_digits_after_the_comma)
                ostatok = 0

            else:
                stream_for_table_4 = ["FW", ostatok, table_3[1][1]]
                index_of_plant = plant[0] - 1
                table_4[index_of_plant][1].append(stream_for_table_4)
                table_3[1][0] = round(table_3[1][0] - ostatok, number_digits_after_the_comma)
                ostatok = 0

    ####################################################################################################################
    print("Осталось потоков от РБ и Чистой воды: ", table_3)
    table_2_sorted = sorted(table_2_sorted, key=lambda item: item[0])

    # Calculation of new RB parameters
    sum_of_output_flows = 0
    sum_of_key_pollutant = 0

    # num_plants = len(table_2_sorted)

    for stream in table_2_sorted:
        output_flow_volume = round(stream[1] * 1000, number_digits_after_the_comma)  # Volume flow of the plant (m3 = 1000l)
        output_flow_concentration = stream[2]  # Effluent concentration of the plant

        sum_of_output_flows = round(sum_of_output_flows + output_flow_volume, number_digits_after_the_comma)
        sum_of_key_pollutant = round(sum_of_key_pollutant + (output_flow_volume * output_flow_concentration), number_digits_after_the_comma)

    sum_of_output_flows_m3 = round(sum_of_output_flows / 1000, number_digits_after_the_comma)  # (m3 = 1000l)
    concentration_of_key_pollutant_sum = round(sum_of_key_pollutant / sum_of_output_flows, number_digits_after_the_comma)
    print(f"Суммарный объёмный расход и концентрация: {sum_of_output_flows_m3} m3/h, {concentration_of_key_pollutant_sum} mg/l")

    if sum_of_output_flows_m3 > parametrs_rb[4]:
        volume_flow_of_incoming_RB_m = parametrs_rb[4]
        volume_flow_of_incoming_RB_l = round(volume_flow_of_incoming_RB_m * 1000, number_digits_after_the_comma) #  (m3 = 1000l)
        volumetric_discharge_flow_rate = round(sum_of_output_flows_m3 - parametrs_rb[4], number_digits_after_the_comma)
        concentration_of_input_RB = concentration_of_key_pollutant_sum
        concentration_of_outgoing_RB = round(concentration_of_input_RB * parametrs_rb[3], number_digits_after_the_comma)
        parametrs_rb[0] = volume_flow_of_incoming_RB_m
        parametrs_rb[1] = concentration_of_input_RB
        parametrs_rb[2] = concentration_of_outgoing_RB
        print(f"1 sum_of_output_flows_m3 > parametrs_rb[4]: {sum_of_output_flows_m3} > {parametrs_rb[4]}")
        print(f"На РБ подано: {parametrs_rb[0]} m3/h, {parametrs_rb[1]} mg/l, {parametrs_rb[2]} mg/l")
        print(f"Ушло на сброс: {volumetric_discharge_flow_rate} m3/h, {concentration_of_key_pollutant_sum} mg/l")

    elif sum_of_output_flows_m3 == parametrs_rb[4]:
        volume_flow_of_incoming_RB_m = parametrs_rb[4]
        volume_flow_of_incoming_RB_l = round(volume_flow_of_incoming_RB_m * 1000, number_digits_after_the_comma)  # (m3 = 1000l)
        volumetric_discharge_flow_rate = 0
        concentration_of_input_RB = concentration_of_key_pollutant_sum
        concentration_of_outgoing_RB = round(concentration_of_input_RB * parametrs_rb[3], number_digits_after_the_comma)
        parametrs_rb[0] = volume_flow_of_incoming_RB_m
        parametrs_rb[1] = concentration_of_input_RB
        parametrs_rb[2] = concentration_of_outgoing_RB
        print(f"2 sum_of_output_flows_m3 == parametrs_rb[4]: {sum_of_output_flows_m3} == {parametrs_rb[4]}")
        print(f"На РБ подано: {parametrs_rb[0]} m3/h, {parametrs_rb[1]} mg/l, {parametrs_rb[2]} mg/l")
        print(f"Ушло на сброс: {volumetric_discharge_flow_rate} m3/h, {concentration_of_key_pollutant_sum} mg/l")

    elif sum_of_output_flows_m3 < parametrs_rb[4]:
        volume_flow_of_incoming_RB_m = sum_of_output_flows_m3
        volume_flow_of_incoming_RB_l = round(volume_flow_of_incoming_RB_m * 1000, number_digits_after_the_comma)  # (m3 = 1000l)
        volumetric_discharge_flow_rate = 0
        concentration_of_input_RB = concentration_of_key_pollutant_sum
        concentration_of_outgoing_RB = round(concentration_of_input_RB * parametrs_rb[3], number_digits_after_the_comma)
        parametrs_rb[0] = volume_flow_of_incoming_RB_m
        parametrs_rb[1] = concentration_of_input_RB
        parametrs_rb[2] = concentration_of_outgoing_RB
        print(f"3 sum_of_output_flows_m3 < parametrs_rb[4]: {sum_of_output_flows_m3} < {parametrs_rb[4]}")
        print(f"На РБ подано: {parametrs_rb[0]} m3/h, {parametrs_rb[1]} mg/l, {parametrs_rb[2]} mg/l")
        print(f"Ушло на сброс: {volumetric_discharge_flow_rate} m3/h, {concentration_of_key_pollutant_sum} mg/l")

    ####################################################################################################################
    # Recalculating plant parameters
    num_of_iter = 0
    for plant in table_4:
        input_volume_flow_for_plant = 0
        incoming_pollutant_mass = 0
        for stream in plant[1]:
            input_volume_flow_for_plant = round(input_volume_flow_for_plant + stream[1], number_digits_after_the_comma)
            input_volume_flow_for_plant_l = round(stream[1] * 1000, number_digits_after_the_comma)
            incoming_pollutant_mass = round(incoming_pollutant_mass + (stream[2] * input_volume_flow_for_plant_l), number_digits_after_the_comma)

        input_concentration = round(incoming_pollutant_mass / (input_volume_flow_for_plant * 1000), number_digits_after_the_comma)

        # plants[num_of_iter][0] = input_volume_flow_for_plant # There could be a mistake
        plants[num_of_iter][1] = input_concentration
        plants[num_of_iter][2] = round(input_concentration + plants[num_of_iter][3], number_digits_after_the_comma)
        num_of_iter = num_of_iter + 1

    # print(new_info_fresh_water)

    return plants, parametrs_rb, parametrs_fresh_water, table_4

# plant_info = [volume_flow, influent_concentration, effluent_concentration, additional_concentration, maximum_concentration_of_inbound_flow]
# parametrs_rb = [volume_flow_rb, influent_concentration_rb, effluent_concentration_rb, remaining_concentration_factor, max_volume_flow_rb]
# parametrs_fresh_water = [volume_consumption_of_fresh_water, fresh_water_concentration]

# new_plant_info_for_table_1 = [num_plant, plant_info[0], plant_info[4], plant_info[3]] - plant
# new_plant_info_for_table_2 = [num_plant, plant_info[0], plant_info[2]] - stream

# table_3 = [new_info_rb, parametrs_fresh_water]
# new_info_rb = [parametrs_rb[0], parametrs_rb[2]] - rb

# stream_for_table_4 = [plant[0], [[stream[0], stream[1], stream[2]], ["FW", required_volume_flow_rate_from_table_3, table_3[1][1]]]]



### For create lists of prodaction
# plants, parametrs_rb, parametrs_fresh_water = create_list_plants()
# print(plants)
# print(parametrs_rb)
# print(parametrs_fresh_water)



# #### Универсальное стабилизированное производство (Кейс № 1)
# plants = [[1.0, 1.0, 2.0, 1.0, 1.01], [39.0, 1.0, 311.0, 310.0, 2.34], [150.0, 1.0, 3001.0, 3000.0, 10.0], [1.0, 52.847, 3052.847, 3000.0, 528.47],
#           [112.0, 52.847, 468.847, 416.0, 413.792], [150.0, 52.847, 53.847, 1.0, 53.375], [1.0, 134.031, 1154.031, 1020.0, 597.778], [97.0, 134.031, 159.031, 25.0, 967.704],
#           [150.0, 134.031, 2647.031, 2513.0, 278.784]]
# parametrs_rb = [350.5, 1340.308, 134.031, 0.1, 350.5]
# parametrs_fresh_water = [350.5, 1.0]


##### ПНХЗ (Кейс № 2): TPH
plants = [[38.4, 0.0, 1000.0, 1000.0, 20.0], [70.0, 0.0, 300.0, 300.0, 20.0], [39.0, 0.0, 800.0, 800.0, 100.0], [10.0, 0.0, 200.0, 200.0, 150.0], [3.3, 0.0, 100.0, 100.0, 0.0],
          [45.0, 0.0, 188.0, 188.0, 150.0], [47.0, 0, 200.0, 200.0, 100.0], [80.1, 0.0, 65.0, 65.0, 100.0], [180.0, 0.0, 3000.0, 3000.0, 100.0], [75.3, 0.0, 25.0, 25.0, 0.0],
          [24.2, 0.0, 5.0, 5.0, 0.0]]
parametrs_rb = [612.3, 1074.636, 3.0, 0.0028, 612.3]
parametrs_fresh_water = [612.3, 0.0]

percent_of_difference_concentrations = 100
past_concentration_outgoing_rb = parametrs_rb[2]
num_of_iter = 0
amount_of_used_fresh_water = 0

while percent_of_difference_concentrations > 0.0001:
    plants, parametrs_rb, parametrs_fresh_water, table_4 = optimization_flows_plants(plants, parametrs_rb, parametrs_fresh_water)
    concentration_outgoing_rb = parametrs_rb[2]
    difference_concentrations = abs(round(past_concentration_outgoing_rb - concentration_outgoing_rb, 4))
    percent_of_difference_concentrations = round(difference_concentrations * 100 / past_concentration_outgoing_rb, 4)
    past_concentration_outgoing_rb = parametrs_rb[2]
    print("Итерация: ", num_of_iter)
    num_of_iter = num_of_iter + 1

print("parametrs_rb_1 = ", parametrs_rb, "parametrs_fresh_water_1 = ", parametrs_fresh_water)

for plant in table_4:
    print(plant)

for plant in plants:
    print(plant)



# for testing /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# num_of_iter = 0
# for i in range(100):
#     plants, parametrs_rb, parametrs_fresh_water, table_4 = optimization_flows_plants(plants, parametrs_rb, parametrs_fresh_water)
#     num_of_iter = num_of_iter + 1
#     print(num_of_iter)
#     print("parametrs_rb_1 = ", parametrs_rb, "parametrs_fresh_water_1 = ", parametrs_fresh_water)
#
# print("parametrs_rb_1 = ", parametrs_rb, "parametrs_fresh_water_1 = ", parametrs_fresh_water)
#
# for plant in table_4:
#     print(plant)
#
# for plant in plants:
#     print(plant)



# for testing /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# plants_1, parametrs_rb_1, parametrs_fresh_water_1, table_4_1 = optimization_flows_plants(plants, parametrs_rb, parametrs_fresh_water)
#
# print("parametrs_rb_1 = ", parametrs_rb_1, "parametrs_fresh_water_1 = ", parametrs_fresh_water_1)
#
# for plant in table_4_1:
#     print(plant)
#
# for plant in plants_1:
#     print(plant)
#
#
# plants_2, parametrs_rb_2, parametrs_fresh_water_2, table_4_2 = optimization_flows_plants(plants_1, parametrs_rb_1, parametrs_fresh_water_1)
#
# print("parametrs_rb_2 = ", parametrs_rb_2, "parametrs_fresh_water_2 = ", parametrs_fresh_water_2)
#
# for plant in table_4_2:
#     print(plant)
#
# for plant in plants_2:
#     print(plant)


