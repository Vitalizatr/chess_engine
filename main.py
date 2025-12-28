class Board:
    def __init__(self,b_p = 0b0000000000111100110000110000000000000000000000000000000000000000,w_p = 0b0000000000000000000000000000000000000000110000110011110000000000,b_k = 0b1011110000000000000000000000000000000000000000000000000000000000,w_k = 0b0000000000000000000000000000000000000000000000000000000000111101):
        self.black_pawns = b_p
        self.white_pawns = w_p
        self.black_knights = b_k
        self.white_knights = w_k
        self.board = 0b0100001111000011000000000000000000000000000000001100001111000010
        self.white_turn = True
        self.en_passant_pawn_white = 0
        self.en_passant_pawn_black = 0
        self.white_king = 0b0000000000000000000000000000000000000000010000000010000000000000
        self.black_king = 0b0000000000000100000000100000000000000000000000000000000000000000
        self.cof_for_pawns =         [0,0,0,0,0,0,0,0,
                                      0,0,-0.1,-0.05,-0.05,0,0,0,
                                      -0.05,-0.1,-0.05,0,0,0.1,-0.05,-0.05,
                                      0,0.05,0,0.5,0.5,0,0,0,
                                      0,0,0,0,0,0,0,0,
                                      0,0,0,0,0,0,0,0,
                                      0,0,0,0,0,0,0,0,
                                      0,0,0,0,0,0,0,0]
        self.cof_for_knights =       [-0.25,2,-0.05,0,-0.05,0,2,2,
                                      2,2,0,0,0,0,2,2,
                                      0.15,0.15,0.10,0.05,0,-0.05,-0.1,-0.15,
                                      0.25,0.25,0.2,0.1,0.5,0,-0.05,-0.1,
                                      0.15,0.15,0.10,0.10,0.05,0,-0.05,-0.1,
                                      0.25,100,0.2,0.2,0.2,0.05,0,-0.05,
                                      2,2,100,0.25,0.15,0.15,2,2,
                                      0,2,0.25,0.2,0.25,0.2,2,-0.1]
    def sum_white_pieces(self):
        sum = 0
        U64 = (1<<64)-1
        n = self.white_pawns & U64
        while n:
            lsb = n & -n  & U64            
            index = lsb.bit_length()-1
            sum+=self.cof_for_pawns[63-index]
            n &= n - 1  & U64
            sum+=1
        
        
        n = self.white_knights & U64
        while n:
            lsb = n & -n  & U64            
            index = lsb.bit_length()-1
            sum+=self.cof_for_knights[63-index]
            n &= n - 1  & U64
            sum+=5
        return sum
    
    def sum_black_pieces(self):
        sum = 0
        U64 = (1<<64)-1
        n = self.black_pawns & U64
        while n:
            lsb = n & -n  & U64            
            index = lsb.bit_length()-1
            sum+=self.cof_for_pawns[index]
            n &= n - 1  & U64
            sum+=1

        n = self.black_knights & U64
        while n:
            lsb = n & -n  & U64           
            index = lsb.bit_length()-1
            sum+=self.cof_for_knights[index]
            n &= n - 1  & U64
            sum+=5
        return sum
    
    def knight_move(self,index):
        moves = {1: 132096, 4: 659456, 8: 1318912, 16: 2622464, 32: 5244928, 1024: 168886289, 2048: 337772576, 4096: 675545092, 8192: 1351090184, 65536: 8657044480, 131072: 21609056261, 262144: 43234889736, 524288: 86469779476, 1048576: 172939543592, 2097152: 345879087120, 4194304: 687463206944, 8388608: 275414786048, 16777216: 2216203386880, 33554432: 5531918402560, 67108864: 11068131837952, 134217728: 22136263676928, 268435456: 44272527353856, 536870912: 88545054691328, 1073741824: 175990580977664, 2147483648: 70506185228288, 4294967296: 4398113751040, 8589934592: 1134696134410240, 17179869184: 2270491797225472, 34359738368: 5666883501293568, 68719476736: 11333767002587136, 137438953472: 4653135495692288, 274877906944: 9024791719706624, 549755813888: 35184913154048, 1099511627776: 1125917120266240, 2199023255552: 290482210409021440, 4398046511104: 580964425113010176, 8796093022208: 1450159226377732096, 17592186044416: 2883429954152824832, 35184372088832: 1155173889878261760, 70368744177664: 11533718717099671552, 140737488355328: 9007337767436288, 1125899906842624: 1152940239254192128, 2251799813685248: 2305880478508384256, 4503599627370496: 288305314741092352, 9007199254740992: 9799982666336960512, 288230376151711744: 4514594743648256, 576460752303423488: 9029189487296512, 1152921504606846976: 1169880371953664, 2305843009213693952: 2339760743907328, 9223372036854775808: 9077567998918656}
        
        if self.white_turn: return (moves.get(index,0)) & ~(self.white_pawns | self.white_knights)
        return (moves.get(index,0)) & ~(self.black_pawns | self.black_knights)
    
    def white_pawns_move_1(self,index):
        moves_1 = {4: 1024, 8: 2048, 16: 4096, 32: 8192, 1024: 262144, 2048: 524288, 4096: 1048576, 8192: 2097152, 65536: 16777216, 131072: 33554432, 262144: 67108864, 524288: 134217728, 1048576: 268435456, 2097152: 536870912, 4194304: 1073741824, 8388608: 2147483648, 16777216: 4294967296, 33554432: 8589934592, 67108864: 17179869184, 134217728: 34359738368, 268435456: 68719476736, 536870912: 137438953472, 1073741824: 274877906944, 2147483648: 549755813888, 4294967296: 1099511627776, 8589934592: 2199023255552, 17179869184: 4398046511104, 34359738368: 8796093022208, 68719476736: 17592186044416, 137438953472: 35184372088832, 274877906944: 70368744177664, 549755813888: 140737488355328, 4398046511104: 1125899906842624, 8796093022208: 2251799813685248, 17592186044416: 4503599627370496, 35184372088832: 9007199254740992, 1125899906842624: 288230376151711744, 2251799813685248: 576460752303423488, 4503599627370496: 1152921504606846976, 9007199254740992: 2305843009213693952}
        capture = {4: 2048, 8: 5120, 16: 10240, 32: 4096, 1024: 655360, 2048: 1310720, 4096: 2621440, 8192: 5242880, 65536: 8388608, 131072: 83886080, 262144: 167772160, 524288: 335544320, 1048576: 671088640, 2097152: 1342177280, 4194304: 2684354560, 8388608: 4294967296, 16777216: 2147483648, 33554432: 21474836480, 67108864: 42949672960, 134217728: 85899345920, 268435456: 171798691840, 536870912: 343597383680, 1073741824: 687194767360, 2147483648: 1099511627776, 4294967296: 549755813888, 8589934592: 5497558138880, 17179869184: 10995116277760, 34359738368: 21990232555520, 68719476736: 43980465111040, 137438953472: 87960930222080, 274877906944: 175921860444160, 1099511627776: 140737488355328, 2199023255552: 1125899906842624, 4398046511104: 2251799813685248, 8796093022208: 5629499534213120, 17592186044416: 11258999068426240, 35184372088832: 4503599627370496, 70368744177664: 9007199254740992, 1125899906842624: 576460752303423488, 2251799813685248: 1441151880758558720, 4503599627370496: 2882303761517117440, 9007199254740992: 1152921504606846976}
        ocupaid = self.black_pawns | self.black_knights | self.white_knights| self.white_pawns
        capturable = self.black_knights | self.black_pawns | self.en_passant_pawn_black
        return (moves_1.get(index,0) & ~ocupaid) | (capture.get(index,0) & capturable)
    
    def white_pawns_move_2(self,index):
        moves_2 = {1024: 67108864, 2048: 134217728, 4096: 268435456, 8192: 536870912}
        ocupaid = self.black_pawns | self.black_knights | self.white_knights| self.white_pawns
        return (moves_2.get(index,0) & ~(ocupaid | ocupaid<<8))

    def white_pawns_promotion(self,index):
        moves_1 = {1125899906842624: 288230376151711744, 2251799813685248: 576460752303423488, 4503599627370496: 1152921504606846976, 9007199254740992: 2305843009213693952}
        capture = {1125899906842624: 576460752303423488, 2251799813685248: 1441151880758558720, 4503599627370496: 2882303761517117440, 9007199254740992: 1152921504606846976}
        ocupaid = self.black_pawns | self.black_knights | self.white_knights| self.white_pawns
        capturable = self.black_knights | self.black_pawns
        return (moves_1.get(index,0) & ~ocupaid) | (capture.get(index,0) & capturable)
    
    def black_pawns_move_1(self,index):
        moves_1 = {1024: 4, 2048: 8, 4096: 16, 8192: 32, 262144: 1024, 524288: 2048, 1048576: 4096, 2097152: 8192, 16777216: 65536, 33554432: 131072, 67108864: 262144, 134217728: 524288, 268435456: 1048576, 536870912: 2097152, 1073741824: 4194304, 2147483648: 8388608, 4294967296: 16777216, 8589934592: 33554432, 17179869184: 67108864, 34359738368: 134217728, 68719476736: 268435456, 137438953472: 536870912, 274877906944: 1073741824, 549755813888: 2147483648, 1099511627776: 4294967296, 2199023255552: 8589934592, 4398046511104: 17179869184, 8796093022208: 34359738368, 17592186044416: 68719476736, 35184372088832: 137438953472, 70368744177664: 274877906944, 140737488355328: 549755813888, 1125899906842624: 4398046511104, 2251799813685248: 8796093022208, 4503599627370496: 17592186044416, 9007199254740992: 35184372088832, 288230376151711744: 1125899906842624, 576460752303423488: 2251799813685248, 1152921504606846976: 4503599627370496, 2305843009213693952: 9007199254740992}
        capture = {1024: 8, 2048: 16, 4096: 32, 8192: 16, 131072: 1024, 262144: 2048, 524288: 4096, 1048576: 8192, 2097152: 4096, 4194304: 8192, 8388608: 65536, 33554432: 262144, 67108864: 524288, 134217728: 1048576, 268435456: 2097152, 536870912: 4194304, 1073741824: 8388608, 2147483648: 16777216, 4294967296: 8388608, 8589934592: 67108864, 17179869184: 134217728, 34359738368: 268435456, 68719476736: 536870912, 137438953472: 1073741824, 274877906944: 2147483648, 549755813888: 4294967296, 1099511627776: 2147483648, 2199023255552: 17179869184, 4398046511104: 34359738368, 8796093022208: 68719476736, 17592186044416: 137438953472, 35184372088832: 274877906944, 70368744177664: 549755813888, 140737488355328: 1099511627776, 1125899906842624: 8796093022208, 2251799813685248: 17592186044416, 4503599627370496: 35184372088832, 9007199254740992: 70368744177664, 288230376151711744: 2251799813685248, 576460752303423488: 4503599627370496, 1152921504606846976: 9007199254740992, 2305843009213693952: 4503599627370496}
        
        ocupaid = self.black_pawns | self.black_knights | self.white_knights| self.white_pawns
        capturable = self.white_knights | self.white_pawns | self.en_passant_pawn_white
        return ((moves_1.get(index,0)) & ~ocupaid) | (capture.get(index,0) & capturable)

    def black_pawns_move_2(self,index):
        moves_2 = {1125899906842624: 17179869184, 2251799813685248: 34359738368, 4503599627370496: 68719476736, 9007199254740992: 137438953472}
        ocupaid = self.black_pawns | self.black_knights | self.white_knights| self.white_pawns
        return (moves_2.get(index,0) & ~(ocupaid | ocupaid<<8))
    
        
    def black_pawns_promotion(self,index):
        moves_1 = {1024: 4, 2048: 8, 4096: 16, 8192: 32}
        capture = {1024: 8, 2048: 16, 4096: 32, 8192: 16}
        ocupaid = self.black_pawns | self.black_knights | self.white_knights| self.white_pawns
        capturable = self.white_knights | self.white_pawns
        return ((moves_1.get(index,0)) & ~ocupaid) | (capture.get(index,0) & capturable)

    def advantage(self):
        return self.sum_white_pieces()-self.sum_black_pieces()
    
    def make_move_knight(self,tip,move):
        board = Board(self.black_pawns,self.white_pawns,self.black_knights,self.white_knights)
        
        if(self.white_turn):
            board.white_knights &= ~ tip
            board.white_knights |= move
            board.black_knights  &= ~ move
            board.black_pawns &= ~move
            board.white_turn = False
            return board
        board.black_knights &= ~ tip
        board.black_knights |= move
        board.white_knights  &= ~ move
        board.white_pawns &= ~move
        return board
            
    def make_move_pawns_1(self,tip,move):
        board = Board(self.black_pawns,self.white_pawns,self.black_knights,self.white_knights)
        
        if(self.white_turn):
            board.white_pawns &= ~ tip
            board.white_pawns |= move
            board.black_knights  &= ~ move
            board.black_pawns &= ~move
            board.white_turn = False
            return board
        board.black_pawns &= ~ tip
        board.black_pawns |= move
        board.white_knights  &= ~ move
        board.white_pawns &= ~move
        return board
        
    def make_move_pawns_2(self,tip,move):
        board = Board(self.black_pawns,self.white_pawns,self.black_knights,self.white_knights)
        
        if(self.white_turn):
            board.en_passant_pawn_white = move>>8
            board.white_pawns &= ~ tip
            board.white_pawns |= move
            board.white_turn = False
            return board
        board.en_passant_pawn_black = move<<8
        board.black_pawns &= ~ tip
        board.black_pawns |= move
        return board
        
    def make_promotion_pawn(self,tip,move):
        board = Board(self.black_pawns,self.white_pawns,self.black_knights,self.white_knights)
        
        if(self.white_turn):
            board.white_pawns &= ~ tip
            board.white_knights |= move
            board.white_turn = False
            return board
        board.black_pawns &= ~ tip
        board.black_knights |= move
        return board   
    
    def game_over(self):
        U64 = (1<<64)-1
        if(self.white_turn):
            n = self.white_knights & U64
            while n:
                lsb = n & -n  & U64            
                if(lsb & self.black_king != 0):
                    return 1000
                n &= n - 1  & U64
        n = self.black_knights & U64
        while n:
            lsb = n & -n  & U64          
            if(lsb & self.white_king != 0):
                return -1000
            n &= n - 1  & U64
        return 0

