import math
from random import sample, choice

import pygame as pg

from card import Card
from card_sprite import SpriteMove
from deck import Deck
from const import *


class GameController:
	def __init__(self, sound_controller=None):
		self.sound_controller = sound_controller

		self.screen = pg.display.set_mode(SCREEN_SIZE)
		self.clock = pg.time.Clock()

		self.background_image = pg.image.load('./img/board.jpg')
		self.screen.blit(self.background_image, (0, 0))

		self.deck = Deck()
	
		self.deck_card_sprite_group = pg.sprite.Group([self.deck.create_card(DECK_POSITION, Suit.back_side, Rank.back_side).sprite])
		self.card_in_action_sprite_group = pg.sprite.Group([])
		self.user_cards_sprites = pg.sprite.Group([])
		self.agent_cards_sprites = pg.sprite.Group([])

		self.sprite_moves = []
		self.current_player_move = USER
		self.current_move_by = USER
		self.game_is_over = False
		self.is_animating = True

		self.show_skip_button = True
		self.skip_button_pos = Point(100, 395)

		self.can_through_only_by_rank = True

		self.can_get_new_card = False
		self.four_in_action = False

		self._initialize_board()

	def main_loop(self):
		while True:
			self._check_if_game_is_over()
			self.is_animating = len(self.sprite_moves) != 0

			for event in pg.event.get():
				if event.type == pg.QUIT:
					exit()
				elif not self.is_animating and event.type == pg.MOUSEBUTTONDOWN:
					self._check_user_input()

			if self.game_is_over:
				continue

			if not self.is_animating and self.current_player_move == AGENT and not self.can_through_only_by_rank:
				self._ai_decide_which_move_to_make()
			elif not self.is_animating and self.current_player_move == AGENT:
				self._ai_through_up_all_possible_cards()

			self._update_animation()

			self.screen.blit(self.background_image, (0, 0))

			self.deck_card_sprite_group.draw(self.screen)
			self.card_in_action_sprite_group.draw(self.screen)
			self.agent_cards_sprites.draw(self.screen)
			self.user_cards_sprites.draw(self.screen)

			if self.show_skip_button:
				self._render_skip_button()

			pg.display.update()
			self.clock.tick(FPS)

	def _check_user_input(self):
		rel = pg.mouse.get_rel()  # we need these three lines, so that if we click mouse once it won't make 100 events of it
		if math.fabs(rel[0]) < 1 and math.fabs(rel[1]) < 1:
			return

		if self.current_player_move == USER:
			mouse_pos = Point(*pg.mouse.get_pos())

			if self.can_get_new_card and self._user_has_chosen_deck(mouse_pos):
				self._player_gets_a_card_from_deck(USER)
				self.can_get_new_card = False
				self.show_skip_button = True
			elif 700 < mouse_pos.y < 1000:
				for user_card in self.deck.user_cards:
					if user_card.was_chosen(mouse_pos):
						if self.can_make_move(user_card):
							self._make_a_move(user_card)
							self.current_move_by = USER
							break
						else:
							self.sound_controller.play(0, 0, fade_ms=5)
			elif self._user_is_pressing_skip_button(mouse_pos):
				if self.four_in_action and self.current_move_by == USER:
					for i in range(int(self.deck.card_in_action.rank)):
						self._player_gets_a_card_from_deck(AGENT)
					self.four_in_action = False
				self.current_player_move = AGENT
				self.show_skip_button = False
				self.can_get_new_card = True
				self.can_through_only_by_rank = False

	def _check_if_game_is_over(self):
		if len(self.deck.agent_cards) == 0 or len(self.deck.user_cards) == 0:
			self._draw_game_over(self.current_player_move)
			self.game_is_over = True

	def _user_has_chosen_deck(self, mouse_pos):
		width, height = CARD_SIZE
		x, y = mouse_pos.x, mouse_pos.y

		fits_y = DECK_POSITION.y - height // 2 < y < DECK_POSITION.y + height // 2
		fits_x = DECK_POSITION.x - width // 2 < x < DECK_POSITION.x + width // 2

		return fits_y and fits_x

	def _update_animation(self):
		for move in self.sprite_moves:
			move.update()

			if move.is_completed():
				self.sprite_moves.remove(move)

	def _initialize_board(self):
		self.deck.initialize_deck()
		
		self.agent_cards_sprites.add([self.deck.create_card(DECK_POSITION, Suit.back_side, Rank.back_side).sprite for i in range(len(self.deck.agent_cards))])
		self.user_cards_sprites.add([c.sprite for c in self.deck.user_cards])
		self.card_in_action_sprite_group.add(self.deck.card_in_action.sprite)
		
		self.sprite_moves.append(SpriteMove([self.deck.card_in_action.sprite], [TABLE_CENTER]))
		
		agent_cards_coords = [Point(100 + i * 90, 150) for i in range(len(self.deck.agent_cards))]
		self.sprite_moves.append(SpriteMove(list(self.agent_cards_sprites), agent_cards_coords))

		user_cards_coords = [Point(100 + (i * 1.35) * 90, 750) for i in range(len(self.deck.user_cards))]
		self.sprite_moves.append(SpriteMove(list(self.user_cards_sprites), user_cards_coords))

		self._check_the_effect_of_the_move()

	def can_make_move(self, chosen_card: Card):
		if self.four_in_action:
			return ((self.deck.card_in_action.suit == chosen_card.suit and chosen_card.rank == Rank.five) and self.deck.card_in_action.suit == Rank.four)\
				or ((self.deck.card_in_action.suit == chosen_card.suit and chosen_card.rank == Rank.six) and self.deck.card_in_action.suit == Rank.five)\
				or ((self.deck.card_in_action.suit == chosen_card.suit and chosen_card.rank == Rank.seven) and self.deck.card_in_action.suit == Rank.six)
		else:
			return self.deck.card_in_action is None \
				or ((self.deck.card_in_action.suit == chosen_card.suit and chosen_card.rank == Rank.four) and self.deck.card_in_action.suit in {Rank.five, Rank.six, Rank.seven}) \
				or ((self.deck.card_in_action.suit == chosen_card.suit or chosen_card.rank == Rank.eight) and not self.can_through_only_by_rank) \
				or self.deck.card_in_action.rank == chosen_card.rank \
				or self.deck.card_in_action.rank == Rank.three

	def _user_is_pressing_skip_button(self, mouse_pos):
		fits_x = self.skip_button_pos.x - 50 < mouse_pos.x < self.skip_button_pos.x + 50
		fits_y = self.skip_button_pos.y - 50 < mouse_pos.y < self.skip_button_pos.y + 50

		return self.show_skip_button and fits_x and fits_y

	def _make_a_move(self, card: Card):
		self.deck.deactivated_cards.add(self.deck.card_in_action)

		if self.current_player_move == USER:
			self.deck.user_cards.difference_update({card})
			self.user_cards_sprites.remove(card.sprite)

			user_cards_coords = [Point(100 + (i * 1.35) * 90, 750) for i in range(len(self.deck.user_cards))]
			self.sprite_moves.append(SpriteMove(list(self.user_cards_sprites), user_cards_coords))
			self.sprite_moves.append(SpriteMove([card.sprite], [TABLE_CENTER]))
		else:
			self.deck.agent_cards.difference_update({card})
			self.agent_cards_sprites = pg.sprite.Group([self.deck.create_card(Point(100 + i * 90, 150), Suit.back_side, Rank.back_side).sprite for i in range(len(self.deck.agent_cards))])
			card.sprite.pos = (100, 150)
			self.sprite_moves.append(SpriteMove([card.sprite], [TABLE_CENTER]))

		self.deck.card_in_action = card
		self.card_in_action_sprite_group = pg.sprite.Group([card.sprite])

		self._check_the_effect_of_the_move()

	def _check_the_effect_of_the_move(self):
		self.can_get_new_card = False
		self.show_skip_button = True
		self.can_through_only_by_rank = True

		if self.deck.card_in_action.rank == Rank.two:
			target_player = USER if self.current_player_move == AGENT else AGENT
			self._player_gets_a_card_from_deck(target_player)
			self._opponent_skips_move()

		elif self.deck.card_in_action.rank == Rank.three:
			self.can_get_new_card = True
			self.show_skip_button = False
			self.can_through_only_by_rank = False

		elif self.deck.card_in_action.rank == Rank.four:
			self.four_in_action = True
		
		elif self.deck.card_in_action.rank == Rank.seven:
			self.four_in_action = False
		
		elif self.deck.card_in_action.rank == Rank.jack:
			self._opponent_skips_move()

	def _player_gets_a_card_from_deck(self, player):
		random_card = self.deck.get_random_card_from_deck()

		if player == USER:
			self.deck.user_cards.add(random_card)
			self.user_cards_sprites.add(random_card.sprite)

			destination_pos = Point(100 + ((len(self.deck.user_cards) - 1) * 1.35) * 90, 750)
			self.sprite_moves.append(SpriteMove([random_card.sprite], [destination_pos]))
		else:
			self.deck.agent_cards.add(random_card)
			card_sprite = self.deck.create_card(DECK_POSITION, Suit.back_side, Rank.back_side).sprite
			self.agent_cards_sprites.add(card_sprite)

			destination_pos = Point(100 + (len(self.deck.agent_cards) - 1) * 90, 150)
			self.sprite_moves.append(SpriteMove([card_sprite], [destination_pos]))

	def _opponent_skips_move(self):
		self.show_skip_button = False
		self.can_get_new_card = True
		self.can_through_only_by_rank = False

	"""
	#########################################################################################
	#########################################################################################
	#########################################################################################
	#########################################################################################
	#########################################################################################
	#########################################################################################
	#########################################################################################
	"""

	def _ai_decide_which_move_to_make(self):
		ai_has_any_moves = len(self._ai_get_all_possible_moves())  # checking if there are any moves Agent can make

		if self.can_get_new_card and not ai_has_any_moves:
			self._player_gets_a_card_from_deck(AGENT)
			self.can_get_new_card = False
			self._ai_decide_which_move_to_make()  # getting a card from a deck, and checking if there are any possible moves again
		elif not ai_has_any_moves:  # we still have no possible moves, and we have already got a card from a deck
			if self.four_in_action and self.current_move_by == AGENT:
				for i in range(int(self.deck.card_in_action.rank)):
					self._player_gets_a_card_from_deck(USER)
				self.four_in_action = False
			self._ai_finishes_his_move()
		else:
			self.can_get_new_card = False

			possible_moves = self._ai_get_all_possible_moves()  # getting all possible moves
			best_card_to_move = max(possible_moves, key=self._ai_value_the_move)  # value each possible move, and choose the best one

			self._make_a_move(best_card_to_move)
			self.current_move_by = AGENT

	def _ai_value_the_move(self, move_card: Card) -> int:		
		if len(self.deck.user_cards) == 1:  # if user have only 1 card, the game is almost over, and we got to play aggressive in order not to lose 
			return self._ai_value_the_move_in_danger_situation(move_card)  # so in danger situation, the value of moves that makes our opponent get cards are higher

		suit, rank = move_card.suit, move_card.rank
		move_points = CARDS_POINTS_BY_RANK[rank]  # getting initial points of our card

		move_points += (self._ai_count_cards_with_specific_rank(rank) - 1) * 60  # counting the number of cards we can through up and giving extra points if there are any
		move_points += (self._ai_count_cards_with_specific_rank(rank) - 1) * CARDS_POINTS_BY_RANK[rank]  # we need it, so the sequence of two Aces will value more than two 9.

		if self._ai_count_cards_with_specific_suit(suit) == 1 and self._ai_count_cards_with_specific_rank(rank) == 1:
			move_points -= 70  # decreasing our points if we don't have the suit we are going to through
		return move_points
	
	def _ai_get_all_possible_moves(self):
		moves = []
		for card in self.deck.agent_cards:
			if self.can_make_move(card):
				moves.append(card)
		return moves

	def _ai_value_the_move_in_danger_situation(self, move_card: Card):
		suit, rank = move_card.suit, move_card.rank
		move_points = CARDS_POINTS_BY_RANK[rank]

		if rank == Rank.four:
			move_points += 250

		if rank == Rank.two:
			move_points += 120 * self._ai_count_cards_with_specific_rank(Rank.two)

		if self._ai_count_cards_with_specific_suit(suit) == 1 and self._ai_count_cards_with_specific_rank(rank) == 1:
			move_points -= 70

		return move_points

	def _ai_count_cards_with_specific_rank(self, rank):
		result = 0
		for card in self.deck.agent_cards:
			if card.rank == rank:
				result += 1
		return result

	def _ai_count_cards_with_specific_suit(self, suit):
		result = 0
		for card in self.deck.agent_cards:
			if card.suit == suit:
				result += 1
		return result

	def _ai_finishes_his_move(self):
		self.can_get_new_card = True
		self.show_skip_button = False
		self.can_through_only_by_rank = False
		self.current_player_move = USER

	def _ai_through_up_all_possible_cards(self):
		"""
			This method checks if we can through up any cards, and if not finishes the Agent move.

			By through up, I mean put additional cards, like:
				I have three cards: 9 spades 9 diamonds and 9 hearts, so I can make a move with 9 spades
				and through up 9 diamonds and 9 hearts.
		"""

		possible_thoughts = []

		if self.deck.card_in_action.rank == Rank.six:
			best_sequence = self._ai_find_best_sequence_to_cover_six(self.deck.card_in_action.suit)
			self._make_a_move(best_sequence[0])
		else:
			for card in self.deck.agent_cards:
				if self.deck.card_in_action.rank == card.rank:
					possible_thoughts.append(card)

			if possible_thoughts:
				self._make_a_move(max(possible_thoughts, key=self._ai_value_the_move))
			else:
				self._ai_finishes_his_move()

	def _ai_find_max_rank_sequence(self, suit):
		max_sequence = []
		for card in self.deck.agent_cards:
			if card.suit == suit and card.rank != Rank.six:
				if self._ai_count_cards_with_specific_rank(card.rank) > len(max_sequence):
					max_sequence = [card]

					for another_card in self.deck.agent_cards:
						if another_card.rank == card.rank and another_card.suit != card.suit:
							max_sequence.append(another_card)
		return max_sequence

	def _draw_game_over(self, winner):
		font = pg.font.SysFont('liberationmono', 60)
		game_over_text = font.render('GAME OVER', True, Color.LIGHT_RED, Color.WHITE)

		s_w, s_h = SCREEN_SIZE
		pos_game_over = game_over_text.get_rect(center=(s_w//2, s_h//2))

		winning_string = 'User is a winner' if winner == USER else 'Agent is a winner'
		winning_text = font.render(winning_string, True, Color.LIGHT_RED, Color.WHITE)
		pos_winner_text = winning_text.get_rect(center=(s_w//2, s_h//2 + 100))

		self.screen.blit(game_over_text, pos_game_over)
		self.screen.blit(winning_text, pos_winner_text)
		pg.display.update()

	def _render_skip_button(self):
		font = pg.font.SysFont('liberationmono', 60)

		skip_text = font.render('SKIP', True, Color.LIGHT_RED, Color.WHITE)
		pos_skip_text = skip_text.get_rect(center=(self.skip_button_pos.x, self.skip_button_pos.y))

		self.screen.blit(skip_text, pos_skip_text)
		pg.display.update()
