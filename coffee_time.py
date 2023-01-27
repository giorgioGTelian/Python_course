def mix_coffee(batch_weight, current_weight, current_ratio):
    # base case: if the current weight of the batch equals the desired batch weight, return
    if current_weight == batch_weight:
        return

    # calculate the target weight for each ingredient
    target_weight_caffe1 = batch_weight * 0.1
    target_weight_caffe2 = batch_weight * 0.24
    target_weight_caffe3 = batch_weight * 0.66

    # calculate the current weight of each ingredient
    current_weight_caffe1 = current_ratio[0] * current_weight
    current_weight_caffe2 = current_ratio[1] * current_weight
    current_weight_caffe3 = current_ratio[2] * current_weight

    # calculate the weight difference for each ingredient
    weight_diff_caffe1 = target_weight_caffe1 - current_weight_caffe1
    weight_diff_caffe2 = target_weight_caffe2 - current_weight_caffe2
    weight_diff_caffe3 = target_weight_caffe3 - current_weight_caffe3

    # add the ingredient with the largest weight difference
    if weight_diff_caffe1 >= weight_diff_caffe2 and weight_diff_caffe1 >= weight_diff_caffe3:
        current_ratio[0] += 1/1000
    elif weight_diff_caffe2 >= weight_diff_caffe1 and weight_diff_caffe2 >= weight_diff_caffe3:
        current_ratio[1] += 1/1000
    else:
        current_ratio[2] += 1/1000
    current_weight += 1/1000
    # recursively call the function with the updated current weight and ratio
    mix_coffee(batch_weight, current_weight, current_ratio)

# Initialize the current weight and ratio
current_weight = 0
current_ratio = [0.1, 0.24, 0.66]

# Call the function with the desired batch weight
batch_weight = 100
mix_coffee(batch_weight, current_weight, current_ratio)


def mix_coffee(batch_weight, current_weight, current_ratio):
    # base case: if the current weight of the batch equals the desired batch weight, return
    if current_weight == batch_weight:
        return

    # calculate the target weight for each ingredient
    target_weight_caffe1 = batch_weight * 0.1
    target_weight_caffe2 = batch_weight * 0.24
    target_weight_caffe3 = batch_weight * 0.38
    target_weight_caffe4 = batch_weight * 0.28

    # calculate the current weight of each ingredient
    current_weight_caffe1 = current_ratio[0] * current_weight
    current_weight_caffe2 = current_ratio[1] * current_weight
    current_weight_caffe3 = current_ratio[2] * current_weight
    current_weight_caffe4 = current_ratio[3] * current_weight

    # calculate the weight difference for each ingredient
    weight_diff_caffe1 = target_weight_caffe1 - current_weight_caffe1
    weight_diff_caffe2 = target_weight_caffe2 - current_weight_caffe2
    weight_diff_caffe3 = target_weight_caffe3 - current_weight_caffe3
    weight_diff_caffe4 = target_weight_caffe4 - current_weight_caffe4

    # add the ingredient with the largest weight difference
    if weight_diff_caffe1 >= weight_diff_caffe2 and weight_diff_caffe1 >= weight_diff_caffe3 and weight_diff_caffe1 >= weight_diff_caffe4:
        current_ratio[0] += 1/1000
    elif weight_diff_caffe2 >= weight_diff_caffe1 and weight_diff_caffe2 >= weight_diff_caffe3 and weight_diff_caffe2 >= weight_diff_caffe4:
        current_ratio[1] += 1/1000
    elif weight_diff_caffe3 >= weight_diff_caffe1 and weight_diff_caffe3 >= weight_diff_caffe2 and weight_diff_caffe3 >= weight_diff_caffe4:
        current_ratio[2] += 1/1000
    else:
        current_ratio[3] += 1/1000
    current_weight += 1/1000
    # recursively call the function with the updated current weight and ratio
    mix_coffee(batch_weight, current_weight, current_ratio)

# Initialize the current weight and ratio
current_weight = 0
current_ratio = [0.1, 0.24, 0.38, 0.28]

# Call the function with the desired batch weight, current weight, and current ratio

batch_weight = 100
mix_coffee(batch_weight, current_weight, current_ratio)

#Print the final ratio of ingredients
print("Final Ratio: ", current_ratio)
