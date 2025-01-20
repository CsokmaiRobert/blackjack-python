# Blackjack Game in Python

This is a simple implementation of the classic Blackjack game using Python. The game allows you to play against the dealer, where you can choose to draw cards or hold. The objective is to get as close to 21 as possible without going over. The dealer must draw cards until their total is at least 17.

---

## Features:
- **Card Drawing:** Draw cards by pressing 'y' and stop drawing with 'n'.
- **Game Flow:** The player competes against the dealer to have a hand value closer to 21.
- **Automatic Dealer Actions:** The dealer automatically draws cards until their hand value is 17 or greater.
- **Game Outcomes:** You win, lose, or tie based on the comparison of the player's hand to the dealer's hand.

---

## How It Works:
1. **Starting the Game:**
   - The player and dealer each receive two random cards from the deck.
   - The player's total is displayed, as well as the dealer's first card.
   
2. **Player's Turn:**
   - The player can choose to "hit" (draw another card) by pressing `y`.
   - If the total goes over 21, the player loses.
   - If the player chooses to "stay" (press `n`), the dealer's turn begins.
   
3. **Dealer's Turn:**
   - The dealer must draw cards until their hand value is at least 17.
   - If the dealer exceeds 21, the player wins.
   
4. **Outcome:**
   - If the player's hand is closer to 21 than the dealer's hand, the player wins.
   - If both hands have the same total, it’s a tie.
   - If the dealer's hand is closer to 21, the player loses.

---

## Example Game Flow:

### Initial Deal:
```text
Your cards: [10, 6] Your total: 16
Dealer's cards: [9] Dealer total: 9
