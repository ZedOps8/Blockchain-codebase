def can_win_suit(cards, trump, current_biggest_card):
    """Returns True if the player can win the current suit.

    Args:
        cards: A list of the player's cards.
        trump: The suit of the trump.
        current_biggest_card: The current biggest card.

    Returns:
        True if the player can win the current suit, False otherwise.
    """
    for card in cards:
        if card[0] == current_biggest_card[0]:  # Check if the suits match
            if card[1] > current_biggest_card[1]:
                return True
        elif card[0] == trump:
            return True
    return False

def optimal_card_selection(players, self, cards, trump, other_players_cards):
    """Selects the optimal card to play in a game similar to bridge.

    Args:
        players: A list of 4 player names in order.
        self: The name of the player who is playing last in this round.
        cards: A list of the player's cards.
        trump: The suit of the trump.
        other_players_cards: A dictionary mapping player names to lists of cards.

    Returns:
        The optimal card to play.
    """

    # Identify the current biggest card.
    current_biggest_card = None
    for player in players:
        if player != self:
            card = other_players_cards[player][0]
            if current_biggest_card is None or card > current_biggest_card:
                current_biggest_card = card

    # Identify the teammate of the player who played the current biggest card.
    teammate = None
    for player in players:
        if player != self and other_players_cards[player][0] == current_biggest_card:
            teammate = player
            break

    # Choose the optimal card to play.
    if teammate == self:
        return min(cards, key=lambda card: card)
    elif can_win_suit(cards, trump, current_biggest_card):
        return min([card for card in cards if card[0] == current_biggest_card[0]], key=lambda card: card[1])
    else:
        return min(cards, key=lambda card: (card[0] != trump, card[0], card[1]))

# Example input data
players = ["tom", "dick", "harry", "john"]
self = "john"
cards = ["s3", "sk", "ha"]
trump = "s"
other_players_cards = {
    "tom": ["s2"],
    "dick": ["s10"],
    "harry": ["ca"]
}

# Call the function and print the output
optimal_card = optimal_card_selection(players, self, cards, trump, other_players_cards)
print(optimal_card)