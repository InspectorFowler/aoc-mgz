from construct import *

"""Snapshot taken at the start of the recorded game

current_age and pop_max are both useful though not much else is
"""
player_stats = Struct("player_stats",
	Struct("resources",
		LFloat32("food"),
		LFloat32("wood"),
		LFloat32("stone"),
		LFloat32("gold"),
	),
	LFloat32("headroom"),
	LFloat32("u0"),
	LFloat32("current_age"),
	LFloat32("num_relics"),
	LFloat32("trade_bonus"),
	LFloat32("trade_goods"),
	LFloat32("trade_production"),
	LFloat32("pop_current"),
	LFloat32("decay"),
	LFloat32("discovery"),
	LFloat32("ruins"),
	LFloat32("meat"),
	LFloat32("berries"),
	LFloat32("fish"),
	LFloat32("u10"),
	LFloat32("total_units_created"),
	LFloat32("num_kills"),
	LFloat32("num_items_researched"),
	LFloat32("percent_map_explored"),
	LFloat32("u11"),
	LFloat32("u12"),
	LFloat32("u13"),
	LFloat32("u14"),
	LFloat32("convert_priests"),
	LFloat32("convert_buildings"),
	LFloat32("u17"),
	LFloat32("building_limit"),
	LFloat32("food_limit"),
	LFloat32("pop_max"),
	LFloat32("maintenance"),
	LFloat32("faith"),
	LFloat32("faith_recharge_rate"),
	LFloat32("farm_food_amount"),
	LFloat32("civilian_pop"),
	LFloat32("u23"),
	LFloat32("all_techs_achieved"),
	LFloat32("military_pop"),
	LFloat32("conversions"),
	LFloat32("num_wonders"),
	LFloat32("razings"),
	LFloat32("kill_ratio"),
	LFloat32("player_killed"),
	LFloat32("tribute_inefficiency"),
	LFloat32("gold_bonus_2"),
	LFloat32("town_center_unavailable"),
	LFloat32("total_gold_gathered_2"),
	LFloat32("writing"),
	LFloat32("u33"),
	LFloat32("monasteries"),
	LFloat32("total_resources_tributed"),
	LFloat32("hold_ruins"),
	LFloat32("hold_relics"),
	LFloat32("ore"),
	LFloat32("captured_unit"),
	LFloat32("u39"),
	LFloat32("trade_good_quality"),
	LFloat32("trade_market_level"),
	LFloat32("formations"),
	LFloat32("building_housing_rate"),
	LFloat32("gather_tax_rate"),
	LFloat32("gather_accumulator"),
	LFloat32("decay_rate"),
	LFloat32("allow_formations"),
	LFloat32("can_convert"),
	LFloat32("u49"),
	LFloat32("p1_kills"),
	LFloat32("p2_kills"),
	LFloat32("p3_kills"),
	LFloat32("p4_kills"),
	LFloat32("p5_kills"),
	LFloat32("p6_kills"),
	LFloat32("p7_kills"),
	LFloat32("p8_kills"),
	LFloat32("convert_resistance"),
	LFloat32("trade_vig_rate"),
	LFloat32("stone_bonus_x"),
	LFloat32("num_units_queued"),
	LFloat32("num_units_making"),
	LFloat32("raider"),
	LFloat32("boarding_recharge_rate"),
	LFloat32("starting_villagers"),
	LFloat32("research_cost_mod"),
	LFloat32("research_time_mod"),
	LFloat32("convert_boats"),
	LFloat32("fish_trap_food"),
	LFloat32("heal_rate_modifier"),
	LFloat32("heal_range"),
	LFloat32("food_bonus"),
	LFloat32("wood_bonus"),
	LFloat32("stone_bonus"),
	LFloat32("gold_bonus"),
	LFloat32("raider_ability"),
	LFloat32("berserker_heal_timer"),
	LFloat32("dominant_sheep_control"),
	LFloat32("object_cost_summation"),
	LFloat32("research_cost_summation"),
	LFloat32("relic_income_summation"),
	LFloat32("trade_income_summation"),
	LFloat32("p1_tributed_to"),
	LFloat32("p2_tributed_to"),
	LFloat32("p3_tributed_to"),
	LFloat32("p4_tributed_to"),
	LFloat32("p5_tributed_to"),
	LFloat32("p6_tributed_to"),
	LFloat32("p7_tributed_to"),
	LFloat32("p8_tributed_to"),
	LFloat32("p1_unit_kill_worth"),
	LFloat32("p2_unit_kill_worth"),
	LFloat32("p3_unit_kill_worth"),
	LFloat32("p4_unit_kill_worth"),
	LFloat32("p5_unit_kill_worth"),
	LFloat32("p6_unit_kill_worth"),
	LFloat32("p7_unit_kill_worth"),
	LFloat32("p8_unit_kill_worth"),
	LFloat32("p1_num_razes"),
	LFloat32("p2_num_razes"),
	LFloat32("p3_num_razes"),
	LFloat32("p4_num_razes"),
	LFloat32("p5_num_razes"),
	LFloat32("p6_num_razes"),
	LFloat32("p7_num_razes"),
	LFloat32("p8_num_razes"),
	LFloat32("p1_raze_worth"),
	LFloat32("p2_raze_worth"),
	LFloat32("p3_raze_worth"),
	LFloat32("p4_raze_worth"),
	LFloat32("p5_raze_worth"),
	LFloat32("p6_raze_worth"),
	LFloat32("p7_raze_worth"),
	LFloat32("p8_raze_worth"),
	LFloat32("num_castles"),
	LFloat32("u73"),
	LFloat32("kills_by_p1"),
	LFloat32("kills_by_p2"),
	LFloat32("kills_by_p3"),
	LFloat32("kills_by_p4"),
	LFloat32("kills_by_p5"),
	LFloat32("kills_by_p6"),
	LFloat32("kills_by_p7"),
	LFloat32("kills_by_p8"),
	LFloat32("razings_by_p1"),
	LFloat32("razings_by_p2"),
	LFloat32("razings_by_p3"),
	LFloat32("razings_by_p4"),
	LFloat32("razings_by_p5"),
	LFloat32("razings_by_p6"),
	LFloat32("razings_by_p7"),
	LFloat32("razings_by_p8"),
	LFloat32("value_killed_by_others"),
	LFloat32("value_razed_by_others"),
	LFloat32("kills"),
	LFloat32("losses"),
	LFloat32("p1_tribute_recvd"),
	LFloat32("p2_tribute_recvd"),
	LFloat32("p3_tribute_recvd"),
	LFloat32("p4_tribute_recvd"),
	LFloat32("p5_tribute_recvd"),
	LFloat32("p6_tribute_recvd"),
	LFloat32("p7_tribute_recvd"),
	LFloat32("p8_tribute_recvd"),
	LFloat32("current_unit_worth"),
	LFloat32("current_building_worth"),
	LFloat32("total_food_gathered"),
	LFloat32("total_wood_gathered"),
	LFloat32("total_stone_gathered"),
	LFloat32("total_gold_gathered"),
	LFloat32("total_kill_and_raze_worth"),
	LFloat32("total_tribute_recvd"),
	LFloat32("total_value_of_razings"),
	LFloat32("castle_high"),
	LFloat32("wonder_high"),
	LFloat32("total_tribute_sent"),
	LFloat32("convert_min_adj"),
	LFloat32("convert_max_adj"),
	LFloat32("convert_resist_min_adj"),
	LFloat32("convert_resist_max_adj"),
	LFloat32("convert_building_min"),
	LFloat32("convert_building_max"),
	LFloat32("convert_building_chance"),
	LFloat32("spies"),
	LFloat32("value_wonders_castles"),
	LFloat32("food_score"),
	LFloat32("wood_score"),
	LFloat32("stone_score"),
	LFloat32("gold_score"),
	LFloat32("wood_bonus0"),
	LFloat32("food_bonus0"),
	LFloat32("relic_rate"),
	LFloat32("heresy"),
	LFloat32("theocracy"),
	LFloat32("crenellations"),
	LFloat32("construction_rate_mod"),
	LFloat32("hun_wonder_bonus"),
	LFloat32("spies_discount"),
)