def int_arr(n):
    arr = []

    U64 = (1<<64)-1
    while n:
        arr.append(n & -n  & U64)
        n &= n - 1  & U64
    return arr

def analiz(board,deapth):
    if(deapth==0 or board.game_over() !=0):
        return float(board.advantage() + board.game_over())
    
    if(board.white_turn):
        best = -10000
        for pawn in int_arr(board.white_pawns):
            for move_1 in int_arr(board.white_pawns_move_1(pawn)):
                b = board.make_move_pawns_1(pawn,move_1)
                val = analiz(b,deapth-1)
                best = max(best,val)
            for move_2 in int_arr(board.white_pawns_move_2(pawn)):
                b = board.make_move_pawns_2(pawn,move_2)
                val = analiz(b,deapth-1)
                best = max(best,val)
            for promotion in int_arr(board.white_pawns_promotion(pawn)):
                b = board.make_promotion_pawn(pawn,promotion)
                val = analiz(b,deapth-1)
                best = max(best,val)
        for knight in int_arr(board.white_knights):
            for move in int_arr(board.knight_move(knight)):
                b = board.make_move_knight(knight,move)
                print(knight.bit_length(),move.bit_length())
                val = analiz(b,deapth-1)
                best = max(best,val)   
    else:
        best = 10000
        for pawn in int_arr(board.black_pawns):
            for move_1 in int_arr(board.black_pawns_move_1(pawn)):
                b = board.make_move_pawns_1(pawn,move_1)
                val = analiz(b,deapth-1)
                best = min(best,val)
            for move_2 in int_arr(board.black_pawns_move_2(pawn)):
                b = board.make_move_pawns_2(pawn,move_2)
                val = analiz(b,deapth-1)
                best = min(best,val)
            for promotion in int_arr(board.black_pawns_promotion(pawn)):
                b = board.make_promotion_pawn(pawn,promotion)
                val = analiz(b,deapth-1)
                best = min(best,val)
        for knight in int_arr(board.black_knights):
            for move in int_arr(board.knight_move(knight)):
                b = board.make_move_knight(knight,move)
                print(knight.bit_length(),move.bit_length())
                val = analiz(b,deapth-1)
                best = min(best,val)   
                
    return best
