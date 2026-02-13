from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.registered_cards = {}
        self.matches_played = 0

    def register_cards(self, card: TournamentCard) -> str:
        card_id = card.name.replace(" ", "_").lower() + "_001"
        self.registered_cards.update({card_id: card})
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches_played += 1
        card1 = self.registered_cards.get(card1_id)
        card2 = self.registered_cards.get(card2_id)
        card1.attack(card2)
        card2.attack(card1)
        if card1.health > card2.health:
            winner = card1
            winner_id = card1_id
            winner.update_wins(1)
            loser = card2
            loser_id = card2_id
            loser.update_losses(1)
            card1.calculate_rating()
            card2.calculate_rating()
        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        return sorted(self.registered_cards.values(),
                      key=lambda card: card.calculate_rating(),
                      reverse=True)

    def generate_tournament_report(self) -> dict:
        return {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": (
                round(
                    sum(
                        card.calculate_rating()
                        for card in self.registered_cards.values()
                    )
                    / len(self.registered_cards)
                )
            ),
            "platform_status": "active"
        }
