import re

BLUEPRINT = re.compile(r'Blueprint (?P<num>\d+): Each ore robot costs (?P<robot_ore>\d+) ore. Each clay robot costs (?P<clay_robot_ore>\d+) ore. Each obsidian robot costs (?P<obsidian_robot_ore>\d+) ore and (?P<obsidian_robot_clay>\d+) clay. Each geode robot costs (?P<geode_robot_ore>\d+) ore and (?P<geode_robot_obsidian>\d+) obsidian.')

def calc_quality(num, geodes):
  return num * geodes


BEST = 0

def calc_potential_earnings(time, geode, r_geode):
  return geode + (r_geode * time) + ((time * (time - 1)) / 2)

def calc_best_choice(time, ore, clay, obsidian, geode, r_ore, r_clay, r_obs, r_geode, m):
  global BEST

  if time <= 0:
    BEST = max(BEST, geode)
    return geode

  if calc_potential_earnings(time, geode, r_geode) < BEST:
    return geode


  choices = { k: 0 for k in ['none', 'ore', 'clay', 'obsidian', 'geode'] }

  if ore >= m['robot_ore'] and ore <= 4:
    choices['ore'] = calc_best_choice(
      time-1,
      ore+r_ore - m['robot_ore'], #
      clay+r_clay,
      obsidian+r_obs,
      geode+r_geode,
      r_ore + 1, #
      r_clay,
      r_obs,
      r_geode,
      m,
    )

  if ore >= m['clay_robot_ore'] and clay <= 20:
    choices['clay'] = calc_best_choice(
      time-1,
      ore+r_ore - m['clay_robot_ore'], #
      clay+r_clay,
      obsidian+r_obs,
      geode+r_geode,
      r_ore,
      r_clay + 1, #
      r_obs,
      r_geode,
      m
    )
  
  if ore >= m['obsidian_robot_ore'] and clay >= m['obsidian_robot_clay'] and obsidian <= 20:
    choices['obsidian'] = calc_best_choice(
      time-1,
      ore+r_ore - m['obsidian_robot_ore'], #
      clay+r_clay - m['obsidian_robot_clay'], #,
      obsidian+r_obs,
      geode+r_geode,
      r_ore,
      r_clay, 
      r_obs + 1, #
      r_geode,
      m,
    )
  

  if ore >= m['geode_robot_ore'] and obsidian >= m['geode_robot_obsidian']:
    choices['geode'] = calc_best_choice(
      time-1,
      ore+r_ore - m['geode_robot_ore'], #
      clay+r_clay,
      obsidian+r_obs - m['geode_robot_obsidian'], #
      geode+r_geode,
      r_ore,
      r_clay, 
      r_obs,
      r_geode + 1,  #
      m,
    )

  
  choices['none'] = calc_best_choice(
    time-1,
    ore+r_ore,
    clay+r_clay,
    obsidian+r_obs,
    geode+r_geode,
    r_ore,
    r_clay,
    r_obs,
    r_geode,
    m,
  )

  return max(choices.values())


def calc_geodes(blueprint):
  global BEST
  BEST = 0
  m = BLUEPRINT.search(blueprint)
  ore = 0
  clay = 0
  obsidian = 0
  geode = 0
  r_ore = 1
  r_clay = 0
  r_obs = 0
  r_geode = 0

  match = {
    'robot_ore': int(m['robot_ore']),
    'clay_robot_ore': int(m['clay_robot_ore']),
    'obsidian_robot_ore': int(m['obsidian_robot_ore']),
    'obsidian_robot_clay': int(m['obsidian_robot_clay']),
    'geode_robot_ore': int(m['geode_robot_ore']),
    'geode_robot_obsidian': int(m['geode_robot_obsidian'])
  }
  total_geodes =  calc_best_choice(24, ore, clay, obsidian, geode, r_ore, r_clay, r_obs, r_geode, match)
  return calc_quality(int(m['num']), total_geodes)

def run():
  data = []
  with open('file.txt', 'r') as f:
    while l := f.readline():
      data.append(l.strip())

  ans = sum(list(map(calc_geodes, data)))
  print(ans)

if __name__ == '__main__':
  run()