def minimax_decision(board, depth):
    possible_actions = board.get_possible_actions()
    
    for action in possible_actions:
