import numpy as np
import sys

def main():
    input_text_file = sys.argv[1]
    training_examples = np.loadtxt(input_text_file)
    d = training_examples.size/len(training_examples) - 1
    x = training_examples[:len(training_examples),:d]
    print(x)
    y = training_examples[:len(training_examples),d:training_examples.size/len(training_examples)]
    print (y)
    h = [ ]
    #initialize the all negative hypothesis
    for i in range(2*d):
        h.append(1)
    y_gag =1
    #set values in hypothesis
    for i in range(len(training_examples)):
        if y[i]==0:
            continue
        instance = x[i]
        y_gag = 1
        for variable_index in range(1,len(instance) +1):
            if h[variable_index*2 -2] ==1:
                y_gag = y_gag*instance[variable_index-1]
            if h[variable_index*2 - 1] ==1:
                if instance[variable_index-1] == 0:
                    setVal = 1
                else:
                    setVal = 0
                y_gag = y_gag*setVal
        if y[i] == 1 and y_gag == 0:
            for index in range(d):
                if instance[index] == 1:
                    h[2*(index+1) -1] = 0
                if instance[index] ==0:
                    h[2*(index+1)-2] = 0
    output =""
    for i in range(1, d+1):
        if h[2*i-2]==1:
            output +=",x"+str(i)
        if h[2*i - 1]:
            output +=",not(x"+str(i)+")"
    output = output.strip(",")
    print output

    file = open("output.txt", "w")
    file.write(output)
    file.close()



    ##################
    print "my final hypo"
    print (h)
    # set values in hypothesis

    for i in range(len(training_examples)):
        if y[i] == 0:
            continue
        instance = x[i]
        y_gag = 1
        for variable_index in range(1, len(instance) + 1):
            if h[variable_index * 2 - 2] == 1:
                y_gag = y_gag * instance[variable_index - 1]
            if h[variable_index * 2 - 1] == 1:
                if instance[variable_index - 1] == 0:
                    setVal = 1
                else:
                    setVal = 0
                y_gag = y_gag * setVal
        if y[i] == 1 and y_gag == 0:
            print "kaka"
    #########
    print h
    print "done"



if __name__ == '__main__':
    main()