import random
import math

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def weights_ways():
    nodes_number = int( input('Type the number of nodes: ') )
    nodes = letters[0:nodes_number]

    weights = []
    inv_weights = []

    for i in range( nodes_number ):

        row = []
        inv_row = []

        for j in range ( nodes_number ):

            if i == j:
                row.append(0)
                inv_row.append(0)
            
            elif i>j:
                row.append( weights[j][i] )
                inv_row.append( inv_weights[j][i] )

            else:
                weight = int( input(f'Type the weight of the path between {nodes[i]} and {nodes[j]}: '))
                row.append(weight)
                if weight == 0:
                    inv_row.append( 0 )
                else:
                    inv_row.append( 1/weight )

        weights.append( row )
        inv_weights.append( inv_row )

    for i in range( nodes_number ):
        print(weights[i])
    
    return (nodes, weights, inv_weights)


def calc_inverses_weigths(weights):

    size = len(weights)

    inv_weights = [[0 for col in range(size)] for row in range(size)]

    for i in range(size):
        for j in range(size):
            if weights[i][j] == 0:
                inv_weights[i][j] = 0
            else:
                inv_weights[i][j] = 1/weights[i][j]
    
    return inv_weights


def weights_dic():

    (nodes, weights, inv_weights) = weights_ways()

    path_weights = {}

    for i in range( len(nodes) - 1):
        for j in range( i, len(nodes) ):
            if i != j:
                path_weights[(nodes[i],nodes[j])] = weights[i][j]

    print( path_weights )

    return path_weights


def calc_min_path_prim(nodes, weights_matrix, inverses_weights):

    nodes_number = len(nodes)

    nodes_connected = [ nodes[0] ]
    paths_selected = [[0 for col in range(nodes_number)] for row in range(nodes_number)]

    while len(nodes_connected)<nodes_number:

        max_list = []
        for i in range(len(nodes_connected)):
            max_list.append( max(inverses_weights[ nodes.index( nodes_connected[i] ) ]) )
        
        # print( max_list )

        row_with_max = max_list.index( max( max_list ) )

        row = nodes.index( nodes_connected[row_with_max] )
        # print(f'row= {row}')
        col = inverses_weights[row].index( max(max_list))

        paths_selected[row][col] = weights_matrix[row][col]

        for k in range(nodes_number):
            inverses_weights[k][col] = 0
        inverses_weights[col][row] = 0


        nodes_connected.append( nodes[col] )
        # print( nodes_connected )

    total_weight = 0
    for i in range(nodes_number):
        for j in range(nodes_number):
            total_weight += paths_selected[i][j]

    print('Paths availables')
    for i in range(nodes_number):
        print(weights_matrix[i])

    print('Paths selected')
    for i in range(nodes_number):
        print( paths_selected[i] )

    print(f'The total weight is {total_weight}')


def run():

    # test = [[0, 4, 0, 6, 4, 0, 0, 0, 0],
    #         [4, 0, 3, 0, 7, 0, 0, 0, 0],
    #         [0, 3, 0, 0, 0, 5, 0, 0, 0],
    #         [6, 0, 0, 0, 5, 0, 8, 0, 0],
    #         [4, 7, 0, 5, 0, 2, 0, 2, 4],
    #         [0, 0, 5, 0, 2, 0, 0, 0, 4],
    #         [0, 0, 0, 8, 0, 0, 0, 6, 0],
    #         [0, 0, 0, 0, 2, 0, 6, 0, 5],
    #         [0, 0, 0, 0, 4, 4, 0, 5, 0]]

    # nodes = letters[0:len(test)]
    # inv_test = calc_inverses_weigths(test)
    # calc_min_path(nodes, test, inv_test)

    (nodes, weights, inv_weights) = weights_ways()
    calc_min_path_prim(nodes, weights, inv_weights)


if __name__=='__main__':
    run()
    