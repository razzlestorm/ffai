#!/usr/bin/env python3

import ffai
import ffai.ai.bots.testbots


# Load competition configuration for the bot bowl
config = ffai.load_config('bot-bowl-ii')

# Get ruleset
ruleset = ffai.load_rule_set(config.ruleset, all_rules=False)

# Load team to be used
human_team_a = ffai.load_team_by_filename('human', ruleset)
human_team_b = ffai.load_team_by_filename('human', ruleset)

# Random vs. Random
competition = ffai.Competition('MyCompetition', competitor_a_team=human_team_a, competitor_b_team=human_team_b, competitor_a_name='random', competitor_b_name='grodbot', config=config)
results = competition.run(num_games=2)
results.print()

# Random vs. idle
config.time_limits.game = 10  # 10 second time limit per game
config.time_limits.turn = 1  # 1 second time limit per turn
competition = ffai.Competition('MyCompetition', competitor_a_team=human_team_a, competitor_b_team=human_team_b, competitor_a_name='random', competitor_b_name='idle', config=config)
results = competition.run(num_games=2)
results.print()

# Random vs. violator
config.time_limits.game = 60  # 60 second time limit per game
config.time_limits.turn_ = 1  # 1 second time limit per turn
config.time_limits.secondary = 1  # 1 second time limit for secondary choices
config.time_limits.disqualification = 1  # 1 second disqualification limit 
competition = ffai.Competition('MyCompetition', competitor_a_team=human_team_a, competitor_b_team=human_team_b, competitor_a_name='random', competitor_b_name='violator', config=config)
results = competition.run(num_games=2)
results.print()

# Random vs. just-in-time
config.time_limits.game = 600  # 60 second time limit per game
config.time_limits.turn = 1  # 1 second time limit per turn
config.time_limits.secondary = 1  # 1 second time limit for secondary choices
config.time_limits.disqualification = 1  # 1 second disqualification limit 
#config.debug_mode = True
competition = ffai.Competition('MyCompetition', competitor_a_team=human_team_a, competitor_b_team=human_team_b, competitor_a_name='random', competitor_b_name='just-in-time', config=config)
results = competition.run(num_games=2)
results.print()

# Random vs. init crash
config.time_limits.game = 60  # 60 second time limit per game
config.time_limits.turn = 1  # 1 second time limit per turn
config.time_limits.secondary = 1  # 1 second time limit for secondary choices
config.time_limits.disqualification = 1  # 1 second disqualification threshold 
config.time_limits.init = 20  # 3 init limit
competition = ffai.Competition('MyCompetition', competitor_a_team=human_team_a, competitor_b_team=human_team_b, competitor_a_name='random', competitor_b_name='init-crash', config=config)
results = competition.run(num_games=2)
results.print()
