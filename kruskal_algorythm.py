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


def calc_min_path_kruskal(nodes, weights_matrix, inverses_weights):
    
    nodes_number = len(nodes)

    nodes_connected = [] 
    paths_selected = [[0 for i in range(nodes_number)] for j in range(nodes_number)]
    # nodes_connected = [[0 for i in range(1)] for j in range(nodes_number)]
    # for i in range( nodes_number):
    #     nodes_connected[i] = [nodes[i]] 
    # print(nodes_connected)

    max_list = []
    for i in range( nodes_number ):
        max_list.append( max(inverses_weights[i] ) )

    row = max_list.index( max(max_list) )
    col = inverses_weights[row].index( max(max_list) )

    paths_selected[row][col] = weights_matrix[row][col]
    paths_selected[col][row] = weights_matrix[row][col]
    inverses_weights[row][col] = 0
    inverses_weights[col][row] = 0

    nodes_connected.append( [ nodes[row], nodes[col] ] )

    print(f'The first way connects {nodes[row]} and {nodes[col]}')

    while len(nodes_connected[0]) < nodes_number:

        # print(inverses_weights)

        max_list = []
        for i in range( nodes_number ):
            max_list.append( max(inverses_weights[i] ) )

        # print(max_list)

        row = max_list.index( max(max_list) )
        col = inverses_weights[row].index( max(max_list) )

        paths_selected[row][col] = weights_matrix[row][col]
        paths_selected[col][row] = weights_matrix[row][col]

        print(f'row  = {row}, col = {col}')

        print(f'The nodes {nodes[row]} and {nodes[col]} have been joined')

        node_row = -1
        node_col = -1

        for i in range( len(nodes_connected) ):

            if nodes_connected[i].__contains__( nodes[row] ):
                node_row = i
            elif nodes_connected[i].__contains__( nodes[col] ):
                node_col = i
            
        if node_row == -1 and node_col == -1:
            nodes_connected.append( [ nodes[row], nodes[col] ] )
            inverses_weights[row][col] = 0
            inverses_weights[col][row] = 0
        elif node_row != -1 and node_col == -1:
            # inverses_weights[row][col] = 0
            # inverses_weights[col][row] = 0
            for k in range( len(nodes_connected[node_row]) ):
                aux = nodes.index( nodes_connected[node_row][k] )
                inverses_weights[aux][col] = 0
                inverses_weights[col][aux] = 0
            nodes_connected[node_row].append( nodes[col] )

        elif node_row == -1 and node_col != -1:
            for k in range( len(nodes_connected[node_col]) ):
                aux = nodes.index( nodes_connected[node_col][k] )
                inverses_weights[aux][row] = 0
                inverses_weights[row][aux] = 0
            nodes_connected[node_col].append( nodes[row] )
        else:
            print(nodes_connected[node_row])
            print(nodes_connected[node_col])
            for m in range( len(nodes_connected[node_row]) ):
                for n in range( len(nodes_connected[node_col]) ):
                    aux1 = nodes.index( nodes_connected[node_row][m] )
                    aux2 = nodes.index( nodes_connected[node_col][n] )
                    inverses_weights[aux1][aux2] = 0
                    inverses_weights[aux2][aux1] = 0
        
            nodes_connected[node_row].extend( nodes_connected[node_col] )
            nodes_connected.pop( node_col )

        print( nodes_connected )

        print('The paths selected are:')
        for i in range(nodes_number):
            print( paths_selected[i] )


def run():
    (nodes, weights, inv_weights) = weights_ways()
    calc_min_path_kruskal(nodes, weights, inv_weights)


if __name__=='__main__':
    run()