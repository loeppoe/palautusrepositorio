class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.score_tie(self.player1_score)

        if self.player1_score >= 4 or self.player2_score >= 4:
            result_difference = self.player1_score - self.player2_score

            if result_difference == 1:
                return self.score_advantage(result_difference)
            if result_difference == -1:
                return self.score_advantage(result_difference)
            else:
                return self.score_win(result_difference)
        
        else:
            return self.score_names()
    
    def score_tie(self, score):
        if score == 0:
            return "Love-All"
        if score == 1:
            return "Fifteen-All"
        if score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
    
    def score_advantage(self, difference):
        if difference == 1:
            return "Advantage player1"
        if difference == -1:
            return "Advantage player2"
    
    def score_win(self, difference):
        if difference >= 1:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def score_names(self):
        temp_score = 0
        score = ""
        for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
        return score
            
