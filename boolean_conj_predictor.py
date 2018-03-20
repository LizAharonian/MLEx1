import numpy as np
import sys

def main():
    """""
    main function.
    runs the program.
    argv[1] - command line argument.
    """""
    input_text_file = sys.argv[1]
    # read training examples from input file
    training_examples = np.loadtxt(input_text_file)
    # d is number of variables
    d = training_examples.size/len(training_examples) - 1
    # x is a matrix, each line contains optional substitute
    x = training_examples[:len(training_examples),:d]
    y = training_examples[:len(training_examples),d:training_examples.size/len(training_examples)]
    h = [ ]
    # initialize the all negative hypothesis
    for i in range(2*d):
        h.append(1)
    # find the correct hypothesis
    h = find_correct_hypothesis(h,training_examples,x,y,d)
    # build the output conjunction
    create_output_file(h,d)


def find_correct_hypothesis(h,training_examples,x,y,d):
    """""
    find_correct_hypothesis function.
    Keyword arguments:
    h - final hypothesis
    training_examples - set of examples
    x - x is a matrix, each line contains optional substitute
    y - vector of correct tag
    d - number of variables
    return:
    final hypothesis
    """""
    for i in range(len(training_examples)):
        if y[i]==0:
            continue
        instance = x[i]
        y_prediction = 1
        for variable_index in range(1,len(instance) +1):
            if h[variable_index*2 -2] ==1:
                y_prediction = y_prediction*instance[variable_index-1]
            if h[variable_index*2 - 1] ==1:
                if instance[variable_index-1] == 0:
                    setVal = 1
                else:
                    setVal = 0
                y_prediction = y_prediction*setVal
        if y[i] == 1 and y_prediction == 0:
            for index in range(d):
                if instance[index] == 1:
                    h[2*(index+1) -1] = 0
                if instance[index] ==0:
                    h[2*(index+1)-2] = 0
    return h

def create_output_file(h,d):
    """""
    create_output_file function.
    Keyword arguments:
    h - final hypothesis
    d - number of variables
    return:
    no outout
    """""
    output = ""
    for i in range(1, d + 1):
        if h[2 * i - 2] == 1:
            output += ",x" + str(i)
        if h[2 * i - 1]:
            output += ",not(x" + str(i) + ")"
    output = output.strip(",")
    file = open("output.txt", "w")
    file.write(output)
    file.close()

if __name__ == '__main__':
    main()